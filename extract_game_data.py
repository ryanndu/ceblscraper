import requests
import pandas as pd
import re
import janitor
import helpers

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
        "s_rebounds_defensive": "defensive_rebounds",
        "s_rebounds_offensive": "offensive_rebounds",
        "s_rebounds_total": "rebounds",
        "s_assists": "assists",
        "s_turnovers": "turnovers",
        "s_steals": "steals",
        "s_blocks": "blocks",
        "s_blocks_received": "blocks_received",
        "s_fouls_personal": "personal_fouls",
        "s_fouls_on": "fouls_drawn",
        "s_points": "points",
        "s_points_second_chance": "second_chance_points",
        "s_points_fast_break": "fast_break_points",
        "s_plus_minus_points": "plus_minus",
        "s_points_in_the_paint": "points_in_the_paint",
        "playing_position": "position",
        "shirt_number": "player_number",
        "family_name": "last_name",
        "family_name_initial": "last_name_initial",
        "international_family_name": "international_last_name",
        "international_family_name_initial": "international_last_name_initial",
        "eff_1": "index_rating",
        "eff_2": "index_rating_2",
        "eff_3": "index_rating_3",
        "eff_4": "index_rating_4",
        "eff_5": "index_rating_5",
        "eff_6": "index_rating_6",
        "eff_7": "index_rating_7",
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
    player_df['player_name'] = player_df['first_name'] + ' ' + player_df['last_name']
    
    # Clean and convert data types
    player_df['captain'] = player_df['captain'].fillna(0)

    dtype_mapping = {
        'captain': bool,
        'game_id': int,
        'player_number': int,
        'starter': bool,
        'active': bool,
        'index_rating' : float,
        'index_rating_2' : float,
        'index_rating_5' : float,
        'index_rating_6' : float,
        'index_rating_7' : float,
    }
    player_df = player_df.astype(dtype_mapping)

    # Reorder columns
    column_order = ['game_id', 'player_number', 'player_name', 'position', 'minutes', 'points', 'field_goals_made', 'field_goals_attempted', 
                    'field_goal_percentage', 'two_point_field_goals_made', 'two_point_field_goals_attempted', 'two_point_percentage',
                    'three_point_field_goals_made', 'three_point_field_goals_attempted', 'three_point_percentage', 'free_throws_made', 
                    'free_throws_attempted', 'free_throw_percentage', 'offensive_rebounds', 'defensive_rebounds', 'rebounds', 'assists',
                    'turnovers', 'steals', 'blocks', 'blocks_received', 'personal_fouls', 'fouls_drawn', 'plus_minus', 'index_rating',
                    'index_rating_2', 'index_rating_3', 'index_rating_4', 'index_rating_5', 'index_rating_6', 'index_rating_7', 'second_chance_points',
                    'fast_break_points', 'points_in_the_paint', 'first_name', 'first_name_initial', 'last_name', 'last_name_initial',
                    'international_first_name', 'international_first_name_initial', 'international_last_name', 'international_last_name_initial',
                    'scoreboard_name', 'active', 'starter', 'captain', 'photo_t', 'photo_s']
    player_df = player_df[column_order]

    return player_df

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
    keys_to_remove = ['coachDetails', 'assistcoach1Details', 'assistcoach2Details', 'pl', 'shot', 'scoring', 'lds', 'full_score', 'points', 'asstSep', 'tot_sPoints']
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
        'tot_s_rebounds_defensive': 'defensive_rebounds',
        'tot_s_rebounds_offensive': 'offensive_rebounds',
        'tot_s_rebounds_total': 'rebounds',
        'tot_s_assists': 'assists',
        'tot_s_turnovers': 'turnovers',
        'tot_s_steals': 'steals',
        'tot_s_blocks': 'blocks',
        'tot_s_blocks_received': 'blocks_received',
        'tot_s_fouls_personal': 'personal_fouls',
        'tot_s_fouls_on': 'fouls_drawn',
        'tot_s_fouls_total': 'total_fouls',
        'tot_s_points_from_turnovers': 'points_from_turnovers',
        'tot_s_points_second_chance': 'second_chance_points',
        'tot_s_points_fast_break': 'fast_break_points',
        'tot_s_bench_points': 'bench_points',
        'tot_s_points_in_the_paint': 'points_in_the_paint',
        'tot_s_time_leading': 'time_leading',
        'tot_s_biggest_lead': 'biggest_lead',
        'tot_s_biggest_scoring_run': 'biggest_scoring_run',
        'tot_s_lead_changes': 'lead_changes',
        'tot_s_times_scores_level': 'times_scores_level',
        'tot_s_fouls_team': 'team_fouls',
        'tot_s_rebounds_team': 'team_rebounds',
        'tot_s_rebounds_team_defensive': 'team_defensive_rebounds',
        'tot_s_rebounds_team_offensive': 'team_offensive_rebounds',
        'tot_s_turnovers_team': 'team_turnovers',
        'tot_eff_1': 'team_index_rating',
        'tot_eff_2': 'team_index_rating_2',
        'tot_eff_3': 'team_index_rating_3',
        'tot_eff_4': 'team_index_rating_4',
        'tot_eff_5': 'team_index_rating_5',
        'tot_eff_6': 'team_index_rating_6',
        'tot_eff_7': 'team_index_rating_7',
        'name': 'team_name',
        'tot_s_minutes': 'minutes',
        'score': 'team_score',
        'assistcoach1': 'assistant_coach_1',
        'assistcoach2': 'assistant_coach_2',
        'coach': 'head_coach',
        'name_international': 'international_team_name',
        'short_name_international': 'international_short_name',
        'code_international': 'international_code',
        'p1_score': 'period_1_score',
        'p2_score': 'period_2_score',
        'p3_score': 'period_3_score',
        'p4_score': 'period_4_score',
        'fouls': 'bonus_fouls',

    }
    team_df = team_df.rename(columns=column_mapping)

    # Data type conversions
    dtype_mapping = {
        'game_id': int,
        'team_index_rating': float,
        'team_index_rating_2': float,
        'team_index_rating_3': float,
        'team_index_rating_4': float,
        'team_index_rating_5': float,
        'team_index_rating_6': float,
        'team_index_rating_7': float,
    }
    team_df = team_df.astype(dtype_mapping)

    # Reorder columns
    column_order = ['game_id', 'team_name', 'short_name', 'code', 'team_score', 'minutes', 'field_goals_made', 'field_goals_attempted', 'field_goal_percentage',
                    'two_point_field_goals_made', 'two_point_field_goals_attempted', 'two_point_percentage', 'three_point_field_goals_made', 'three_point_field_goals_attempted',
                    'three_point_percentage', 'free_throws_made', 'free_throws_attempted', 'free_throw_percentage', 'offensive_rebounds', 'defensive_rebounds',
                    'rebounds', 'assists', 'steals', 'turnovers', 'blocks', 'blocks_received', 'personal_fouls', 'fouls_drawn', 'total_fouls', 'bonus_fouls',
                    'points_in_the_paint', 'second_chance_points', 'points_from_turnovers', 'bench_points', 'fast_break_points', 'team_index_rating', 
                    'team_index_rating_2', 'team_index_rating_3', 'team_index_rating_4', 'team_index_rating_5', 'team_index_rating_6', 'team_index_rating_7',
                    'team_fouls', 'team_turnovers', 'team_rebounds', 'team_defensive_rebounds', 'team_offensive_rebounds', 'period_1_score', 'period_2_score',
                    'period_3_score', 'period_4_score', 'biggest_lead', 'biggest_scoring_run', 'time_leading', 'lead_changes', 'times_scores_level', 'timeouts',
                    'head_coach', 'assistant_coach_1', 'assistant_coach_2', 'international_team_name', 'international_short_name', 'international_code', 'logo',
                    'logo_t_url', 'logo_t_size', 'logo_t_height', 'logo_t_width', 'logo_t_bytes', 'logo_s_url', 'logo_s_size', 'logo_s_height', 'logo_s_width',
                    'logo_s_bytes',]
    team_df = team_df[column_order]

    team_df['minutes'] = team_df['minutes'].apply(helpers.normalize_time)
    team_df["biggest_lead"] = team_df["biggest_lead"].fillna(0)

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
    
    coach_df_list = []
    
    # Extract coach data from both teams
    for team_num in ['1', '2']:
        team_data = json['tm'][team_num]
        team_name = team_data['name']
        
        # Extract different coach types
        coaches_data = [
            (team_data['coachDetails'], 'Head Coach'),
            (team_data['assistcoach1Details'], 'Assistant Coach'),
            (team_data['assistcoach2Details'], 'Assistant Coach')
        ]
        
        for coach_data, coach_type in coaches_data:
            coach_record = pd.json_normalize(coach_data)
            coach_record['team_name'] = team_name
            coach_record['coach_type'] = coach_type
            coach_df_list.append(coach_record)
    
    # Combine and clean
    coach_df = pd.concat(coach_df_list, ignore_index=True)
    coach_df = coach_df.clean_names(case_type="snake")
    
    # Add game ID
    coach_df['game_id'] = json['game_id']
    
    # Column renaming mapping
    column_mapping = {
        'family_name': 'last_name',
        'family_name_initial': 'last_name_initial',
        'international_family_name': 'international_last_name',
        'international_family_name_initial': 'international_last_name_initial',
    }
    coach_df = coach_df.rename(columns=column_mapping)
    
    # Add coach full name
    coach_df['coach_name'] = coach_df['first_name'] + ' ' + coach_df['last_name']
    
    # Convert data types
    dtype_mapping = {
        'game_id': int,
    }
    
    for col, dtype in dtype_mapping.items():
        coach_df[col] = coach_df[col].astype(dtype)
    
    # Reorder columns
    column_order = [
        'game_id', 'team_name', 'coach_name', 'coach_type',
        'first_name', 'first_name_initial', 'last_name', 'last_name_initial',
        'international_first_name', 'international_first_name_initial', 
        'international_last_name', 'international_last_name_initial',
        'scoreboard_name',
    ]
    coach_df = coach_df[column_order]
    
    return coach_df