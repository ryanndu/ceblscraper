# CEBL Schedule Data Dictionary

## Preamble

This document explores the nested JSON structure for CEBL schedule data.

### Data Dictionary

```python
url = "https://api.data.cebl.ca/games/2025/"
```

### Game Schedule Data

All game schedules have the following format:

- **`home_team_id`** (*int*): Unique identifier for the home team, ex: `18`
- **`home_team_name`** (*str*): Name of the home team, ex: `Edmonton Stingers`
- **`home_team_logo_url`** (*str*): URL to the home team's logo, ex: `https://se-img.dcd-production.i.geniussports.com/b16d89027cdf127f5d1c8529e43a8afaM1.png`
- **`home_team_stats_url_en`** (*str*): URL to the home team's stats page, ex: `https://cebl.ca/stats/edmonton`
- **`home_team_stats_url_fr`** (*str*): URL to the home team's stats page in French, ex: `https://cebl.ca/fr-ca/stats/edmonton`
- **`away_team_id`** (*int*): Unique identifier for the away team, ex: `17`
- **`away_team_name`** (*str*): Name of the away team, ex: `Calgary Surge`
- **`away_team_logo_url`** (*str*): URL to the away team's logo, ex: `https://se-img.dcd-production.i.geniussports.com/54ef29f1411f501cd4e00036c8a046e9M1.png`
- **`away_team_stats_url_en`** (*str*): URL to the away team's stats page, ex: `https://cebl.ca/stats/calgary`
- **`away_team_stats_url_fr`** (*str*): URL to the away team's stats page in French, ex: `https://cebl.ca/fr-ca/stats/calgary`
- **`stats_url_en`** (*str*): URL to the game stats page in English, ex: `https://cebl.ca/stats/2023-06-01/edmonton-vs-calgary`
- **`stats_url_fr`** (*str*): URL to the game stats page in French, ex: `https://www.cebl.ca/fr-ca/game?id=2600563`
- **`tickets_url_en`** (*str*): URL to purchase tickets for the game in English, ex: `https://www.thestingers.ca/tickets?language=en-ca`
- **`tickets_url_fr`** (*str*): URL to purchase tickets for the game in French, ex: `https://www.thestingers.ca/tickets?language=fr-ca`
- **`broadcast_partner_logo_urls`** (*list*): List of URLs to broadcast partner logos
  - **`0`** (*str*): URL to the first broadcast partner logo, ex: `https://storage.googleapis.com/cebl/logos/broadcasters/game-plus.png`
  - Other entries follow the same format
- **`id`** (*int*): Unique identifier for the game, ex: `14708701`
- **`start_time_utc`** (*str*): Start time of the game in UTC, ex: `2025-05-11T22:00:00Z`
- **`home_team_score`** (*int*): Score of the home team, ex: `84`
- **`away_team_score`** (*int*): Score of the away team, ex: `86`
- **`competition`** (*str*): Type of game, ex: `"REGULAR"`
- **`status`** (*str*): Current status of the game, ex: `"COMPLETE"`
- **`venue_name`** (*str*): Name of the venue where the game is played, ex: `Edmonton Expo Centre`
- **`period`** (*int*): Current period of the game, ex: `4` or `null` if game is not in progress
- **`fiba_json_url`** (*str*): URL to the FIBA JSON data for the game, ex: `"https://fibalivestats.dcd.shared.geniussports.com/data/2600563/data.json"`