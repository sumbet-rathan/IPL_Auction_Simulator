class Team:

    def __init__(self, name):
        self.name = name
        self.purse = 2000
        self.squad = []
        self.max_players = 25
        self.min_players = 18
        self.max_overseas = 8

    # count overseas players
    def foreign_count(self):
        count = 0
        for player in self.squad:
            if player.country == "Overseas":
                count += 1
        return count

    # check if team can buy
    def can_buy(self, player, price):

        if self.purse < price:
            return False

        if len(self.squad) >= self.max_players:
            return False

        if player.country == "Overseas" and self.foreign_count() >= self.max_overseas:
            return False

        return True

    # buy player
    def buy(self, player, price):
        self.squad.append(player)
        self.purse -= price
        print(self.name, "bought", player.name)