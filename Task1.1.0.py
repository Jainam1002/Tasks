class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def update_product_count(self, products):
        self.no_of_products = sum(1 for product in products if product.category == self)

    def display_sorted_products(self, products):
        print(f"\nProducts Sorted by Price (High to Low) in {self.name} category:")
        for product in products:
            if product.category == self:
                print(f"Name: {product.name}, Code: {product.code}, Price: ${product.price}")


class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

   
    def bubble_sort_products_by_price(products, reverse=False):
        n = len(products)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if (products[j].price < products[j + 1].price) if reverse else (products[j].price > products[j + 1].price):
                    products[j], products[j + 1] = products[j + 1], products[j]

    def search_product_by_code(self, products, searched_product_code):
        found_product = next((product for product in products if product.code == searched_product_code), None)
        return found_product


category1 = Category("Stationary", "S001")
category2 = Category("Footwear", "A002")
category3 = Category("Medicines", "C003")

products = []

product1 = Product("Pen Box", "P001", category1, 20)
product2 = Product("Nike Dunk Air Rift", "P002", category2, 500)
product3 = Product("Combiflam", "P003", category3, 100)
product4 = Product("Pencil Set", "P004", category1, 10)
product5 = Product("Paracetamol", "P005", category3, 40)
product6 = Product("Adidas Gazelle", "P006", category2, 300)
product7 = Product("Stick Pen", "P007", category1, 12)
product8 = Product("Adidas Stan Smith", "P008", category2, 600)
product9 = Product("Armour Thyroid (Thyroid tablets)", "P009", category3, 70)
product10 = Product("Relaxed Fit", "P010", category2, 400)

products.extend([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10])


for category in [category1, category2, category3]:
    category.update_product_count(products)


Product.bubble_sort_products_by_price(products, reverse=True)


print("\nAll Products Sorted by Price (High to Low):")
for product in products:
    print(f"Name: {product.name}, Code: {product.code}, Category: {product.category.name}, Price: ${product.price}")


searched_product_code = input("\nEnter the product code to search: ")
found_product = next((product for product in products if product.code == searched_product_code), None)

if found_product:
    print(f"\nProduct found with code {searched_product_code}:")
    print(f"Name: {found_product.name}, Category: {found_product.category.name}, Price: ${found_product.price}")
else:
    print(f"\nProduct with code {searched_product_code} not found.")
