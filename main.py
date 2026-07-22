# CLI Struc

# Standard library
import argparse
import cmd
import unicodedata

# External library
import pandas as pd


def normalize_text(text):
    """Converts 'Bøe' or 'Xènia' to 'boe' or 'xenia' for easy matching."""
    nfkd = unicodedata.normalize('NFKD', str(text))
    # In this case, strips out accent marks and converts to lower case
    return "".join([_ for _ in nfkd if not unicodedata.combining(_)]).lower()

class PitchToPassport(cmd.Cmd):
    prompt = "PitchToPassport> "
    intro = "Welcome to Pitch to Passport! Type 'help' for commands. Use 'exit' to get out of the program."
    
    def __init__(self, df):
        super().__init__() # inherit everything from cmd basically.
        self.df = df # load df

        # normalized names once at startup for accent searches
        self.df["_NormalizedPlayer"] = self.df["Player"].fillna("").apply(normalize_text)

# This is basically csv search with name
# might optimize that one later on as it is a bit stretchy..
# But so far super happy as player xenia works now to find -> Xènia Pérez for example.
    def do_player(self, line):
        # shall be:
        # case insensitive 
        # Chck if the input a in the player oclumn not just exact
        # if multiple results -> show all mathces so the user can be more specific 
        # If zero results -> helpful not found message 
        """Look up a player via: player <name>"""

        # Clean up user input
        # basically: empty handling so prevents erros fi the user just types player with no argument
        query = line.strip()

        if not query:
            print("Please enter a player name to search. Such as: player Mead")
            return

        clean_query = normalize_text(query)

        # Now Case-insensitive search using .str.contains()
        # regex=False prevents crashes from symbols such as ? , etc.
        matches = self.df[self.df["_NormalizedPlayer"].str.contains(clean_query, regex=False)]
        
        # Handling zero results
        if matches.empty:
            print(f"No players found matching {query}. Try a different spelling or single name")
            return
        
        # Display
        print(f"\nFound {len(matches)} match for {query}:")
        print("----------------------------------------------------------------------------------")

        for _, row in matches.iterrows():
            print(
                f"- {row['Player']} | Position: {row['Pos']} | "
                f"Club: {row['ClubName']} ({row['ClubCountry']}) | Shirt #{row['ShirtNumber']}"
                )

        print("----------------------------------------------------------------------------------")

# do_team
# that one is basically the same as do_player mechanical wise: filtering self.df by ClubName with agg: mean(), nunique() .sum ..
# then print formatted overview basically. Should be .. faster then te do_player .. but will see heh! :D
    def do_team(self, _):
      pass


# do_compare
    def do_compare(self, _):
      pass


# do_map
# Atleast cuz need folium struc first from Emily 
    def do_map(self):
      pass


# do_exit
    def do_exit(self, _):
      "Exit the program"
      return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser() # load class parser
    parser.add_argument("--config", type=str, default="data/players_enriched.csv") # adding the argument for configuration and a defualt read
    args = parser.parse_args() #  get config path 
    df = pd.read_csv(args.config, encoding="utf-8") # loading the csv if different csv (default utf-8)
    PitchToPassport(df).cmdloop() # start interactive cli