# cart.py

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product["price"] * self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return len(self.items) == 0

    def total(self):
        return sum(item.get_total_price() for item in self.items)

    def __iter__(self):
        return iter(self.items)
