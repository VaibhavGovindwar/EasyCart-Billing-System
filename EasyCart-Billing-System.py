import csv
from prettytable import PrettyTable

# Path to the uploaded CSV file
csv_file_path = 'Inventory.csv'

# Load the CSV file with product details
products = {}
product_codes = {}
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Product_Name']:
            product_name = row['Product_Name'].strip()
            product_code = row['Product_Code'].strip()
            products[product_name] = {
                'product_code': row['Product_Code'].strip(),
                'price': float(row['Price'].strip()),
                'quantity': int(row['Quantity'].strip())
            }
            # Map product code to product name for reverse lookup
            product_codes[product_code] = product_name

print("------ Billing System ------")

# It will Create a table using PrettyTable and print a bill
table = PrettyTable(["Product Name", "Quantity", "Price", "Total Price"])
total1 = 0  # To keep track of the total price
total_quantity = 0  # To keep track of the total quantity

while True:
    # Manually enter a product Code according to product name listed in inventory file
    code = input("Enter Product Code (or 'q' to quit): ")

# enter "q" to quit and break the loop and print thr bill
    if code == 'q':
        break

    if code in product_codes:
        product_name = product_codes[code]  # Get the product name using the code
        qty = int(input("Enter Quantity : "))

        # Check if requested quantity is available
        if qty > products[product_name]['quantity']:
            print("Sorry, we do not have enough stock.")
            # if the product is out-of stock it will show available quantity
            print(f"Available quantity for '{product_name}': {products[product_name]['quantity']}")

        else:
            # Update quantity and total price
            total_quantity += qty
            item_price = products[product_name]['price']
            total_price = item_price * qty # multiply item per price with quantity entered
            total1 += total_price
            table.add_row([product_name, qty, item_price, total_price])
            products[product_name]['quantity'] -= qty  # Update stock in dictionary

            # Check if the product is out of stock
            if products[product_name]['quantity'] == 0:
                print(f"{product_name} is now out of stock.")

    # product code is not in inventory it will print a message
    else:
        print(f"Product '{code}' not found in store!")


# Sum of all the Quantity
table.add_row(["\n", "", "", ""])
table.add_row(["Total Quantity", total_quantity, "-", "-"])

# price before discounted
table.add_row(["Price", "-", "-", total1])

# Apply discount
discount = total1 * 5 / 100
total = total1 - discount
table.add_row(["Discount", "-", "-", -discount])
table.add_row(["Total", "-", "-", total])

# Print the bill
print("\n")
print("\n+------- Welcome to EasyCart Grocery Store -------+")
print(table)
print(f"\nYour Total Amount is: {total}")
print("\nThank you for Shopping\nHave a Nice Day")

# Update the CSV file with new quantities
# in this code it will automatically decrease the quantities from inventory
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as file:
    fieldnames = ['Product_Code', 'Product_Name', 'Price', 'Quantity']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for product_name, details in products.items():
        writer.writerow({
            'Product_Code': details['product_code'],
            'Product_Name': product_name,
            'Price': details['price'],
            'Quantity': details['quantity']
        })