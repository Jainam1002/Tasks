class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

def bubble_sort(products, key_function, reverse=False):
    n = len(products)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (key_function(products[j]) > key_function(products[j + 1])) if not reverse else (
                    key_function(products[j]) < key_function(products[j + 1])):
                products[j], products[j + 1] = products[j + 1], products[j]


category1 = Category("Stationaray", "S001")
category2 = Category("Footwear", "A002")
category3 = Category("Medicines", "C003")

product1 = Product("Pen Box", "P001", category1, 20 )
product2 = Product("Nike Dunk Air Rift", "P002", category2, 500 )
product3 = Product("Combiflam", "P003", category3, 100 )
product4 = Product("Pencil Set", "P004", category1, 10 )
product5 = Product("Paracetamol", "P005", category3, 40 )
product6 = Product("Adidas Gazelle", "P006", category2, 300 )
product7 = Product("Stick Pen", "P007", category1, 12 )
product8 = Product("Adidas Stan Smith", "P008", category2, 600 )
product9 = Product("Armour Thyroid (Thyroid tablets)", "P009", category3, 70 )
product10 = Product("Relaxed Fit,", "P010", category2, 400 )


category1.no_of_products += 4  
category2.no_of_products += 3  
category3.no_of_products += 3  

print(f"{category1.name} (Code: {category1.code}) - No. of Products: {category1.no_of_products}")
print(f"{category2.name} (Code: {category2.code}) - No. of Products: {category2.no_of_products}")
print(f"{category3.name} (Code: {category3.code}) - No. of Products: {category3.no_of_products}")


bubble_sort([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10],
            key_function=lambda x: x.price, reverse=True)
print("\nProducts Sorted by Price (High to Low):")
for product in [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]:
    print(f"Name: {product.name}, Code: {product.code}, Category: {product.category.name}, Price: ${product.price}")



searched_product_code = input("\nEnter the product code to search: ")
found_product = next((product for product in [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10] if product.code == searched_product_code), None)

if found_product:
    print(f"\nProduct found with code {searched_product_code}:")
    print(f"Name: {found_product.name}, Category: {found_product.category.name}, Price: ${found_product.price}")
else:
    print(f"\nProduct with code {searched_product_code} not found.")
