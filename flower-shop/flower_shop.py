flowers_list = []
bouquets = []
order_list = []


class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def save_flower(self):
        flower = {'type': self.name, 'color': self.color}
        flowers_list.append(flower)


class Bouquet:
    def __init__(self, name, price, quantity, *flower_types):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.flower_types = flower_types

    def create_bouquet(self):
        bouquet = []
        for flower in flowers_list:
            for flower_type in self.flower_types:
                if flower['type'] == flower_type:
                    bouquet.append(flower)
        bouquet_dict = {'bouquet_name': self.name, 'quantity': self.quantity, 'price': self.price, 'bouquet': bouquet}
        bouquets.append(bouquet_dict)


class Shop:
    def __init__(self, bouquet_name, ordered_quantity):
        self.bouquet_name = bouquet_name
        self.ordered_quantity = ordered_quantity

    def sell(self):
        for bouquet in bouquets:
            if bouquet['bouquet_name'] != self.bouquet_name:
                continue
            else:
                if bouquet['quantity'] >= self.ordered_quantity:
                    bouquet['quantity'] -= self.ordered_quantity
                else:
                    self.order()

    def order(self):
        order = {'bouquet_name': self.bouquet_name, 'ordered_quantity': self.ordered_quantity}
        order_list.append(order)


if __name__ == "__main__":
    rose = Flower('rose', 'pink')
    lily = Flower('lily', 'white')

    rose.save_flower()
    lily.save_flower()

    fantastic = Bouquet('fantastic', 1.25, 5, 'rose', 'lily')
    romantic = Bouquet('romantic', 1.50, 10, 'lily')

    fantastic.create_bouquet()
    romantic.create_bouquet()

    flower_shop = Shop('fantastic', 2)
    flower_shop.sell()
