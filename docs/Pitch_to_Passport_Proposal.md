# Pitch to Passport — A Women's Champions League Talent Map

**Final Project Proposal for** Basics of Software Development Practice SS 2026

**Group:** Max Elixhauser, Emily Panzl | **Repo:** [https://github.com/Secreez/pitch-to-passport](https://github.com/Secreez/pitch-to-passport)

## Description & Overall Goal

Pitch to Passport is an interactive CLI tool to analyze and map the geographical origins and migratory flows of football talent in the 2025–26 UEFA Women's Champions League (UWCL). It combines text-based data exploration in the terminal with HTML maps generated on demand via `folium`.

**Goal:** Pitch to Passport bridges raw sports statistics and spatial analytics, turning tabular football data into a macro-level visualization of talent migration trends in the 2025–26 UWCL. Instead of just numbers on a spreadsheet, the software should let users answer broader questions:

- Where does winning talent come from geographically?
- Which clubs attract the most international players?
- Which countries export talent without having a club in the competition?

### Core Features (MVP)

- **`player <name>`:** Full name, age, nationality, current/former club, squad number, positions
- **`team <name>`:** Squad size, avg age, nationalities, goals/assists, home stadium
- **`compare <player1> <player2>`:** Side-by-side player stats (goals, assists, club, etc.)
- **`compare <team1> <team2>`:** Side-by-side squad stats (size, goals, assists, top scorer, age, diversity)
- **`map <team>`:** Map linking each player’s home country to the club, with stat popups
- **`map all`:** Global talent migration map across all 18 UWCL clubs

### Nice to Have / Stretch Goals

- **`map <player>`:** single-line map for one player's journey. Low visual value vs. team/global maps, easy to cut.
- **CL trophies & market value in `compare <team1> <team2>`:** needs extra data sourcing (ESPN/Transfermarkt) and merging; added only if time allows.

## Feasibility & Known Risks

- Data is manually sourced from FBref rather than scraped — a conscious tradeoff for realistic scope and to avoid bot-protection issues.
- Some players appear twice due to mid-season transfers — a known data quirk handled during cleaning.
- Player name matching is case-insensitive but requires exact spelling; partial search is nice-to-have, **not guaranteed in the MVP.**
- Generated maps are HTML files opened in the default browser — assumes one is available.

## Approach & Milestones

- **Object-oriented:** CLI built on `cmd.Cmd`, inherited and extended with custom commands (`do_player`, `do_team`, etc.)
- **Procedural:** data cleaning/transformation in `format.py` via single-purpose functions
- **External packages:** `pandas` (data handling), `folium` (maps), `argparse`/`cmd` (CLI)

**Language:** Python 3.x | **Version control:** Git / GitHub

**Milestones:**

1. **Proposal & Planning:** define scope, feature triage, repo structure, data sourcing *in progress*
2. **Data Foundation:** `format.py` complete, clean CSV ready, duplicates handled
3. **CLI Core:** `player`, `team`, `compare` commands working with proper edge case handling
4. **Spatial Layer:** `map <team>` and `map all` generating correct folium HTML maps
5. **Testing & Polish:** edge cases tested, documentation finalised, repo clean
6. **Submission:** final code pushed, individual reflections written separately


## Learning Goals

- **(Max) CLI edge case thinking:** I felt a spark of joy when we first touched argparse in class. Building itself isn't really the why but it's thinking through the edge cases for an MVP: what happens on unexpected input, where does scope realistically stop, how does a stakeholder think.
- **(Emily) Creating an interactive webmap (with Folium):** So, I have never used Folium before and am interested to learn how to create interactive webmaps with Python since it is a much more interesting way to explore data. 

## Responsibilities

- **Max:** Data cleaning & formatting (`format.py`), CLI architecture & commands (`main.py`), repo structure & documentation
- **Emily:** Data analysis, validation & duplicate handling, football domain expertise & stat interpretation, spatial map design & folium implementation
- **Both:** Country centroid/geocoordinate research, proposal, individual reflections

## Effort Estimate and Deadline

**Submission deadline:** August 15th, 2026

- **Time:** 25h per person (50h total): Proposal & planning ~3h each | Data cleaning & ad-hoc pivots ~3h (Max) | CLI & repo structure ~14h (Max) | Data analysis & map design ~17h (Emily) | Testing & polish ~3h each | Individual reflection ~2h each
- **Tools:** Python, GitHub, Git, VS Code | **Communication:** WhatsApp
- **Data sources:** FBref (player stats, manually exported) | Google Maps (stadium coordinates) | OpenStreetMap via folium (base tiles) | *Stretch goal: ESPN for CL trophies & market value*