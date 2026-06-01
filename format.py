###
# Pitch to Passport - A Women's Champions League Talent Map
# Cleans raw FBref player stats into a usable CSV.
#
# Data source: https://fbref.com/en/comps/181/stats/Champions-League-Stats#all_stats_standard
# Usage: ...
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
df.columns = df.columns.str.strip()