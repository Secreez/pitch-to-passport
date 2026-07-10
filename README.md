# Pitch to Passport

A CLI tool that maps where Women's Champions League talent comes from and where it lands.

Built for the course "Basics of Software Development Practice" for our Final Project.

**Authors:** Emily Panzl & Max Elixhauser

## Concept

...

We draw lines from each player's home country to their club location, therefore revealing the global flow of women's football talent across Europe.

## Data

Data is sourced from [FBref](https://fbref.com/en/comps/181/stats/Champions-League-Stats) 
(2025-26 UEFA Women's Champions League, knockout stage clubs only).

Due to FBref's TOS, raw data files are not included in this repository.

**Two-step data pipeline:**

1. **Base cleaning** (`format.py`): copies raw FBref stats into a clean CSV (401 players, 18 clubs)
2. **Manual enrichment** (Emily): manually validated and enriched with `ShirtNumber`, `FormerClub`, 
   and `Awards` columns, scoped to 12 knockout stage clubs (275 players)

**To reproduce:**
1. Go to the FBref link above, copy the Player Standard Stats table
2. Save as `data/players.txt` (UTF-8 encoded)
3. Run `python format.py` → generates `data/players.csv`
4. Apply manual enrichment

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --config data/players.csv
```

### Commands [To be determined]

| Command | Description |
|---|---|
| `player <name>` | Show stats for a specific player |
| `team <name>` | Show squad nationality breakdown and top scorers |
| `compare <team1> <team2>` | Side-by-side team comparison |
| `map <team>` | Generate folium map for a club |
| `map all` | Generate full global talent flow map |
| `exit` | Exit the program |


## Project Structure

```
pitch-to-passport/
├── data/
│   ├── players.txt # Raw FBref copy-paste (not in repo)
│   └── players.csv # Cleaned data (not in repo)
├── docs/           # public deliverable
└── proposal.md     # the actual deliverable
└── time.md         # time tracking
├── format.py       # Data cleaning script
├── main.py         # CLI entry point
├── [placeholder]
├── README.md
└── .gitignore
```

## Who does what - Division

**Emily:**
- Data analysis & validation
- Football domain expertise
- Map design (folium)

**Max:**
- Data cleaning (format.py)
- CLI logic (main.py)
- Repo structure & documentation

**Both:**
- Proposal
- Individual reflection (mandatory after project)

## License

Code: MIT
Data: sourced from FBref - not redistributed
