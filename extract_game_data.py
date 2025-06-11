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
    pbp_data = json['pbp']
    pbp_df = pd.json_normalize(pbp_data)

    pbp_df = pbp_df.clean_names(case_type="snake")
    pbp_df = pbp_df.drop(columns= ['scoreboard_name'])
    pbp_df = pbp_df.rename(columns={'player' : 'scoreboard_name'})
    pbp_df['player'] = pbp_df['first_name'] + ' ' + pbp_df['family_name']
    pbp_df['game_id'] = json['game_id']

    qualifier_df = pd.DataFrame(pbp_df['qualifier'].tolist()).add_prefix('qualifier_')
    pbp_df = pd.concat([pbp_df.drop(columns=['qualifier']), qualifier_df], axis=1)

    shot_data_one = json['tm']['1']['shot']
    shot_data_two = json['tm']['2']['shot']
    shot_df_one = pd.json_normalize(shot_data_one)
    shot_df_two = pd.json_normalize(shot_data_two)
    shot_df = pd.concat([shot_df_one, shot_df_two], ignore_index=True)

    shot_df = shot_df.clean_names(case_type="snake")
    pbp_df = pbp_df.merge(
        shot_df[["action_number", "x", "y"]],
        on="action_number",
        how="left"
    )

    pbp_df = pbp_df.fillna(pd.NA)
    pbp_df = pbp_df.replace({None: pd.NA})
    pbp_df = pbp_df.rename(columns={
        "gt": "game_time",
        "s1": "home_score",
        "s2": "away_score",
        "lead": "home_lead",
        "tno": "team_id",
        "pno": "player_id",
    })

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
    official_data = json['officials']
    official_df = pd.json_normalize(official_data.values())
    official_df = official_df.clean_names(case_type="snake")
    official_df['game_id'] = json['game_id']

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