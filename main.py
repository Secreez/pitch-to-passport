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
    return "".join([_ for _ in nfkd if not unicodedata.combining(_)]).lower()

class PitchToPassport(cmd.Cmd):
    prompt = "PitchToPassport> "
    intro = "Welcome to Pitch to Passport! Type 'help' for commands. Use 'exit' to get out of the program."

    def __init__(self, df):
        super().__init__()
        self.df = df 

        # normalized names once at startup for accent searches
        self.df["_NormalizedPlayer"] = self.df["Player"].fillna("").apply(normalize_text)
        self.df["_NormalizedClub"] = self.df["ClubName"].fillna("").apply(normalize_text)

    # helper func to not dublicate stuff along the way
    def _find_club(self, query):
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

    def _team_card(self, matches):
        club_name = matches["ClubName"].iloc[0]
        club_country = matches["ClubCountry"].iloc[0]
        squad_size = len(matches)
        avg_age = matches["Age"].mean()
        nations_count = matches["NationCode"].nunique()
        total_goals = matches["Gls"].sum()
        total_assists = matches["Ast"].sum()
        top_scorer_row = matches.loc[matches["Gls"].idxmax()]
        top_scorer_name = top_scorer_row["Player"]
        top_scorer_goals = top_scorer_row["Gls"]

        print(f"\n{'=' * 50}")
        print(f"  {club_name} ({club_country}) - Squad Overview")
        print(f"{'=' * 50}")
        print(f" Squad Size:       {squad_size} players")
        print(f" Average Age:      {avg_age:.1f} years")
        print(f" Diversity:        {nations_count} unique nationalities")
        print(f" Team Totals:      {total_goals} Goals | {total_assists} Assists")
        print(f" Top Scorer (MVP): {top_scorer_name} ({top_scorer_goals} goals)")
        print(f"{'=' * 50}\n")

    def _player_card(self, row):
        print(f"\n{'=' * 50}")
        print(f"  {row['Player']} - Player Profile")
        print(f"{'=' * 50}")
        print(f" Club:      {row['ClubName']} ({row['ClubCountry']})")
        print(f" Position:  {row['Pos']}")
        print(f" Shirt:     #{row['ShirtNumber']}")
        print(f" Age:       {row['Age']}")
        print(f" Goals:     {row['Gls']}")
        print(f" Assists:   {row['Ast']}")
        print(f" Minutes:   {row['Min']}")
        print(f"{'=' * 50}\n")

    def do_player(self, line):
        """Look up a player via: player <name>"""
        query = line.strip()

        if not query:
            print("Please enter a player name to search. Such as: player Mead")
            return

        matches = self._find_player(query)

        if matches is None:
            print(f"No players found matching {query}. Try a different spelling or single name")
            return

        match_word = "match" if len(matches) == 1 else "matches"
        print(f"\nFound {len(matches)} {match_word} for '{query}':")
        print(f"{"=" * 90}")
        for _, row in matches.iterrows():
            print( # increment as needed. but should be sufficient really.
                f"- {row['Player']:<20} | #{row['ShirtNumber']:<3} | "
                f"Pos: {row['Pos']:<6} | Club: {row['ClubName']} ({row['ClubCountry']})"
                )
        print(f"{"=" * 90}\n")

# do_team
    def do_team(self, line):
        """Look up a team's statistics via: team <team_name>"""
        query = line.strip()

        if not query:
            print("Please enter a team name. Such as: team Arsenal")
            return

        matches = self._find_club(query)
        if matches is None:
            print(f"No teams found matching '{query}'. Try a different spelling.")
            return

        if matches["ClubName"].nunique() > 1:
            print(f"Multiple teams found for '{query}'. Be more specific:")
            for club in matches["ClubName"].unique():
                print(f"  - {club}")
            return

        self._team_card(matches)


# do_compare
    def do_compare(self, line):
        """Compare either player1 vs. player2 or team1 vs. team2 via: compare <x1> vs <x2>"""
        if not line.strip():
            print("Please enter two names / teams. Example: compare Arsenal vs Barcelona")
            return

        parts = line.split(" vs ")

        if len(parts) != 2:
            # Else IndexError -> as only has oen element and parts[1] crashes.
            print("Please use 'vs' to separate. Example: compare Arsenal vs Barcelona")
            return

        query1 = parts[0].strip()
        query2 = parts[1].strip()

        club1 = self._find_club(query1)
        club2 = self._find_club(query2)
        player1 = self._find_player(query1)
        player2 = self._find_player(query2)

        if club1 is not None and club2 is not None:
            if club1["ClubName"].nunique() > 1: # if we use len() we whould get 22 Arsenal prints -> because all 22 Players therefore nunique
                print(f"Multiple clubs found for '{query1}'. Be more specific:")
                for _, row in club1.iterrows():
                    print(f"  - {row['ClubName']} ({row['ClubCountry']})")
                return

            if club2["ClubName"].nunique() > 1:
                print(f"Multiple clubs found for '{query2}'. Be more specific:")
                for _, row in club2.iterrows():
                    print(f"  - {row['ClubName']} ({row['ClubCountry']})")
                return

            self._team_card(club1)
            print(f"\n{'-' * 22}  VS  {'-' * 22}\n")
            self._team_card(club2)

        elif player1 is not None and player2 is not None:
            if len(player1) > 1:
                print(f"Multiple players found for '{query1}'. Be more specific:")
                for _, row in player1.iterrows():
                    print(f"  - {row['Player']} ({row['ClubName']})")
                return

            if len(player2) > 1:
                print(f"Multiple players found for '{query2}'. Be more specific:")
                for _, row in player2.iterrows():
                    print(f"  - {row['Player']} ({row['ClubName']})")
                return

            self._player_card(player1.iloc[0])
            print(f"\n{'-' * 22}  VS  {'-' * 22}\n")
            self._player_card(player2.iloc[0])

        else:
            print(f"Could not match '{query1}' and '{query2}' to the same type.")
            print("Make sure both are clubs or both are players. Example: compare Arsenal vs Barcelona")








# do_map
# TODO LATER: Atleast cuz need folium struc first from Emily 
#• map <team>: Map linking each player’s home country to the club, with stat popups
#• map all: Global talent migration map across all 18 UWCL clu
    def do_map(self, line):
      pass


# TODO: OPTIONAL
#• map <player>: single-line map for one player’s journey. Low visual value vs. team/global maps, easy to cut.
#• CL trophies & market value in compare <team1> <team2>: needs extra data sourcing (ESPN/
# Transfermarkt) and merging; added only if time allows

    def do_exit(self, _):
      """Exit the program"""
      return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="data/players_enriched.csv")
    args = parser.parse_args()
    df = pd.read_csv(args.config, encoding="utf-8")
    PitchToPassport(df).cmdloop()