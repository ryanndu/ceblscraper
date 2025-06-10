import requests
import pandas as pd
import re
import janitor

def extract_pbp_data(json):
    """
    Extracts the CEBL play by play data from CEBL JSON.

    Parameters
    ----------
    json : dict
        The JSON response containing play-by-play data

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

    pbp_df = pbp_df.rename(columns={
        "gt": "clock",
        "s1": "home_score",
        "s2": "away_score",
        "lead": "home_lead",
        "tno": "team_id",
        "pno": "player_number",
    })

    column_order = ['period', 'period_type', 'clock', 'home_score', 'away_score', 'home_lead', 'team_id',
                    'player_number', 'player', 'scoreboard_name', 'action_type', 'sub_type', 'success', 
                    'scoring', 'qualifier', 'first_name', 'family_name', 'first_name_initial', 'family_name_initial',
                    'international_first_name_initial', 'international_family_name_initial']
    pbp_df = pbp_df[column_order]
    
    return pbp_df

