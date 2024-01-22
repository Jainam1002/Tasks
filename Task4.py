from datetime import date
from operator import attrgetter
import re

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company_type):
        self.name = self.validate_name(name)
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.street = self.validate_street(street)
        self.city = self.validate_name(city)
        self.state = self.validate_name(state)
        self.country = self.validate_name(country)
        self.company_type = self.validate_company_type(company_type)

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise ValueError("Name cannot contain numbers.")
        return value

    def validate_email(self, value):
        # Implement your email validation logic here
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email address.")
        return value

    def validate_phone(self, value):
        # Implement your phone number validation logic here
        if not re.match(r"\d{10}", value):
            raise ValueError("Invalid phone number.")
        return value

    def validate_street(self, value):
        return value

    def validate_company_type(self, value):
        valid_types = ["company", "contact", "billing", "shipping"]
        if value not in valid_types:
            raise ValueError("Invalid company type.")
        return value


class OrderLine:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calculate_subtotal()

    def calculate_subtotal(self):
        return self.quantity * self.price


class Order:
    def __init__(self, number, order_date, company, billing, shipping, order_lines):
        self.number = number
        self.date = self.validate_date(order_date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_lines
        self.total_amount = self.calculate_total_amount()

    def validate_date(self, value):
        today = date.today()
        if value < today:
            raise ValueError("Invalid order date. Order date cannot be in the past.")
        return value

    def calculate_total_amount(self):
        return sum(line.subtotal for line in self.order_lines)

    def display_order_and_customer_information(self):
        print(f"Order Number: {self.number}")
        print(f"Order Date: {self.date}")
        print("Customer Information:")
        print(f"  Name: {self.company.name}")
        print(f"  Email: {self.company.email}")
        print(f"  Phone: {self.company.phone}")
        print(f"  Street: {self.company.street}")
        print(f"  City: {self.company.city}")
        print(f"  State: {self.company.state}")
        print(f"  Country: {self.company.country}")
        print(f"  Company Type: {self.company.company_type}")
        print(f"Total Amount: ${self.total_amount}")
        print("\nOrder Lines:")
        for line in self.order_lines:
            print(f"  Product: {line.product}, Quantity: {line.quantity}, Price: ${line.price}, Subtotal: ${line.subtotal}")
        print("\n")


# Example usage:
customer1 = Customer("Bill Gates", "bill.gates@gmail.com", "1234567890", "123 Main St", "Cityville", "CA", "USA", "company")
order_line1 = OrderLine(None, "Product A", 2, 10.99)
order_line2 = OrderLine(None, "Product B", 1, 5.99)
order1 = Order("123456", date(2024, 1, 22), customer1, None, None, [order_line1, order_line2])

customer2 = Customer("Michel Johnson", "mitchel.johnson@example.com", "9876543210", "456 Oak St", "Townsville", "NY", "USA", "billing")
order_line3 = OrderLine(None, "Product C", 3, 15.99)
order_line4 = OrderLine(None, "Product A", 1, 10.99)
order2 = Order("789012", date(2024, 2, 15), customer2, None, None, [order_line3, order_line4])

customer3 = Customer("Bob Smith", "bob.smith@example.com", "5556667777", "789 Pine St", "Cityburg", "TX", "USA", "shipping")
order_line5 = OrderLine(None, "Product B", 2, 5.99)
order_line6 = OrderLine(None, "Product C", 1, 15.99)
order3 = Order("345678", date(2024, 3, 5), customer3, None, None, [order_line5, order_line6])

customer4 = Customer("Traves Head", "Tra.head@example.com", "5566889911", "78 yute St", "Hamburg", "Munich", "Germany", "contact")
order_line7 = OrderLine(None, "Product B", 3, 6.99)
order_line8 = OrderLine(None, "Product C", 2, 14.99)
order4 = Order("345678", date(2024, 2, 5), customer4, None, None, [order_line7, order_line8])

# Create a list of orders
orders = [order1, order2, order3, order4]

# Sort orders based on date
sorted_orders = sorted(orders, key=attrgetter('date'), reverse = True)

# Display sorted orders
print("Sorted Orders:")
for order in sorted_orders:
    order.display_order_and_customer_information()
