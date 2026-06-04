# Final Project Proposal - Group: Pitch to Passport

---

> **NOTE FOR US**
>
> Martin's key points for the proposal:
> - Practice a structured approach to software development
> - Evaluate **feasibility before starting to program**
> - The **process is more important than the outcome** -> be realistic and convincing
> - An **individual reflection after group submission is mandatory** (submitted separately, not in this document)
> - 1-2 pages maximum
> (See Blackboard for more info under: Final Project Proposal)

---

**Course:** Basics of Software Development Practice SS 2026
**Department:** Z_GIS, University of Salzburg

**Group Members:**
- Max Elixhauser
- Emily Panzl

## Project Title

Pitch to Passport — A Women's Champions League Talent Map (? Map.. well its both CLI and Map)

## Description

> *Martin: Description of what you want to (try to) do*

Pitch to Passport is an interactive Command Line Interface (CLI) tool designed to analyze and map the geographical origins and migratory flows of football talent in the 2025–26 UEFA Women's Champions League (UWCL).

The software shall utilize a dual-layered approach to user interaction: immediate text-based data exploration within the terminal, and dynamic HTML spatial visualizations generated on demand based on feature.

> **@Emily I whould write that actually quite User driven.. -> Lets be explicit here and Feature enables User to .. as -> WHAT and the HOW -> is the Description.**

1. CLI-Only Features (Text-Based Data Analysis)

These features focus on fast, tabular data querying, filtering, and aggregation directly inside the terminal environment:

- Player Profile Exploration (`player <name>`): Enters a specific player's name .. 

- Squad Metrics .... Breakdown: (`team <name>`): Queries a specific club to calculate aggregate squad metrics. It shall provide .. 

- Side-by-Side Comparison (`compare <team1> <team2>): Allows users to input two clubs ...

...

2. CLI + Map Output Features (Geospatial Visualization)

These commands trigger the spatial data ... `folium`

- Club Talent Pipeline Map (`map <team>`):

- Global Flow Map (`map all`)

...


---
| Command | Description |
|---|---|
| `player <name>` | Show stats for a specific player |
| `team <name>` | Show squad nationality breakdown and top scorers |
| `compare <team1> <team2>` | Side-by-side team comparison |
| `map <team>` | Generate folium map for a club |
| `map all` | Generate full global talent flow map |
| `exit` | Exit the program |
--- (just added that as a reminder for me xD - @Emily, feel free to add your commands in here that you want and are feasible ofc.)

Link to our Repo: https://github.com/Secreez/pitch-to-passport

### Overall Goal

> *Martin: the overall goal of your project (what should the software do)?*

**! The Overall Goal is the WHY and the BIG PICTURE ! Ergo: Why shit Matters .. higher-level insights .. core thesis of our tool - Something like ...:**

The primary objective of Pitch to Passport is to bridge the gap between simple ass sports stats and spatial analytics, transofmring raw tabular football data into a macro-level vizualization snapshot of migrations trends within the UEFA in .. 


So, instead of just looking at numbers on a spreadsheet, the software should enable the user to answer broader questions about the sport:



### Feasibility & Known Risks

> **@Emily I suggest putting feasibility/risks here as its own subsection? Is always cool to have and more honest. Even if he didn't asked for it explicitly.**

- The data is manually sourced from FBref rather than scraped, which is a conscious tradeoff to keep the scope realistic and avoid bot-protection issues.
- Emily: Some players appear twice in the dataset due to mid-season club transfers. This is a known data quirk that will be documented and handled in the cleaning step.
- **@Emily ... add any other data discrepancies you found here so far**

### Programming Paradigm & Approach

> *Martin: The programming paradigm and approach (object-oriented, procedural, external packages, ...)*

In our case, the project uses a mixed paradigm:

- **Object-oriented:** as the CLI is built on `cmd.Cmd`, a Python base class that is inherited and extended with custom commands (`do_player`, `do_team` etc.)

- **Procedural:** data cleaning and transformation in `format.py` follows a procedural approach with single-purpose functions

- **External packages:** `pandas` for data handling, `folium` for spatial  map generation, `argparse` and `cmd` for the CLI interface

**Language:** Python 3.x
**Version control:** Git / GitHub

### Milestones & Intermediate Steps

> *Martin: Intermediate steps and milestones*

1. ...
2. ...
3. ...
4. ...

## Learning Goals

> *Martin: your goals of what each of you wants to learn more about*

**Max:**

**Data Cleaning with pandas:** Well, I know R/tidyverse cold (dplyr is my comfort zone), but the "way of the pandas" — if you will — is genuinely new territory for me. Even after years of dragging Python along through my Bachelor's, I never properly sat down with it. And although, let's be honest, the hour investment won't be huge here, it still has meaning.

**CLI edge case thinking:** I genuinely felt a spark of joy when we first touched argparse in class, weirdly enough. What excites me more than just building things (as in most cases I really don't care about building) is: did I actually think through the most important edge cases for an MVP? What happens when the user types something unexpected? Where does the scope realistically stop? How does a stakeholder think? That's the part I want to nail — more of a... "semantic product thinking exercise within the gamification of a CLI". One more thing. But there ain't no one more thing.

**Emily:**

...

## Responsibilities

> *Martin: Include who in the group is responsible for what*

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

> *Martin: When you plan to have it done: set your own deadline -> any time from July until end of August*

**Submission deadline: ...**

- **@Emily - .. August somethingsomething?**

## Effort Estimate

> *Martin: How much effort and resources will be required*

- **Time:** ~25 hours per person (~50 hours total)
    - Proposal & planning: ~3h each

    - Data cleaning & ad-hoc pivots mid-project: ~5.5h (Max)  
    - CLI & repo structure: ~11.5h (Max)

    - Data analysis & map design: ~13h (Emily)

    - Testing & polish: ~3h each
    - Individual reflection: ~2h each

- **Data:** Manually sourced from FBref (401 players, 2025-26 Women's CL season)
- **Tools:** Python, GitHub, Git (VSC), IDE: VS Code (Emily) / Positron (Max), WhatsApp (lol)
- **@Emily - anything to add here?**