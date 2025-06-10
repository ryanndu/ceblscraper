import requests
import pandas as pd
import re

def get_cebl_schedule(year):
    """
    Fetches the CEBL game schedule for a given year.

    Parameters
    ----------
    year (int): The season year (e.g., 2023) to retrieve the schedule for.

    Returns
    -------
        pandas.DataFrame: A DataFrame containing the schedule and metadata for that season.
    """
    headers = {
    "x-api-key": "800chyzv2hvur3z0ogh39cve2zok0c",
    "accept": "application/json"
    }
    schedule_url = "https://api.data.cebl.ca/games/" + str(year) + "/"
    schedule_json_data = requests.get(schedule_url, headers=headers).json()
    yearly_data = pd.json_normalize(schedule_json_data)
    yearly_data['season'] = year
    cols = ['id', 'season', 'start_time_utc', 'status', 'competition', 'venue_name', 'period', 'home_team_id', 'home_team_name', 'home_team_score',
            'home_team_logo_url', 'home_team_stats_url_en', 'home_team_stats_url_fr','away_team_id', 'away_team_name',
            'away_team_score', 'away_team_logo_url', 'away_team_stats_url_en', 'away_team_stats_url_fr', 'stats_url_en', 'stats_url_fr', 'cebl_stats_url_en',
            'cebl_stats_url_fr', 'tickets_url_en', 'tickets_url_fr']
    yearly_data = yearly_data[cols]
    yearly_data['fiba_id'] = yearly_data['cebl_stats_url_en'].str.extract(r"id=(\d+)")
    yearly_data['fiba_json_url'] = "https://fibalivestats.dcd.shared.geniussports.com/data/" + yearly_data['fiba_id'] + "/data.json"
    yearly_data.drop(columns='fiba_id', inplace=True)
    return yearly_data