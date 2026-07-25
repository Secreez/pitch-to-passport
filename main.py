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
        self.df["_NormalizedClub"] = self.df["ClubName"].fillna("").apply(normalize_text)


    def _find_club(self, query): # helper func to not dublicate stuff along the way
        clean_query = normalize_text(query)
        matches = self.df[self.df["_NormalizedClub"].str.contains(clean_query, regex=False)]
        if matches.empty:
            return None
        return matches
    
    def _find_player(self, query):
        clean_query = normalize_text(query)
        matches = self.df[self.df["_NormalizedPlayer"].str.contains(clean_query, regex=False)]
        if matches.empty:
            return None
        return matches

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
        match_word = "match" if len(matches) == 1 else "matches"
        print(f"\nFound {len(matches)} {match_word} for '{query}':")
        print(f"{"=" * 90}")
        for _, row in matches.iterrows():
            print(
                f"- {row['Player']:<20} | #{row['ShirtNumber']:<3} | "
                f"Pos: {row['Pos']:<6} | Club: {row['ClubName']} ({row['ClubCountry']})"
                )
        print(f"{"=" * 90}\n")

# do_team
# that one is basically the same as do_player mechanical wise: filtering self.df by ClubName with agg: mean(), nunique() .sum ..
# then print formatted overview basically. Should be .. faster then te do_player .. but will see heh! :D
    def do_team(self, line):
        """Look up a team's statistics via: team <team_name>"""
        # Input hadning -> same as do_player: empty check, normalzie, searhc Clubnames
        query = line.strip()

        if not query:
            print("Please enter a team name to search. Such as: team Arsenal")
            return
        
        matches = self._find_club(query)
        if matches is None:
            print(f"No teams found matching '{query}'. Try a different spelling.")
            return

        # Fitler: self.df[self.df["ClubName"].str.containts(...)]
        # Agg and print 
        # len(squad) -> squad size
        # squad["Age"].mean()
        # squad["NationCode"].nunique()
        # squad["Gls"].sum() -> goals
        # squad["Ast"].sum() -> assists
        # squad.loc[squad["Gls"].idxmax(), "Player"] -> top scorer
        
        # TODO CHECK FOR PROBLEMS IN THIS EDGE CASE!!!
        # TODO: SIMPLIFY LIKE do_compare VIA HELPER FUNCTIONS ABOVE AND RECYCLE!


        # NO SURFACE ERRORS YET.
        club_name = matches["ClubName"].iloc[0] # iloc to extract full club and coutnry form the first row of matches 
        club_country = matches["ClubCountry"].iloc[0]

        # Metrics
        squad_size = len(matches)
        avg_age = matches["Age"].mean()
        nations_count = matches["NationCode"].nunique()
        total_goals = matches["Gls"].sum()
        total_assists = matches["Ast"].sum()

        # Top Scorer
        top_scorer_row = matches.loc[matches["Gls"].idxmax()] # index at maximum -> returns label/index of the row where maximum is instead of just value itself via max()
        top_scorer_name = top_scorer_row["Player"]
        top_scorer_goals = top_scorer_row["Gls"]

        # Desigining a clean console card..

        # ===== ...
        # club_name (club_country) - Squad Overview
        # ===== ...
        # - Squd Size:        squad_size players
        # - Average Age:      avg_age years
        # - Diviersity:       nations_count unique nationalities
        # - Team Totals:      total_goals Goals | total_assists Assists
        # - Top Scorer (MVP): top_scorer_name (top_scorer_goals goals)
        # ===== ...

        print(f"\n{'=' * 50}")
        print(f"  {club_name} ({club_country}) - Squad Overview")
        print(f"{'=' * 50}")
        print(f" Squad Size:       {squad_size} players")
        print(f" Average Age:      {avg_age:.1f} years")
        print(f" Diversity:        {nations_count} unique nationalities")
        print(f" Team Totals:      {total_goals} Goals | {total_assists} Assists")
        print(f" Top Scorer (MVP): {top_scorer_name} ({top_scorer_goals} goals)")
        print(f"{'=' * 50}\n")

# do_compare
    def do_compare(self, line):
        # TODO
        # WORK ON do_compare NEXT!
        # Gonna be a bit tricker: we want a if/else struc:
        # trick is detecting whether the user typed two player onames or two team names
        # basically:
        # compare Arsenal Barcelona -> both found in ClubName -> team compare
        # compare Russo Harder -> both found in Player -> player compare
        # compare Arsenal Russo -> one of each -> error, tell the user
        # Also.. logically, we need a seperator.. else its Real Madrid vs Bayern Munich or Real vs. Madrid Bayern Munich
        # Therefore.. suggest: line.split(" vs ")

        # Attributes for the two:

        # Player: Club, Position, Nationality, Age
        # Goals, Assists, G+A, Minutes, Matches played

        # Team: Squad size, Avg age, Nationalities, 
        # Total goals, Total asissts, Top scorer, Most assists
        parts = line.split(" vs ")

        query1 = parts[0].strip()
        query2 = parts[1].strip()

        # TODO .... helpers to detect what the user typed? Prob.. and then catch them via if/else.. or..

        club1 = self._find_club(query1)
        club2 = self._find_club(query2)
        player1 = self._find_player(query1)
        player2 = self._find_player(query2)





# do_map
# TODO LATER: Atleast cuz need folium struc first from Emily 
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