# Pitch to Passport

A CLI tool that maps where Women's Champions League talent comes from and where it lands.

Built for the course "Basics of Software Development Practice" — Final Project SS 2026  
**Authors:** Emily Panzl & Max Elixhauser · **Repo:** https://github.com/Secreez/pitch-to-passport

## Concept

275 players. 12 clubs. 30+ nations. One map.

Pitch to Passport bridges raw sports statistics and spatial analytics, turning tabular football data into a macro-level visualization of talent migration trends in the 2025–26 UEFA Women's Champions League. Instead of just numbers on a spreadsheet, the tool lets you answer broader questions:

- Where does winning talent come from geographically?
- Which clubs attract the most international players?
- Which countries export talent without having a club in the competition?

## Data

Data is sourced from [FBref](https://fbref.com/en/comps/181/stats/Champions-League-Stats)  
(2025–26 UEFA Women's Champions League, knockout stage clubs only — 12 clubs, 275 players).

Due to FBref's TOS, raw data files are not included in this repository.

**Two-step data pipeline:**

1. **Base cleaning** (`format.py`) — copies raw FBref stats into a clean CSV (401 players, 18 clubs)
2. **Manual enrichment** (Emily) — validated and enriched with `ShirtNumber`, `FormerClub` and `Awards` columns, scoped to 12 knockout stage clubs (275 players)

**To reproduce:**
1. Go to the FBref link above and copy the Player Standard Stats table
2. Save as `data/players.txt` (UTF-8 encoded)
3. Run `python format.py` → generates `data/players.csv`
4. Apply manual enrichment or contact the authors

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --config data/players_enriched.csv
```

### Commands

| Command | Description |
|---|---|
| `player <name>` | Look up a player by name (partial, accent-insensitive) |
| `team <name>` | Show squad overview and stats for a club |
| `compare <x1> vs <x2>` | Side-by-side comparison of two players or two clubs |
| `map <team>` | Generate folium map — player origins to club location |
| `map all` | Global talent migration map across all knockout clubs |
| `exit` | Exit the program |

**Examples:**

```
player Russo
player Xènia (player can also be called via.: Xenia)
team Arsenal
team madrid
compare Arsenal vs Barcelona
compare Alessia Russo vs Pernille Harder
```

## Project Structure

```
pitch-to-passport/
├── data/
│   ├── players.txt          # Raw FBref copy-paste (not in repo)
│   ├── players.csv          # Base cleaned data (not in repo)
│   └── players_enriched.csv # Manually enriched dataset (not in repo)
├── docs/
│   ├── proposal.md          # Final project proposal
│   └── time.md              # Time tracking
├── format.py                # Data cleaning script (step 1)
├── main.py                  # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore
```

## Who Does What

**Max:** Data cleaning (`format.py`), CLI architecture (`main.py`), repo structure & documentation  
**Emily:** Data analysis & validation, football domain expertise, map design (folium)  
**Both:** Proposal, individual reflections

## License

Code: MIT  
Data: sourced from FBref — not redistributed
