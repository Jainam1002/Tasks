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

def create_category_tree(categories, parent=None):
    if not categories:
        return None

    current_category = Category(categories[0], parent)
    if len(categories) > 1:
        current_category.children = create_category_tree(categories[1:], current_category)
    return current_category

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

categories = ["Vehicle", "Car", "Bike", "Petrol", "Diesel"]
root_category = create_category_tree(categories)


product1 = Product("Ecar", "P001", root_category)
product2 = Product("Car", "P002", root_category)
product3 = Product("Bike", "P003", root_category)
product4 = Product("Sedan", "P004", root_category.children)
product5 = Product("Sports Car", "P005", root_category.children)
product6 = Product("SUV", "P006", root_category.children)
product7 = Product("Yamaha", "P007", root_category.children.children)
product8 = Product("Ducati", "P008", root_category.children.children)
product9 = Product("Hayabusa", "P009", root_category.children.children)
product10 = Product("Ferrari", "P010", root_category.children.children.children)
product11 = Product("Supra", "P011", root_category.children.children.children)
product12 = Product("Mashtang", "P012", root_category.children.children.children)
product13 = Product("Swift", "P013", root_category.children.children.children.children)
product14 = Product("Verna", "P014", root_category.children.children.children.children)
product15 = Product("i20", "P015", root_category.children.children.children.children)


display_category(root_category)


display_products_by_category([root_category, root_category.children, root_category.children.children, root_category.children.children.children, root_category.children.children.children.children])






