###
#
# Pitch to Passport - Women's Champions League Talent Map
# Cleans raw FBref player stats into a usable CSV.
#
# Data source: https://fbref.com/en/comps/181/stats/Champions-League-Stats#all_stats_standard
# Usage: ...
#
###

import pandas as pd
import sys
import os
 
INPUT_FILE = "data/players.txt"
OUTPUT_FILE = "data/players.csv"
 
if not os.path.exists(INPUT_FILE):
    print(f"Error: {INPUT_FILE} not found. Copy the FBref player table and save it there.")
    sys.exit(1) # 1 = error
 
print(f"Reading {INPUT_FILE}...")
 
df = pd.read_csv(INPUT_FILE, sep="\t", encoding="utf-8")
df.columns = df.columns.str.strip() # strips the column names itself: "Player " -> "Player"


df = df[df["Rk"].apply(lambda x: str(x).strip().isdigit())] # removes where 'string : RK' row is not a number
for col in df.select_dtypes(include="object").columns: # select only string colums then strip whitespace from each
    df[col] = df[col].str.strip()



# Extract nationality and club name from FBref's prefixed format
# TODO


############# I'll keep it frozen for now until the Proposal is delivered! 


# Club coordinates 'verified via Google Maps' will be pretty handy for the map.

CLUB_COORDS = {
    "Arsenal":         {"country": "England",     "lat": 51.5550, "lon": -0.1084},
    "Chelsea":         {"country": "England",     "lat": 51.4817, "lon": -0.1909},
    "Manchester Utd":  {"country": "England",     "lat": 53.4630, "lon": -2.2914},
    "Barcelona":       {"country": "Spain",       "lat": 41.3809, "lon":  2.1228},
    "Real Madrid":     {"country": "Spain",       "lat": 40.4531, "lon": -3.6882},
    "Atletico Madrid": {"country": "Spain",       "lat": 40.4363, "lon": -3.5995},
    "Lyon":            {"country": "France",      "lat": 45.7652, "lon":  4.9820},
    "Paris FC":        {"country": "France",      "lat": 48.8433, "lon":  2.2529},
    "Paris S-G":       {"country": "France",      "lat": 48.8414, "lon":  2.2530},
    "Bayern Munich":   {"country": "Germany",     "lat": 48.2188, "lon": 11.6248},
    "Wolfsburg":       {"country": "Germany",     "lat": 52.4327, "lon": 10.8040},
    "Juventus":        {"country": "Italy",       "lat": 45.1096, "lon":  7.6413},
    "AS Roma":         {"country": "Italy",       "lat": 41.9339, "lon": 12.4548},
    "Twente":          {"country": "Netherlands", "lat": 52.2366, "lon":  6.8378},
    "OH Leuven":       {"country": "Belgium",     "lat": 50.8683, "lon":  4.6944},
    "SL Benfica":      {"country": "Portugal",    "lat": 38.7526, "lon": -9.1846},
    "Valerenga":       {"country": "Norway",      "lat": 59.9178, "lon": 10.8067},
    "St. Polten":      {"country": "Austria",     "lat": 48.2209, "lon": 15.6535},
}

# df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

def get_club_field(club, field):
    return CLUB_COORDS.get(club, {}).get(field)

# LOGIC apply into ClubName for ClubCountry, ClubLat, ClubLon
# TODO

# Afterwards: Logic Checks
# TODO

# User Friendly Output
# TODO

############# I'll keep it frozen for now until the Proposal is delivered! 
############# I'll keep it frozen for now until the Proposal is delivered! 
############# I'll keep it frozen for now until the Proposal is delivered! 
