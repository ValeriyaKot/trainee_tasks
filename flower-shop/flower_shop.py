from enum import Enum, auto
from collections import defaultdict


class FlowerType(Enum):
    Rose = auto()
    Aster = auto()
    Tulip = auto()
    Lily = auto()
    Iris = auto()


class Flower:
    def __init__(self, flower_type):
        self.flower_type = flower_type

    def __str__(self):
        return 'flower type: {}'.format(self.flower_type)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.flower_type == other.flower_type


class Bouquet:
    def __init__(self, name, price, flowers=None):
        self.name = name
        self.price = price
        self.flowers = (defaultdict(int, flowers)
                        if flowers is not None
                        else defaultdict(int))

    def __str__(self):
        return 'Bouquet: {}'.format(self.name)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.name == other.name

    def __getitem__(self, key):
        return self.flowers[key]

    def __setitem__(self, key, value):
        self.flowers[key] = value


class Shop:
    def __init__(self, shop_name, bouquets=None):
        self.shop_name = shop_name
        self.bouquets = (defaultdict(int, bouquets)
                         if bouquets is not None
                         else defaultdict(int))

    def __str__(self):
        return self.shop_name

    def __getitem__(self, key):
        return self.bouquets[key]

    def __setitem__(self, key, value):
        self.bouquets[key] = value

    def check_quantity_of_bouquets(self, bouquet, quantity):
        if self.bouquets[bouquet] < quantity:
            raise ValueError('Not enough bouquets')

    def sell(self, bouquet, quantity):
        self.check_quantity_of_bouquets(bouquet, quantity)
        self.bouquets[bouquet] -= quantity

    def order(self, bouquet, quantity):
        self.bouquets[bouquet] += quantity


if __name__ == "__main__":
    rose = Flower(FlowerType.Rose)
    aster = Flower(FlowerType.Aster)
    lily = Flower(FlowerType.Lily)
    tulip = Flower(FlowerType.Tulip)
    iris = Flower(FlowerType.Iris)

    fantastic = Bouquet('fantastic', 1.25, {rose: 20})
    romantic = Bouquet('romantic', 1.50, {tulip: 5, rose: 20})

    shop = Shop('Iris', {fantastic: 10, romantic: 2})

    shop.sell(fantastic, 2)
    shop.sell(romantic, 1)
    shop.order(romantic, 2)
