# CLI Struc

# Standard library
import argparse
import cmd
import unicodedata

# External library
import pandas as pd
import folium
from collections import Counter
#import webbrowser

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
    def do_map(self, line):
      '''Either link a team's players' home countries to the club's stadium 
      or show the global talent migration across all clubs'''

      #AI-generated dictionary
      country_capital_coordinates = {
        "ENG": [51.5074, -0.1278],    # London
        "GER": [52.5200, 13.4050],    # Berlin
        "AUS": [-35.2809, 149.1300],  # Canberra
        "NED": [52.3676, 4.9041],     # Amsterdam
        "USA": [38.9072, -77.0369],   # Washington, D.C.
        "NOR": [59.9139, 10.7522],    # Oslo
        "IRL": [53.3498, -6.2603],    # Dublin
        "SCO": [55.9533, -3.1883],    # Edinburgh
        "ESP": [40.4168, -3.7038],    # Madrid
        "CAN": [45.4215, -75.6972],   # Ottawa
        "SWE": [59.3293, 18.0686],    # Stockholm
        "BRA": [-15.7939, -47.8828],  # Brasília
        "VEN": [10.4806, -66.9036],   # Caracas
        "DEN": [55.6761, 12.5683],    # Kopenhagen
        "POR": [38.7223, -9.1393],    # Lissabon
        "POL": [52.2297, 21.0122],    # Warschau
        "SUI": [46.9480, 7.4474],     # Bern
        "CIV": [5.3599, -4.0083],     # Abidjan
        "ITA": [41.9028, 12.4964],    # Rom
        "SRB": [44.7866, 20.4489],    # Belgrad
        "AUT": [48.2082, 16.3738],    # Wien
        "ISL": [64.1466, -21.9426],   # Reykjavík
        "JPN": [35.6762, 139.6503],   # Tokio
        "FRA": [48.8566, 2.3522],     # Paris
        "MWI": [-13.9626, 33.7741],   # Lilongwe
        "HAI": [18.5944, -72.3074],   # Port-au-Prince
        "CHI": [-33.4489, -70.6693],  # Santiago (Chile)
        "WAL": [51.4816, -3.1791],    # Cardiff
        "BEL": [50.8503, 4.3517],     # Brüssel
        "HUN": [47.4979, 19.0402],    # Budapest
        "GRE": [37.9838, 23.7275],    # Athen
        "SVN": [46.0569, 14.5058],    # Ljubljana
        "CRC": [9.9281, -84.0907],    # San José
        "MLI": [12.6392, -8.0029],    # Bamako
        "COL": [4.7110, -74.0721],    # Bogotá
        }

      #AI-generated dictionary
      country_colors = {
              "ENG": "red",
              "GER": "black",
              "AUS": "darkblue",
              "NED": "orange",
              "USA": "blue",
              "NOR": "darkred",
              "IRL": "green",
              "SCO": "cadetblue",
              "ESP": "darkred",
              "CAN": "red",
              "SWE": "blue",
              "BRA": "green",
              "VEN": "orange",
              "DEN": "red",
              "POR": "darkgreen",
              "POL": "red",
              "SUI": "red",
              "CIV": "orange",
              "ITA": "green",
              "SRB": "darkred",
              "AUT": "red",
              "ISL": "blue",
              "JPN": "red",
              "FRA": "blue",
              "MWI": "green",
              "HAI": "blue",
              "CHI": "red",
              "WAL": "green",
              "BEL": "black",
              "HUN": "green",
              "GRE": "blue",
              "SVN": "cadetblue",
              "CRC": "red",
              "MLI": "green",
              "COL": "yellow"
      }

      query = line.strip()

      if not query:
        print("Please enter a team name, such as: map Barcelona, or map all")

      m = folium.Map(location=(54.5260, 15.2551), zoom_start=4, tiles="CartoDB.Voyager")

      # map all
      if query.casefold() == "all":

        for club_name, club_df in df.groupby("ClubName"):
            stadium_coordinates = [float(club_df["ClubLat"].iloc[0]), float(club_df["ClubLon"].iloc[0])]

            folium.Marker(
                location=stadium_coordinates,
                tooltip=club_name,
                icon=folium.Icon(icon="star", color="blue")
                ).add_to(m)

            country_counts = Counter(club_df["NationCode"])

            for code, count in country_counts.items():
                home_coordinates = country_capital_coordinates[code]
                color = country_colors[code]

                folium.PolyLine(
                    locations=[home_coordinates, stadium_coordinates], color=color, weight=count).add_to(m)
                    
        m.save('map.html')

      # map <team>
      else:
        matches = self._find_club(query)

        if matches is None:
            print(f"No teams found matching '{query}'. Try a different spelling.")
            return

        if matches["ClubName"].nunique() > 1:
            print(f"Multiple teams found for '{query}'. Be more specific:")
            for club in matches["ClubName"].unique():
                print(f"  - {club}")
            return

        stadium_coordinates = [float(matches["ClubLat"].iloc[0]), float(matches["ClubLon"].iloc[0])]

        nation_codes = matches["NationCode"]

        folium.Marker(
            location=stadium_coordinates,
            icon=folium.Icon(color="blue", icon="star", prefix="fa"),
            ).add_to(m)

        country_counts = Counter(nation_codes)

        for code, count in country_counts.items():
            coord = country_capital_coordinates[code]
            color = country_colors[code]
            folium.PolyLine(
                locations=[coord, stadium_coordinates], 
                weight=count, 
                color=color
            ).add_to(m)
            
        m.save('map.html')


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