import requests
import pandas as pd
import re
import janitor

def extract_pbp_data(json):
    """
    Extracts the CEBL play by play data from JSON response.

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