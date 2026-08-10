###
#
# Pitch to Passport - Women's Champions League Talent Map
# Cleans raw FBref player stats into a usable CSV (all 18 clubs, 401 players).
#
# NOTE: This script produces the base dataset only. The final enriched dataset
# (12 knockout stage clubs, 275 players) was manually validated by Emily
#
# Data source: https://fbref.com/en/comps/181/stats/Champions-League-Stats#all_stats_standard
# Usage: python format.py
#
###

import pandas as pd
import sys
import os
import unicodedata

INPUT_FILE = "data/players.txt"
OUTPUT_FILE = "data/players.csv"

if not os.path.exists(INPUT_FILE):
    print(f"Error: {INPUT_FILE} not found. Copy the FBref player table and save it there.")
    sys.exit(1)

print(f"Reading {INPUT_FILE}...")

df = pd.read_csv(INPUT_FILE, sep="\t", encoding="utf-8")
df.columns = df.columns.str.strip()

df = df[pd.to_numeric(df["Rk"], errors="coerce").notnull()]

obj_cols = df.select_dtypes(include="str").columns
df[obj_cols] = df[obj_cols].apply(lambda col: col.str.strip())

df["NationCode"] = df["Nation"].str.split().str[-1]
df["ClubName"] = df["Squad"].str.split(" ", n=1).str[-1]

# Manual club coordinates searched and verified via Google Maps
CLUB_COORDS = {
    "Arsenal":          {"country": "England",     "lat": 51.5550, "lon": -0.1084},
    "Chelsea":          {"country": "England",     "lat": 51.4817, "lon": -0.1909},
    "Manchester Utd":   {"country": "England",     "lat": 53.4630, "lon": -2.2914},
    "Barcelona":        {"country": "Spain",       "lat": 41.3809, "lon":  2.1228},
    "Real Madrid":      {"country": "Spain",       "lat": 40.4531, "lon": -3.6882},
    "Atletico Madrid":  {"country": "Spain",       "lat": 40.4363, "lon": -3.5995},
    "Lyon":             {"country": "France",      "lat": 45.7652, "lon":  4.9820},
    "Paris FC":         {"country": "France",      "lat": 48.8433, "lon":  2.2529},
    "Paris S-G":        {"country": "France",      "lat": 48.8414, "lon":  2.2530},
    "Bayern Munich":    {"country": "Germany",     "lat": 48.2188, "lon": 11.6248},
    "Wolfsburg":        {"country": "Germany",     "lat": 52.4327, "lon": 10.8040},
    "Juventus":         {"country": "Italy",       "lat": 45.1096, "lon":  7.6413},
    "AS Roma":          {"country": "Italy",       "lat": 41.9339, "lon": 12.4548},
    "Twente":           {"country": "Netherlands", "lat": 52.2366, "lon":  6.8378},
    "OH Leuven":        {"country": "Belgium",     "lat": 50.8683, "lon":  4.6944},
    "SL Benfica":       {"country": "Portugal",    "lat": 38.7526, "lon": -9.1846},
    "Valerenga":        {"country": "Norway",      "lat": 59.9178, "lon": 10.8067},
    "St. Polten":       {"country": "Austria",     "lat": 48.2209, "lon": 15.6535},
}

def normalize(text):
    # Max AI Assistance Note (Claude): Consulted on using 
    # unicodedata.normalize("NFD", text) combined with category "Mn" 
    # to efficiently strip accents and special characters for robust dictionary lookups.

    """Strips accents/special characters for dictionary lookup via the unicodedata library
    e.g. 'Vålerenga' -> 'Valerenga', 'St. Pölten' -> 'St. Polten'
    """
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )

def get_club_field(club, field):
    """Looks up a club field from CLUB_COORDS, normalizing special characters first."""
    return CLUB_COORDS.get(normalize(club), {}).get(field)

df["ClubCountry"] = df["ClubName"].apply(lambda x: get_club_field(x, "country") or "Unknown")
df["ClubLat"] = df["ClubName"].apply(lambda x: get_club_field(x, "lat"))
df["ClubLon"] = df["ClubName"].apply(lambda x: get_club_field(x, "lon"))

# Drop the Matches column (just a link placeholder from FBref really)
if "Matches" in df.columns:
    df = df.drop(columns=["Matches"])

df = df.reset_index(drop=True)

missing = df[df["ClubCountry"] == "Unknown"]["ClubName"].unique()
nan_counts = df[["NationCode", "ClubName", "ClubLat", "ClubLon"]].isnull().sum()

print("\n--- Pitch to Passport: Data Cleaning Summary ---")
print(f"------------------------------------------------\n")
print(f"Players loaded: {len(df)}")
print(f"Unique clubs: {df['ClubName'].nunique()}")
print(f"Unique nations: {df['NationCode'].nunique()}")
if len(missing) > 0:
    print(f"WARNING - Clubs not found in CLUB_COORDS: {missing}")
else:
    print(f"Club lookup: All clubs matched successfully")
if nan_counts.sum() > 0:
    print(f"WARNING - NaN values found:\n{nan_counts[nan_counts > 0]}")
else:
    print(f"NaN check: No missing values in key columns\n")
print(f"------------------------------------------------")

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
print(f"Saved to {OUTPUT_FILE}")