class Product:
    def __init__(self, name, code, category):
        self.name = name
        self.code = code
        self.category = category
        category.add_product(self)

class Category:
    def __init__(self, code, parent=None):
        self.code = code
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = []

    def generate_display_name(self):
        if self.parent:
            return f"{self.parent.generate_display_name()} > {self.code}"
        else:
            return self.code

    def add_product(self, product):
        self.products.append(product)

    def add_child_products_recursively(self, product):
        for child_category in self.get_all_child_categories():
            child_category.add_product(product)

    def get_all_child_categories(self):
        all_child_categories = []
        for product in self.products:
            if isinstance(product, Category):
                all_child_categories.append(product)
                all_child_categories.extend(product.get_all_child_categories())
        return all_child_categories

def display_category(category):
    print(f"Category: {category.code}")
    print(f"Display Name: {category.display_name}")
    print("Product Details:")
    for product in category.products:
        print(f"  - Code: {product.code}, Name: {product.name}")
    print("\n")

def display_products_by_category(categories):
    for category in categories:
        print(f"Category: {category.display_name}")
        for product in category.products:
            print(f"  - Code: {product.code}, Name: {product.name}")
        print("\n")

vehicle_category = Category("Vehicle")
car_category = Category("Car", parent=vehicle_category)
bike_category = Category("Bike", parent=vehicle_category)
petrol_category = Category("Petrol", parent=car_category)
diesel_category = Category("Diesel", parent=car_category)

product1 = Product("Ecar", "P001", vehicle_category)
product2 = Product("Car", "P002", vehicle_category)
product3 = Product("Bike", "P003", vehicle_category)
product4 = Product("Sedan", "P004", car_category)
product5 = Product("Sports Car", "P005", car_category)
product6 = Product("SUV", "P006", car_category)
product7 = Product("Yamaha", "P007", bike_category)
product8 = Product("Ducati", "P008", bike_category)
product9 = Product("Hayabusa", "P009", bike_category)
product10 = Product("Ferrari", "P010", petrol_category)
product11 = Product("Supra", "P011", petrol_category)
product12 = Product("Mashtang", "P012", petrol_category)
product13 = Product("Swift", "P013", diesel_category)
product14 = Product("Verna", "P014", diesel_category)
product15 = Product("i20", "P015", diesel_category)

# ... (previous code)

categories = [vehicle_category, car_category, bike_category, petrol_category, diesel_category]

# Add child products recursively
for category in categories:
    for product in category.get_all_child_categories():
        category.add_child_products_recursively(product)

# Display products for all categories
display_products_by_category(categories)



