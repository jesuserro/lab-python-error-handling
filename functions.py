# 1. Define a function named `initialize_inventory` that takes `products` as a parameter. 
# Inside the function, implement the code for initializing the inventory dictionary using a loop and user input.
def initialize_inventory(products):
    inventory = {product: int(input(f"Enter the quantity of {product}s available: ")) for product in products}
    return inventory

# Update function "get_customer_orders" to grab the pairs of product:quantity
def get_customer_orders():
    customer_orders = {}
    customer_orders_num = int(input("Enter the number of products you want to order: "))
    for i in range(customer_orders_num):
        product = input(f"Enter the name of product number {i + 1}: ")
        quantity = int(input(f"Enter the quantity of {product}: "))
        customer_orders[product] = quantity
    return customer_orders

# 4. Modify the update_inventory function to remove the product from the inventory if its quantity becomes zero after fulfilling the customer orders. 
# Use comprehension to filter out the products with a quantity of zero from the inventory.
def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        inventory[product] -= customer_orders[product]
    inventory = {product: quantity for product, quantity in inventory.items() if quantity > 0}
    return inventory

# 4. Define a function named `calculate_order_statistics` that takes `customer_orders` and `products` as parameters. 
# Inside the function, implement the code for calculating the order statistics (total products ordered, and percentage of unique products ordered). 
# The function should return these values.
def calculate_order_statistics(customer_orders, products):
    total_products_ordered = len(customer_orders)
    percentage_products_ordered = (total_products_ordered / len(products)) * 100
    return total_products_ordered, percentage_products_ordered

# 5. Define a function named `print_order_statistics` that takes `order_statistics` as a parameter. 
# Inside the function, implement the code for printing the order statistics.
def print_order_statistics(order_statistics):
    total_products_ordered, percentage_products_ordered = order_statistics
    print(f"Order Statistics:\nTotal Products Ordered: {total_products_ordered}\nPercentage of Products Ordered: {percentage_products_ordered}%")

# 6. Define a function named `print_updated_inventory` that takes `inventory` as a parameter. 
# Inside the function, implement the code for printing the updated inventory.
def print_updated_inventory(inventory):
    inventory_list = [f"- {product}: {quantity}" for product, quantity in inventory.items()]
    print("\n".join(inventory_list))

# 3. Add a new function to calculate the total price of the customer order. 
# For each product in customer_orders, prompt the user to enter the price of that product. 
# Use comprehension to calculate the total price. 
# Note: assume that the user can only have 1 unit of each product.
def calculate_total_price(customer_orders):
    total_price = 0
    for product in customer_orders:
        price = float(input(f"Enter the price of {product}: "))
        total_price += price * customer_orders[product]

    return total_price

# Create function to print total price, calling function "calculate_total_price" inside
def print_total_price(customer_orders):
    total_price = calculate_total_price(customer_orders)
    print(f"Total Price: {total_price} €")

