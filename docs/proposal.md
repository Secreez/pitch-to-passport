# Final Project Proposal - Group: Pitch to Passport

**Course:** Basics of Software Development Practice SS 2026
**Department:** Z_GIS, University of Salzburg

**Group Members:**
- Max Elixhauser
- Emily Panzl

## Project Title

Pitch to Passport — A Women's Champions League Talent Map

## Description

Pitch to Passport is an interactive Command Line Interface (CLI) tool designed to analyze and map the geographical origins and migratory flows of football talent in the 2025–26 UEFA Women's Champions League (UWCL).

The software shall utilize a dual-layered approach to user interaction: immediate text-based data exploration within the terminal, and dynamic HTML spatial visualizations generated on demand based on feature.

1. CLI-Only Features (Text-Based Data Analysis)

These features focus on fast, tabular data querying, filtering, and aggregation directly inside the terminal environment:

- Player Profile Exploration (`player <name>`): Enters a specific player's name and gives information about full name, birthday/age, nationality, current club, former club if they signed with another during the season, number, positions played. 

- Squad Metrics .... Breakdown: (`team <name>`): Queries a specific club to calculate aggregate squad metrics. It shall provide squad size, average age, number of different nationalities, goals and assists, home stadium.

- Side-by-Side Comparison (`compare <player1> <player2>`): Allows users to input two players and compare their stats (goals, assists, club, ...).

- Side-by-Side Comparison (`compare <team1> <team2>`): Allows users to input two clubs and compare their squad depth, market value, games played overall in the league, goals, assists, top scorer, age, nationality diversity, champions league trophies.

2. CLI + Map Output Features (Geospatial Visualization)

These commands trigger the spatial data and generate interactive maps using `folium` that can be viewed in a web browser.

- Club Talent Pipeline Map (`map <team>`):

This feature enables users to see where a club's players originate from geographically. The command generates an HTML map that links a player's home country with the club they're currently playing at. It will also show the most important facts about the player through a popup.

- Global Flow Map (`map all`)

This feature enables users to explore talent migration patterns across all featured clubs in the Women's Champions League. Users get to see which countries are talent-exporting and talent-importing countries.

Link to our Repo: https://github.com/Secreez/pitch-to-passport

### Overall Goal

The primary objective of Pitch to Passport is to bridge the gap between raw sports statistics and spatial analytics, transforming tabular football data into a macro-level visualization of talent migration trends across the 2025–26 UEFA Women's Champions League.

So, instead of just looking at numbers on a spreadsheet, the software should enable the user to answer broader questions about the sport:

- Where does winning talent come from geographically?
- Which clubs attract the most international players?
- Which countries export talent without having a club in the competition?

### Feasibility & Known Risks

- The data is manually sourced from FBref rather than scraped, which is a 
  conscious tradeoff to keep the scope realistic and avoid bot-protection issues.
- Across different platforms, the data can sometimes vary, so it is sometimes
  unclear which data is correct.  
- Some players appear twice in the dataset due to mid-season club transfers.
  This is a known data quirk that will be documented and handled in the cleaning step.
- Player name matching is case-insensitive but requires exact spelling — 
  partial name search is a nice-to-have, not guaranteed in the MVP.
- Generated maps are HTML files opened in the default browser — assumes a 
  browser is available on the user's machine.
  

### Programming Paradigm & Approach

In our case, the project uses a mixed paradigm:

- **Object-oriented:** as the CLI is built on `cmd.Cmd`, a Python base class that is inherited and extended with custom commands (`do_player`, `do_team` etc.)

- **Procedural:** data cleaning and transformation in `format.py` follows a procedural approach with single-purpose functions

- **External packages:** `pandas` for data handling, `folium` for spatial  map generation, `argparse` and `cmd` for the CLI interface

**Language:** Python 3.x
**Version control:** Git / GitHub

### Milestones & Intermediate Steps

1. **Proposal & Planning:** define scope, feature triage, repo structure, data sourcing *in progress*
2. **Data Foundation:** `format.py` complete, clean CSV ready, duplicates handled
3. **CLI Core:** `player`, `team`, `compare` commands working with proper edge case handling
4. **Spatial Layer:** `map <team>` and `map all` generating correct folium HTML maps
5. **Testing & Polish:** edge cases tested, documentation finalised, repo clean
6. **Submission:** final code pushed, individual reflections written separately


## Learning Goals

**Max:**

**CLI edge case thinking:** I genuinely felt a spark of joy when we first touched argparse in class, weirdly enough. What excites me more than just building things (as in most cases I really don't care about building) is: did I actually think through the most important edge cases for an MVP? What happens when the user types something unexpected? Where does the scope realistically stop? How does a stakeholder think? That's the part I want to nail — more of a... "semantic product thinking exercise within the gamification of a CLI". Now those are words.

**Emily:**

**Creating an interactive webmap (with Folium):** So, I have never used Folium before and am interested to learn how to create interactive webmaps with Python since it is a much more interesting way to explore data. 

## Responsibilities

| Task | Responsible |
|------|-------------|
| Data cleaning & formatting (`format.py`)| Max |
| CLI architecture & commands (`main.py`) | Max |
| Repo structure, README & documentation | Max |
| Data analysis, validation & duplicate handling | Emily |
| Football domain expertise & stat interpretation | Emily |
| Spatial map design & folium implementation | Emily |
| Country centroid lookup & geocoordinate research | Both |
| Proposal | Both |
| Reflection | Both (on our own) |

## Deadline

- **Submission deadline: August 15th, 2026**

## Effort Estimate

- **Time:** 25 hours per person (50 hours total)
    - **Proposal & planning:** ~3h each
    - **Data cleaning & ad-hoc pivots mid-project:** ~5.5h (Max)
    - **CLI & repo structure:** ~11.5h (Max)
    - **Data analysis & map design:** ~13h (Emily)
    - **Testing & polish:** ~3h each
    - **Individual reflection:** ~2h each

- **Tools:** Python, GitHub, Git, IDE: VS Code
- **Data sources:**
    - **FBref (fbref.com), ESPN:** player stats, manually exported
    - **Google Maps:** stadium coordinate verification
    - **OpenStreetMap (via folium):** base map tiles
- **Communication:** WhatsApp 