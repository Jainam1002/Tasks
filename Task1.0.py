class Category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price


def create_category():
    name = input("Enter category name: ")
    code = input("Enter category code: ")
    no_of_products = int(input("Enter the number of products in this category: "))
    return Category(name, code, no_of_products)


def create_product(categories):
    name = input("Enter product name: ")
    code = input("Enter product code: ")
    
  
    print("Available Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category.name}")

   
    selected_category_index = int(input("Select a category (enter the corresponding number): ")) - 1
    category = categories[selected_category_index]

    price = float(input("Enter product price: "))
    return Product(name, code, category, price)


categories = []
products = []


for _ in range(3):
    category = create_category()
    categories.append(category)


for _ in range(10):
    product = create_product(categories)
    products.append(product)


for category in categories:
    print(f"{category.name} (Code: {category.code}) - No. of Products: {category.no_of_products}")



print("\nProducts sorted by Price (High to Low):")
for product in sorted(products, key=lambda x: x.price, reverse=True):
    print(f"{product.name} (Code: {product.code}) - Price: ${product.price}")



searched_product_code = input("Enter the code of the product you want to search: ")
found_product = next((product for product in products if product.code == searched_product_code), None)

if found_product is not None:
    print(f"\nProduct found: {found_product.name} (Code: {found_product.code}) - Price: ${found_product.price}")
else:
    print("\nProduct not found.")
