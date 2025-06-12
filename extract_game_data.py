import requests
import pandas as pd
import re
import janitor

def extract_pbp_data(json):
    """
    Extracts the CEBL play by play data from JSON.

    Parameters
    ----------
    json : dict
        The JSON response containing play-by-play and shot data.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the play by play data for a specific game

    """

    # Extract and normalize play-by-play data
    pbp_df = pd.json_normalize(json['pbp']).clean_names(case_type="snake")
    
    # Clean and rename columns
    pbp_df = pbp_df.drop(columns= ['scoreboard_name']).rename(columns={'player' : 'scoreboard_name'})
    pbp_df['player'] = pbp_df['first_name'] + ' ' + pbp_df['family_name']
    pbp_df['game_id'] = json['game_id']

    # Expand qualifier column into seperate columns
    qualifier_df = pd.DataFrame(pbp_df['qualifier'].tolist()).add_prefix('qualifier_')
    pbp_df = pd.concat([pbp_df.drop(columns=['qualifier']), qualifier_df], axis=1)

    # Extract and combine shot data from both teams
    shot_df_team1 = pd.json_normalize(json['tm']['1']['shot']).clean_names(case_type="snake")
    shot_df_team2 = pd.json_normalize(json['tm']['2']['shot']).clean_names(case_type="snake")
    shot_df = pd.concat([shot_df_team1, shot_df_team2], ignore_index=True)

    # Merge shot coordinates with play-by-play data
    pbp_df = pbp_df.merge(
        shot_df[["action_number", "x", "y"]],
        on="action_number",
        how="left"
    )

    # Clean null values and rename final columns
    pbp_df = pbp_df.fillna(pd.NA).replace({None: pd.NA, "": pd.NA})
    
    column_mapping = {
        "gt": "game_time",
        "s1": "home_score",
        "s2": "away_score",
        "lead": "home_lead",
        "tno": "team_id",
        "pno": "player_id",
    }
    pbp_df = pbp_df.rename(columns=column_mapping)

    # Convert data types
    dtype_mapping = {
        'game_id': int,
    }
    pbp_df = pbp_df.astype(dtype_mapping)

    return pbp_df

def extract_official_data(json):
    """
    Extracts the CEBL official data from JSON.

    Parameters
    ----------
    json : dict
        The JSON response containing the official data.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame containing the official data for a specific game
    """

    # Extract and normalize official data
    official_df = pd.json_normalize(json['officials'].values()).clean_names(case_type="snake")
    official_df['game_id'] = json['game_id']

    # Convert data types
    dtype_mapping = {
        'game_id': int,
    }
    official_df = official_df.astype(dtype_mapping)

    return official_df

def extract_player_data(json):
    """
    Extract and clean player data from game JSON.

    Parameters
    ----------
    json : dict
        The JSON response containing the player data.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame containing the player data for a specific game
    """

    # Extract player data from both teams
    team_1_players_df = pd.json_normalize(json['tm']['1']['pl'].values()).clean_names(case_type="snake")
    team_2_players_df = pd.json_normalize(json['tm']['2']['pl'].values()).clean_names(case_type="snake")
    player_df = pd.concat([team_1_players_df, team_2_players_df], ignore_index=True)

    # Add game ID
    player_df['game_id'] = json['game_id']

    # Column renaming mapping
    column_mapping = {
        "s_minutes": "minutes",
        "s_field_goals_made": "field_goals_made",
        "s_field_goals_attempted": "field_goals_attempted",
        "s_field_goals_percentage": "field_goal_percentage",
        "s_three_pointers_made": "three_point_field_goals_made",
        "s_three_pointers_attempted": "three_point_field_goals_attempted",
        "s_three_pointers_percentage": "three_point_percentage",
        "s_two_pointers_made": "two_point_field_goals_made",
        "s_two_pointers_attempted": "two_point_field_goals_attempted",
        "s_two_pointers_percentage": "two_point_percentage",
        "s_free_throws_made": "free_throws_made",
        "s_free_throws_attempted": "free_throws_attempted",
        "s_free_throws_percentage": "free_throw_percentage",
        "s_rebounds_defensive": "rebounds_defensive",
        "s_rebounds_offensive": "rebounds_offensive",
        "s_rebounds_total": "rebounds",
        "s_assists": "assists",
        "s_turnovers": "turnovers",
        "s_steals": "steals",
        "s_blocks": "blocks",
        "s_blocks_received": "blocks_received",
        "s_fouls_personal": "fouls_personal",
        "s_fouls_on": "fouls_drawn",
        "s_points": "points",
        "s_points_second_chance": "points_second_chance",
        "s_points_fast_break": "points_fast_break",
        "s_plus_minus_points": "plus_minus",
        "s_points_in_the_paint": "points_in_the_paint",
        "playing_position": "position",
        "shirt_number": "jersey_number",
    }
    player_df = player_df.rename(columns=column_mapping)

    # Drop unnecessary columns
    columns_to_drop = [
        'comp_s_minutes_average', 
        'comp_s_points_average',
        'comp_s_rebounds_total_average', 
        'comp_s_assists_average',
        'name',
    ]
    player_df = player_df.drop(columns=columns_to_drop)
    
    # Create full name from first and last name
    player_df['name'] = player_df['first_name'] + ' ' + player_df['family_name']
    
    # Clean and convert data types
    player_df['captain'] = player_df['captain'].fillna(0)

    dtype_mapping = {
        'captain': bool,
        'game_id': int,
        'jersey_number': int,
        'starter': bool,
        'active': bool,
        'eff_1' : float,
        'eff_2' : float,
        'eff_5' : float,
        'eff_6' : float,
        'eff_6' : float,
        'eff_7' : float,
    }
    player_df = player_df.astype(dtype_mapping)
    return player_df

def extract_team_data(json):
    """
    Extract and clean team data from game JSON.

    Parameters
    ----------
    json : dict
        The JSON response containing the team data.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame containing the team data for a specific game
    """

    # Extract and clean team data for both teams
    team_data_one = json['tm']['1']
    team_data_two = json['tm']['2']
    
    # Keys to exclude from team data
    keys_to_remove = ['coachDetails', 'assistcoach1Details', 'assistcoach2Details', 'pl', 'shot', 'scoring', 'lds']
    for key in keys_to_remove:
        team_data_one.pop(key, None)  # avoids KeyError if key doesn't exist
        team_data_two.pop(key, None)

    # Normalize and combine team data
    team_df_one = pd.json_normalize(team_data_one)
    team_df_two = pd.json_normalize(team_data_two)
    team_df = pd.concat([team_df_one, team_df_two], ignore_index=True)

    # Clean columns and add game ID
    team_df = team_df.clean_names(case_type="snake")
    team_df['game_id'] = json['game_id']

    # Column renaming mapping
    column_mapping = {
        'tot_s_field_goals_made': 'field_goals_made',
        'tot_s_field_goals_attempted': 'field_goals_attempted',
        'tot_s_field_goals_percentage': 'field_goal_percentage',
        'tot_s_three_pointers_made': 'three_point_field_goals_made',
        'tot_s_three_pointers_attempted': 'three_point_field_goals_attempted',
        'tot_s_three_pointers_percentage': 'three_point_percentage',
        'tot_s_two_pointers_made': 'two_point_field_goals_made',
        'tot_s_two_pointers_attempted': 'two_point_field_goals_attempted',
        'tot_s_two_pointers_percentage': 'two_point_percentage',
        'tot_s_free_throws_made': 'free_throws_made',
        'tot_s_free_throws_attempted': 'free_throws_attempted',
        'tot_s_free_throws_percentage': 'free_throw_percentage',
        'tot_s_rebounds_defensive': 'rebounds_defensive',
        'tot_s_rebounds_offensive': 'rebounds_offensive',
        'tot_s_rebounds_total': 'rebounds',
        'tot_s_assists': 'assists',
        'tot_s_turnovers': 'turnovers',
        'tot_s_steals': 'steals',
        'tot_s_blocks': 'blocks',
        'tot_s_blocks_received': 'blocks_received',
        'tot_s_fouls_personal': 'fouls_personal',
        'tot_s_fouls_on': 'fouls_drawn',
        'tot_s_fouls_total': 'fouls_total',
        'tot_s_points': 'points',
        'tot_s_points_from_turnovers': 'points_from_turnovers',
        'tot_s_points_second_chance': 'points_second_chance',
        'tot_s_points_fast_break': 'points_fast_break',
        'tot_s_bench_points': 'points_bench',
        'tot_s_points_in_the_paint': 'points_in_the_paint',
        'tot_s_time_leading': 'time_leading',
        'tot_s_biggest_lead': 'biggest_lead',
        'tot_s_biggest_scoring_run': 'biggest_scoring_run',
        'tot_s_lead_changes': 'lead_changes',
        'tot_s_times_scores_level': 'times_scores_level',
        'tot_s_fouls_team': 'team_fouls',
        'tot_s_rebounds_team': 'team_rebounds',
        'tot_s_rebounds_team_defensive': 'team_rebounds_defensive',
        'tot_s_rebounds_team_offensive': 'team_rebounds_offensive',
        'tot_s_turnovers_team': 'team_turnovers',
    }
    
    # Apply column renaming
    team_df = team_df.rename(columns=column_mapping)

    # Data type conversions
    dtype_mapping = {
        'game_id': int,
        'tot_eff_1': float,
        'tot_eff_2': float,
        'tot_eff_3': float,
        'tot_eff_4': float,
        'tot_eff_5': float,
        'tot_eff_6': float,
        'tot_eff_7': float,
    }

    return team_df

def extract_coach_data(json):
    """
    Extract and clean coach data from game JSON.

    Parameters
    ----------
    json : dict
        The JSON response containing the coach data.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame containing the coach data for a specific game
    """
    coach_df = []
    for team_num in ['1', '2']:
        head_coach_data = json['tm'][team_num]['coachDetails']
        assist_coach_1_data = json['tm'][team_num]['assistcoach1Details']
        assist_coach_2_data = json['tm'][team_num]['assistcoach2Details']

        head_coach_df = pd.json_normalize(head_coach_data)
        assist_coach_1_df = pd.json_normalize(assist_coach_1_data)
        assist_coach_2_df = pd.json_normalize(assist_coach_2_data)

        coach_df.append(head_coach_df)
        coach_df.append(assist_coach_1_df)
        coach_df.append(assist_coach_2_df)

    coach_df = pd.concat(coach_df, ignore_index=True)
    coach_df = coach_df.clean_names(case_type="snake")
    coach_df['head_coach'] = coach_df.index.isin([0, 3])

    return coach_df