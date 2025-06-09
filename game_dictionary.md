# CEBL Game Data Dictionary

## Preamble

This document explores the nested JSON structure for CEBL game data.

### Data Dictionary

```python
url = "https://fibalivestats.dcd.shared.geniussports.com/data/2600564/data.json"
```

### Game Metadata

- **`clock`** (*string*): Time remaining in period, ex: `"3:18"`
- **`period`** (*int*): Current period number, ex: `2`
- **`periodLength`** (*int*): Length of each period in minutes (typically `10`)
- **`periodType`** (*string*): Type of period, ex: `"REGULAR"`
- **`inOT`** (*bool*): Indicates if the game is in overtime, (yes: `1`, no: `0`)

### tm (`Team Data`)

**`tm`** (*list*): List of two dictionaries, each containing detailed data for one team (home: `1`, away: `2`).

#### Team Identification

- **`name`** (*string*): Full team name, ex: `"Saskatchewan Rattlers"`
- **`nameInternational`** (*string*): International team name
- **`shortName`** (*string*): Short team name, ex: `"Saskatchewan"`
- **`shortNameInternational`** (*string*): International short team name
- **`logo`** (*string*): Logo identifier or empty string
- **`logoT`**, **`logoS`** (*dict*): Logo objects with:
  - **`size`** (*string*): Size type, ex: `"T1"` or `"S1"`
  - **`height`** (*int*), **`width`** (*int*): Dimensions in pixels
  - **`bytes`** (*int*): File size in bytes
  - **`url`** (*string*): Logo image url
- **`code`** (*string*): Team code, ex: `"SSK"`
- **`codeInternational`** (*string*): International team code

#### Coaching Staff

##### Head Coach
- **`coach`** (*string*): Head coach name, ex: `"Eric Magdenz"`
- **`coachDetails`** (*dict*): Coach metadata
  - **`firstName`** (*string*): First name, ex: `"Eric"`
  - **`familyName`** (*string*): Last name, ex: `"Magdenz"`
  - **`internationalFirstName`** (*string*): International first name
  - **`internationalFamilyName`** (*string*): International last name
  - **`firstNameInitial`** (*string*): First name initial, ex: `"E"`
  - **`familyNameInitial`** (*string*): Last name initial, ex: `"M"`
  - **`internationalFirstNameInitial`** (*string*): International first name initial
  - **`internationalFamilyNameInitial`** (*string*): International last name initial
  - **`scoreboardName`** (*string*): Display name for scoreboard purposes, ex: `"E. Magdenz"`
  
##### Assistant Coaches
- **`assistcoach1`**, **`assistcoach2`** (*string*): Assistant coach names, ex: `"Steve Burrows"` and `"Robert Lovelace"`
- **`assistCoach1Details`**, **`assistCoach2Details`** (*dict*): Assistant coach metadata
  - Same structure as `coachDetails`:

#### Game & Stat Info

- **`asstSep`** (*string*): Separator for multi-player assist strings, ex: `","`

##### Team Stats

- **`score`** (*int*): Current score, ex: `65`
- **`full_score`** (*int*): Final score, ex: `65`
- **`tot_sMinutes`** (*string*): Minutes played, ex: `"199:60"`

> ⚠️ May include invalid formats like `199:60`; consider normalizing to `"200:00"`

- **`tot_sFieldGoalsMade`** (*int*): Field goals made, ex: `24`
- **`tot_sFieldGoalsAttempted`** (*int*): Field goals attempted, ex: `68`
- **`tot_sFieldGoalsPercentage`** (*int*): Field goal percentage, ex: `35`

- **`tot_sThreePointersMade`** (*int*): Three-pointers made, ex: `4`
- **`tot_sThreePointersAttempted`** (*int*): Three-pointers attempted, ex: `18`
- **`tot_sThreePointersPercentage`** (*int*): Three-point percentage, ex: `22`

- **`tot_sTwoPointersMade`** (*int*): Two-pointers made, ex: `20`
- **`tot_sTwoPointersAttempted`** (*int*): Two-pointers attempted, e.g., `50`
- **`tot_sTwoPointersPercentage`** (*int*): Two-point percentage, ex: `40`

- **`tot_sFreeThrowsMade`** (*int*): Free throws made, ex: `13`
- **`tot_sFreeThrowsAttempted`** (*int*): Free throws attempted, ex: `17`
- **`tot_sFreeThrowsPercentage`** (*int*): Free throw percentage, ex: `76`

- **`tot_sReboundsDefensive`** (*int*): Defensive rebounds, ex: `25`
- **`tot_sReboundsOffensive`** (*int*): Offensive rebounds, ex: `9`
- **`tot_sReboundsTotal`** (*int*): Total rebounds, ex: `34`

- **`tot_sAssists`** (*int*): Assists, ex: `9`
- **`tot_sTurnovers`** (*int*): Turnovers committed, ex: `20`
- **`tot_sSteals`** (*int*): Steals, ex: `7`

- **`tot_sBlocks`** (*int*): Blocks, ex: `3`
- **`tot_sBlocksReceived`** (*int*): Blocks recieved, e.g., `2`

- **`tot_sFoulsPersonal`** (*int*): Personal fouls committed, ex: `16`
- **`tot_sFoulsOn`** (*int*): Fouls drawn from opponents, ex: `18`
- **`tot_sFoulsTotal`** (*int*): Total fouls, typically equals `tot_sFoulsPersonal`, ex: `18`

- **`tot_sPoints`** (*int*): Points scored, ex: `65`
- **`tot_sPointsFromTurnovers`** (*int*): Points scored off opponent turnovers, ex: `18`
- **`tot_sPointsSecondChance`** (*int*): Second chance points, ex: `8`
- **`tot_sPointsFastBreak`** (*int*): Fast break points, ex: `14`
- **`tot_sBenchPoints`** (*int*): Points scored by bench players, ex: `19`
- **`tot_sPointsInThePaint`** (*int*): Points scored in the paint area, ex: `38`

- **`tot_sTimeLeading`** (*int*): Minutes the team held the lead, ex: `0`
- **`tot_sBiggestLead`** (*int*): Largest lead held by the team, ex: `0`
- **`tot_sBiggestScoringRun`** (*int*): Largest scoring run, ex: `7`
- **`tot_sLeadChanges`** (*int*): Number of lead changes during the game, ex: `0`
- **`tot_sTimesScoresLevel`** (*int*): Number of times the score was tied, ex: `0`

- **`tot_sFoulsTeam`** (*int*): Team (non-personal) fouls, ex: `0`
- **`tot_sReboundsTeam`** (*int*): Team-attributed rebounds, ex: `3`
- **`tot_sReboundsTeamDefensive`** (*int*): Team defensive rebounds, ex: `3`
- **`tot_sReboundsTeamOffensive`** (*int*): Team offensive rebounds, ex: `0`
- **`tot_sTurnoversTeam`** (*int*): Team-attributed turnovers, ex: `2`
  
##### Player Stats

- **`pl`** (*dict*): Maps each player's unique ID to their individual stat dictionary:
  - **`1`** (*dict*): Statistical data for player ID `1` (same structure applies to all other players):
    - **`sMinutes`** (*string*): Minutes played, ex: `"14:40"`
    - **`sFieldGoalsMade`** (*int*): Field goals made, ex: `0`
    - **`sFieldGoalsAttempted`** (*int*): Field goals attempted, ex: `1`
    - **`sFieldGoalsPercentage`** (*int*): Field goal percentage, ex: `0`

    - **`sThreePointersMade`** (*int*): Three-pointers made, ex: `0`
    - **`sThreePointersAttempted`** (*int*): Three-pointers attempted, ex: `0`
    - **`sThreePointersPercentage`** (*int*): Three-point percentage, ex: `0`

    - **`sTwoPointersMade`** (*int*): Two-pointers made, ex: `0`
    - **`sTwoPointersAttempted`** (*int*): Two-pointers attempted, ex: `1`
    - **`sTwoPointersPercentage`** (*int*): Two-point percentage, ex: `0`

    - **`sFreeThrowsMade`** (*int*): Free throws made, ex: `0`
    - **`sFreeThrowsAttempted`** (*int*): Free throws attempted, ex: `0`
    - **`sFreeThrowsPercentage`** (*int*): Free throw percentage, ex: `0`

    - **`sReboundsDefensive`** (*int*): Defensive rebounds, ex: `0`
    - **`sReboundsOffensive`** (*int*): Offensive rebounds, ex: `0`
    - **`sReboundsTotal`** (*int*): Total rebounds, ex: `0`

    - **`sAssists`** (*int*): Assists, ex: `0`
    - **`sTurnovers`** (*int*): Turnovers, ex: `0`
    - **`sSteals`** (*int*): Steals, ex: `0`
    - **`sBlocks`** (*int*): Blocks, ex: `0`
    - **`sBlocksReceived`** (*int*): Blocks received, ex: `0`
    - **`sFoulsPersonal`** (*int*): Personal fouls, ex: `0`
    - **`sFoulsOn`** (*int*): Fouls drawn, ex: `0`

    - **`sPoints`** (*int*): Points scored, ex: `0`
    - **`sPointsSecondChance`** (*int*): Points scored off second-chance opportunities, ex: `0`
    - **`sPointsFastBreak`** (*int*): Points scored off fast-break, ex: `0`
    - **`sPlusMinusPoints`** (*int*): Point differential on court, ex: `-20`
    - **`sPointsInThePaint`** (*int*): Points scored in the paint, ex: `0`

    - **`eff_1`** – **`eff_7`** (*float*): Various efficiency ratings, e.g., `eff_1`: `-1`, `0`: `-0.7`, ..., `eff_7`: `-1`

    - **`firstName`** (*string*): First name, ex: `"Shane"`
    - **`firstNameInitial`** (*string*): First name initial, ex: `"S"`
    - **`familyName`** (*string*): Last name, ex: `"Osayande"`
    - **`familyNameInitial`** (*string*): Last name initial, ex: `"O"`
    - **`internationalFirstName`** (*string*): International first name, ex: `"Shane"`
    - **`internationalFirstNameInitial`** (*string*): International first name initial, ex: `"S"`
    - **`internationalFamilyName`** (*string*): International last name, ex: `"Osayande"`
    - **`internationalFamilyNameInitial`** (*string*): International last name initial, ex: `"O"`
    - **`scoreboardName`** (*string*): Display Name used for scoreboard purposes, ex: `"S. Osayande"`
    - **`active`** (*bool*): Whether the player was active in the game (true: `0`, false: `1`)
    - **`starter`** (*bool*): Whether the player started the game, ex: `1`
    - **`photoT`** (*string*): URL to player photo (T1 size), ex: `https://images.statsengine.playbyplay.api.geniussports.com/70c2dca52a2962186782874cee710b91T1.png`
    - **`photoS`** (*string*): URL to player photo (S1 size), ex: `https://images.statsengine.playbyplay.api.geniussports.com/70c2dca52a2962186782874cee710b91S1.png`
    - **`playingPosition`** (*string*): Playing position, ex: `"F"`
    - **`shirtNumber`** (*int*): Shirt number, ex: `33`
    - **`name`** (*string*): Display name used in game, ex: `"S. Osayande"`

##### Extended Team Stats

- **`tot_eff_1`** – **`tot_eff_7`** (*float*): Sum of player efficiency ratings, e.g., `tot_eff_1`: `50`, `2`: `28.2`, ..., `eff_7`: `50`
- **`p1_score`** (*int*): Points scored in period 1, ex: `18`
- **`p2_score`** (*int*): Points scored in period 2, ex: `16`
- **`p3_score`** (*int*): Points scored in period 3, ex: `10`
- **`p4_score`** (*int*): Points scored in period 4, ex: `21`
- **`fouls`** (*int*): Team fouls, ex: `5`
- **`timeouts`** (*int*): Team timeouts, ex: `0`

##### Shot Chart Data

- **`shot`** (*list*): A list of dictionaries, each representing a shot taken by the team.
  - **`0`** (*dict*): Statistical data for the first shot (same structure applies to all other shots):   
    - **`r`** (*int*): Shot result (made: `1`, missed: `0`)
    - **`x`** (*flaot*): X-coordinate of the shot on the court, ex: `5.960000038147`
    - **`y`** (*float*): Y-coordinate of the shot on the court, ex: `52`
    - **`p`** (*int*): Player id of the shooter, ex: `10`
    - **`pno`** (*int*): Jersey number of the shooter, ex: `10`
    - **`tno`** (*int*): Team id of the shooter, ex: `1`
    - **`per`** (*int*): Period number when the shot was taken, ex: `1`
    - **`perType`** (*string*): Type of period, ex: `"REGULAR"`
    - **`actionType`** (*string*): Shot type, ex: `"2pt"`
    - **`actionNumber`** (*int*): Unique action identifier, ex: `534`
    - **`previousAction`** (*string*): Id of previous action (may be empty), ex: `""`
    - **`subType`** (*string*): Subtype of the shot, ex: `"jumpshot"`
    - **`player`** (*string*): Name of the shooter, ex: `"N. Pierre-Louis"`
    - **`shirtNumber`** (*string*): Jersey number of the shooter (as string), ex: `"1"`
  
##### Scoring Events Timeline

- **`scoring`** (*list*): A list of dictionaries, each representing a scoring event by the team.
  - **`0`** (*dict*): Statistical data for the first scoring event (same structure applies to all other scoring events):
    - **`gt`** (*string*): Clock time when the basket was made, e.g., `"09:11"`
    - **`pno`** (*int*): Jersey number of the player, e.g., `10`
    - **`tno`** (*int*): Team ID of the scoring team, e.g., `1`
    - **`per`** (*int*): Period number, e.g., `1`
    - **`perType`** (*string*): Type of period, e.g., `"REGULAR"`
    - **`player`** (*string*): Display name of the player, e.g., `"N. Pierre-Louis"`
    - **`shirtNumber`** (*string*): Player’s jersey number, ex: `"1"`
    - **`firstName`** (*string*): First name of the player
    - **`familyName`** (*string*): Last name of the player
    - **`internationalFirstName`** (*string*): International first name
    - **`internationalFamilyName`** (*string*): International last name
    - **`firstNameInitial`** (*string*): Initial of the first name
    - **`familyNameInitial`** (*string*): Initial of the last name
    - **`internationalFirstNameInitial`** (*string*): International first name initial
    - **`internationalFamilyNameInitial`** (*string*): International last name initial
    - **`scoreboardName`** (*string*): Name used for scoreboard purposes, ex: `"N. Pierre-Louis"`
  
##### lds (`Logged Detailed Stats`)

> ℹ️ **Note:** Within `lds`, only one player's stats are documented below for the `sBlocks` category. All other stat categories (`sSteals`, `sAssists`, `sReboundsTotal`, `sPoints`) follow the exact same structure.

- **`lds`** (*dict*): Logged detailed stats for specific performance categories such as `sBlocks`, `sSteals`, `sAssists`, `sReboundsTotal`, and `sPoints`. Each key represents a stat category and maps to a dictionary of player-level summaries for that stat.
  - **`sBlocks`** (*dict*): Dictionary of players who recorded at least one block.
    - **`1`** (*dict*): Player ID `1`'s block stats:
      - **`name`** (*string*): Scoreboard display name, ex: `"J. Chaplin"`
      - **`tot`** (*int*): Total count for this stat, ex: `1`
      - **`tno`** (*int*): Team number, ex: `1`
      - **`pno`** (*int*): Player number, ex: `11`
      - **`shirtNumber`** (*string*): Jersey number, ex: `"34"`
      - **`firstName`** (*string*): First name, ex: `"Jamir"`
      - **`familyName`** (*string*): Last name, ex: `"Chaplin"`
      - **`internationalFirstName`** (*string*): International first name, ex: `"Jamir"`
      - **`internationalFamilyName`** (*string*): International last name, ex: `"Chaplin"`
      - **`firstNameInitial`** (*string*): Initial of first name, ex: `"J"`
      - **`familyNameInitial`** (*string*): Initial of last name, ex: `"C"`
      - **`internationalFirstNameInitial`** (*string*): International first name initial, ex: `"J"`
      - **`internationalFamilyNameInitial`** (*string*): International last name initial, ex: `"C"`
      - **`scoreboardName`** (*string*): Display name used on the scoreboard, ex: `"J. Chaplin"`
      - **`photoT`** (*string*): URL to player's photo (thumbnail T1 size), ex: `"https://images.statsengine.playbyplay.api.geniussports.com/072d69731b8ad6f3693c680cb4461d92T1.png"`
      - **`photoS`** (*string*): URL to player's photo (thumbnail S1 size), ex: `"https://images.statsengine.playbyplay.api.geniussports.com/072d69731b8ad6f3693c680cb4461d92S1.png"`

  - **`sSteals`** (*dict*): Same structure as `sBlocks`, but for players who recorded steals.
  - **`sAssists`** (*dict*): Same structure as `sBlocks`, but for players who recorded assists.
  - **`sReboundsTotal`** (*dict*): Same structure as `sBlocks`, but for players who recorded rebounds.
  - **`sPoints`** (*dict*): Same structure as `sBlocks`, but for players who scored points.

### pbp (`Play-by-Play Data`)

> ℹ️ Note: Every event in `pbp` follows one of two formats:
> - Player-involved actions (ex: shots, assists, fouls)
> - Non-player/team-only actions (ex: timeouts, period start/end)

**`pbp`** (*list*): List of play-by-play events recorded during the game. Each item in the list represents a single event.

#### Player Event Format
- **`2`** (*dict*): Event involving a player
  - **`gt`** (*string*): Game time when the event occurred, ex: `"03:18"`
  - **`clock`** (*string*): Clock time when the event occurred, ex: `"03:18: 00"`
  - **`s1`** (*string*): Score of team 1, ex: `"65"`
  - **`s2`** (*string*): Score of team 2, ex: `"105"`
  - **`lead`** (*int*): Score differential from team 1's perspective, ex: `-40`
  - **`tno`** (*int*): Team number involved in the event, ex: `2`
  - **`period`** (*int*): Period number, ex: `4`
  - **`periodType`** (*string*): Type of period, ex: `"REGULAR"`
  - **`pno`** (*int*): Player number involved in the event, ex: `9`
  - **`player`** (*string*): Scoreboard name of the player involved, ex: `"C. Hollis"`
  - **`success`** (*int*): Success of the action, `1` if successful, `0` if not, ex: `1`
  - **`actionType`** (*string*): Action type, ex: `"rebound"`
  - **`actionNumber`** (*int*): Unique action ID, ex: `1123`
  - **`previousAction`** (*string*): ID of the previous action or `""`
  - **`qualifier`** (*list*): Extra tags, ex: `["pointsinthepaint"] or ["fastbreak]` or empty
  - **`subType`** (*string*): Subcategory of the action, ex: `"dunk"` or `""`
  - **`scoring`** (*int*): 1 if scoring occurred, else `0`
  - **`shirtNumber`** (*int*): Player’s jersey number, ex: `0`
  - **`firstName`** (*string*): Player’s first name, ex: `"Curtis"`
  - **`familyName`** (*string*): Player’s last name, ex: `"Hollis"`
  - **`internationalFirstName`** (*string*): International first name, ex: `"Curtis"`
  - **`internationalFamilyName`** (*string*): International last name, ex: `"Hollis"`
  - **`firstNameInitial`** (*string*): First name initial, ex: `"C"`
  - **`familyNameInitial`** (*string*): Last name initial, ex: `"H"`
  - **`internationalFirstNameInitial`** (*string*): International first name initial, ex: `"C"`
  - **`internationalFamilyNameInitial`** (*string*): International last name initial, ex: `"H"`
  - **`scoreboardName`** (*string*): Scoreboard display name, ex: `"C. Hollis"`

#### Non-Player Event Format
- **`0`** (*dict*): Event involving no specific player
  - **`gt`** (*string*): Game time when the event occurred, ex: `"00:00"`
  - **`clock`** (*string*): Clock time when the event occurred, ex: `"00:00: 00"`
  - **`s1`** (*string*): Score of team 1, ex: `"65"`
  - **`s2`** (*string*): Score of team 2, ex: `"105"`
  - **`lead`** (*int*): Score differential from team 1's perspective, ex: `-40`
  - **`tno`** (*int*): Team number involved in the event, ex: `0`
  - **`period`** (*int*): Period number, ex: `4`
  - **`periodType`** (*string*): Type of period, ex: `"REGULAR"`
  - **`pno`** (*int*): Always `0`
  - **`player`** (*string*): Empty string `""`
  - **`success`** (*int*): Usually `1`
  - **`actionType`** (*string*): High-level category, e.g., `"game"`, `"period"`
  - **`actionNumber`** (*int*): Unique identifier for the event
  - **`previousAction`** (*string*): ID of prior event, or empty string
  - **`qualifier`** (*list*): Tags like `["confirmed"]`
  - **`subType`** (*string*): Detail about the action, e.g., `"end"`
  - **`scoring`** (*int*): Always `0`
  - **`shirtNumber`** (*string*): Empty string `""`

### leaddata (`Lead Data`)

**`leaddata`** (*list*): Contains two parallel arrays tracking lead changes throughout the game.
  - **`0`** (*list*): Strings indicating period starts (`"P1"`, `"P2"`, `"P3"`, `"P4"`) with empty strings between them representing time segments.
    - Example: `["", "P1", "", "", ... "", "P2", "", ...]`
  - **`1`** (*list*): Integers representing team 1's lead at each corresponding time segment. Negative values indicate team 2 is leading.
    - Example: `[0, 0, 0, 0, 0, 0, 3, 0, ... -40, -40]`

### Game Metadata

- **`disableMatch`** (*int*): Flag indicating if match is disabled (ex: `0` for active, `1` for disabled)
- **`attendance`** (*int*): Number of attendees at the game, ex: 2328
- **`periodsMax`** (*int*): Maximum number of periods in game (typically 4)
- **`periodLengthREGULAR`** (*int*): Length of regular periods in minutes (10)
- **`periodLengthOVERTIME`** (*int*): Length of overtime periods in minutes (5)
- **`timeline`** (*list*): Empty list (possibly reserved for future timeline data)
- **`totalTimeAdded`** (*int*): Total added time (`0` if none)

### scorers (`Player Scoring Details`)

**`scorers`** (*dict*): Contains scoring data for both teams (keyed by number)
  - **`1`** (*list*): List of scoring players for team 1 (home team)
    - **`0`** (*dict*): First scoring player (same structure applies to all other players):
      - **`tno`** (*int*): Team number
      - **`pno`** (*int*): Player number
      - **`player`** (*string*): Scoreboard name (ex: `"N. Pierre-Louis"`)
      - **`shirtNumber`** (*int*): Jersey number, 
      - **`firstName`** (*string*): Player first name
      - **`familyName`** (*string*): Player last name
      - **`internationalFirstName`** (*string*): International first name
      - **`internationalFamilyName`** (*string*): International last name
      - **`scoreboardName`**: Display name for scoreboard purposes
      - **`times`** (*list*): List of scoring events
        - **`0`** (*dict*): Details of the first scoring event (same structure applies to all other scoring events):
          - **`gt`** (*string*): Game time
          - **`per`** (*int*): Period number
          - **`perType`** (*string*): Period type
          - **`subType`** (*string*): Shot type (ex: "jumpshot")
      - `summary`: Space-separated times of scoring events
  - **`2`** (*list*): Away team scorers (same structure as home team)

### totallds (`Total Logged Detailed Stats`)

**`totallds`** (*dict*): Top performers by category

#### Statistical Categories
- Each category (`sBlocks`, `sSteals`, `sAssists`, `sReboundsTotal`, `sPoints`) (*list*): is a list of the 5 top performers across both teams.
- They are in the same format as the `lds` section, but only include the top 5 players for each stat category.

### officials (`Game Officials`)

**`officials`** (*dict*): Game officials information
  - `referee1`, `referee2`, `referee3` (*dict*): Each contains:
    - **`firstName`** (*string*): Official's first name
    - **`familyName`** (*string*): Last name
    - **`name`** (*string*): Full name
    - **`internationalFirstName`** (*string*): International first name
    - **`internationalFamilyName`** (*string*): International last name
    - **`internationalFirstNameInitial`** (*string*): International first name initial
    - **`internationalFamilyNameInitial`** (*string*): International last name initial
    - **`scoreboardName`** (*string*): Display name for scoreboard purposes (ex: "R. Kerrison")

### othermatches (`Related Matches`)
  
**`othermatches`** (*list*): Empty list (potential placeholder for related matches data)