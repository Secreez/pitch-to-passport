# Pitch to Passport — Submission

**Repo:** https://github.com/Secreez/pitch-to-passport

## How to run

1. Clone the repo or download the files
2. Place `players_enriched.csv` into the `data/` folder
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

## Note on data pipeline

`format.py` produces a base cleaned CSV from raw FBref data. While the raw data file itself is not included in the repository, `format.py` is provided so you can see how the raw data is initially parsed and cleaned. 

A key project limitation was that our goals required deeper data not available in standard scrapes. To solve this, the final dataset (`players_enriched.csv`) was manually validated and enriched by Emily — please place it in the `data/` folder as instructed above.

Full documentation: see `README.md` in the repo.