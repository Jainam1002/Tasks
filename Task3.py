class Location:
    def __init__(self, name, code):
        self.name, self.code = name, code

    def __str__(self):
        return f"{self.name}"

    def display_product_list(self, products):
        print(f"\nLocation: {self.name}")
        for product in products:
            stock = product.stock_at_locations.get(self, 0)
            print(f"Product: {product.name} (Code: {product.code}), Stock: {stock} units")


class Product:
    def __init__(self, name, code):
        self.name, self.code, self.stock_at_locations = name, code, {}

    def __str__(self):
        return f"{self.name} (Code: {self.code})"

    def display_info(self):
        print(f"\nProduct: {self.name} (Code: {self.code}), Stock at Locations: {self.stock_at_locations}")

    def display_product_list_by_location(self, locations):
        for location in locations:
            stock = self.stock_at_locations.get(location, 0)
            print(f"Product: {self.name} (Code: {self.code}), Stock at {location}: {stock} units")


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location, self.to_location, self.product, self.quantity = from_location, to_location, product, quantity

    @staticmethod
    def movements_by_product(product, movements):
        return [movement for movement in movements if movement.product == product]


# Create Location objects
location1 = Location("Warehouse1", "L001")
location2 = Location("Warehouse2", "L002")
location3 = Location("Warehouse3", "L003")
location4 = Location("Warehouse4", "L004")

# Create Product objects
product1 = Product("Tshirts", "P001")
product2 = Product("Shurts", "P002")
product3 = Product("Pants", "P003")
product4 = Product("Trousers", "P004")
product5 = Product("Jacket", "P005")

# Add new members inside the product “stock_at_locations” with initial stock at each location
for product in [product1, product2, product3, product4, product5]:
    product.stock_at_locations = {location1: 100, location2: 200, location3: 300, location4: 350}

# Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve.
movements = [
    Movement(location1, location2, product1, 90),
    Movement(location2, location3, product1, 60),
    Movement(location3, location4, product1, 40),
    Movement(location4, location1, product1, 70),
    Movement(location1, location2, product2, 90),
    Movement(location2, location3, product2, 100),
    Movement(location3, location4, product2, 120),
]

# Manage exceptions if product stock goes negative
for movement in movements:
    if movement.product.stock_at_locations.get(movement.from_location, 0) - movement.quantity < 0:
        print(f"Error: Insufficient stock of {movement.product.name} at {movement.from_location.name}")
    else:
        movement.product.stock_at_locations[movement.from_location] -= movement.quantity
        movement.product.stock_at_locations[movement.to_location] = movement.product.stock_at_locations.get(movement.to_location, 0) + movement.quantity

# Display movements of each product
for product in [product1, product2, product3, product4, product5]:
    print(f"\nMovements for {product.name} (Code: {product.code}):")
    for movement in Movement.movements_by_product(product, movements):
        print(f"From: {movement.from_location.name} To: {movement.to_location.name}, Quantity: {movement.quantity}")

# Display product details with its stock at various locations
for location in [location1, location2, location3, location4]:
    location.display_product_list([product1, product2, product3, product4, product5])
