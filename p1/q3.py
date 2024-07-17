class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, quantity_sell):
        self.quantity -= quantity_sell

    def restock(self, quantity_restock):
        self.quantity += quantity_restock

    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price, quantity):
        for product1 in self.products:
            if product1["product_name"] == product_name:
                print(f"Product {product_name} already exists.")
                return
        self.products.append({"product_name": product_name, "price": price, "quantity": quantity})
        print(f"Product {product_name} added.")

    def remove_product(self, product_name):
        for product1 in self.products:
            if product1["product_name"] == product_name:
                self.products.remove(product1)
                print(f"Product {product_name} removed.")
                return
        print(f"Product {product_name} not found.")

    def update_product(self, product_name, price, quantity):
        for product1 in self.products:
            if product1["product_name"] == product_name:
                product1["price"] = price
                product1["quantity"] = quantity
                print(f"Product {product_name} updated.")
                return
        print(f"Product {product_name} not found.")

    def read_inventory(self):
        if self.products:
            print("Inventory:")
            for product in self.products:
                print(f"Name: {product['product_name']}, Price: {product['price']}, Quantity: {product['quantity']}")
        else:
            print("Inventory is empty.")


# Instantiate and use the Inventory and Product classes
inventory = Inventory()

# Add products to the inventory
inventory.add_product("Apple", 0.5, 100)
inventory.add_product("Banana", 0.3, 150)

# Display the inventory
inventory.read_inventory()

# Update a product's price and quantity
inventory.update_product("Apple", price=0.6, quantity=120)

# Display the updated inventory
inventory.read_inventory()

# Remove a product from the inventory
inventory.remove_product("Banana")

# Display the updated inventory
inventory.read_inventory()

