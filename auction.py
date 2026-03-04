import random
import csv
from team import Team
from utils import load_players


class Auction:

    def __init__(self):
        self.players = load_players()
        self.teams = self.create_teams()
        self.unsold_players = []
        self.sold_players = []

    # create IPL teams
    def create_teams(self):
        team_names = ["SRH","CSK","MI","RCB","KKR","RR","DC","GT"]
        teams = []
        for name in team_names:
            teams.append(Team(name))
        return teams

    # start auction
    def start_auction(self):
        print("AUCTION STARTED\n")

        for player in self.players:
            self.bid_player(player)

        print("\nAuction Finished")
        self.show_results()

    # bidding logic
    def bid_player(self, player):

        bidding_teams = random.sample(self.teams, 3)
        price = player.base_price
        winner = None

        for team in bidding_teams:
            bid_price = price + random.randint(5, 20)

            if team.can_buy(player, bid_price):
                price = bid_price
                winner = team

        if winner:
            winner.buy(player, price)
            self.sold_players.append(player)
        else:
            self.unsold_players.append(player)

    # save results to CSV
    def show_results(self):

        # TEAM SQUADS CSV
        with open("data/team_squads.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Team", "Player", "Role", "Country"])

            for team in self.teams:
                for player in team.squad:
                    writer.writerow([team.name, player.name, player.role, player.country])

        # UNSOLD PLAYERS CSV
        with open("data/unsold_players.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Player", "Role", "Country"])

            for player in self.unsold_players:
                writer.writerow([player.name, player.role, player.country])

        print("\nCSV files created inside data folder.")