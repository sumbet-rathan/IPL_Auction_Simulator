import csv
from player import Player

def load_players():

    players = []

    with open("data/players.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = Player(
                row["Name"],
                row["Country"],
                row["Role"],
                row["Base_Price"],
                row["Rating"]
            )

            players.append(player)

    print("Players loaded:", len(players))
    return players