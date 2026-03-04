import random
from team import Team
from utils import load_players

class Auction:

    def __init__(self):
        self.players = load_players()
        self.teams = self.create_teams()
        self.unsold_players = []

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

        # choose 3 random teams to bid
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
        else:
            self.unsold_players.append(player)

    # show results
    def show_results(self):

        print("\nTEAM SQUADS\n")

        for team in self.teams:
            print("----", team.name, "----")
            for p in team.squad:
                print(p.name, "-", p.role, "-", p.country)
            print("Total Players:", len(team.squad))
            print()

        print("Unsold Players:", len(self.unsold_players))