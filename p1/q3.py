from itertools import product


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self):
        self.quantity = 0

    def restock(self, quantity):
        self.quantity += quantity

    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


class Inventory:
    price = 0

    def __init__(self, *products):
        self.products = list(products)

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self):
        if product in self.products:
            self.products.remove(product)

    @staticmethod
    def update_product(self, new_price):
        Inventory.price += new_price

    def read_inventory(self):
        print(f"Inventory: {self.products}")



