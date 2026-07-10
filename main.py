# CLI Struc

# Standard library
import argparse
import cmd

# External library
import pandas as pd


class PitchToPassport(cmd.Cmd):
    prompt = "PitchToPassport> "
    intro = "Welcome to Pitch to Passport! Type 'help' for commands."
    
    def __init__(self, df):
        super().__init__() # inherit everything from cmd basically.
        self.df = df # load df 


# do_player
# This is basically csv search with name
    def do_player(self, line):
        "Look up a player via: player <name>"
        pass

# do_team
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
    def do_exit(self, _): # _ = filler..
      "Exit the program"
      return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser() # load class parser
    parser.add_argument("--config", type=str, default="data/players_enriched.csv") # adding the argument for configuration and a defualt read
    args = parser.parse_args() #  get config path 
    df = pd.read_csv(args.config, encoding="utf-8") # loading the csv if different csv 
    PitchToPassport(df).cmdloop() # start interactive cli