class Player:

    def __init__(self, name, country, role, base_price, rating):
        self.name = name
        self.country = country
        self.role = role
        self.base_price = int(base_price)
        self.rating = int(rating)

    def display(self):
        print(self.name, "-", self.country, "-", self.role, "-", self.base_price, "-", self.rating)