# EasyCart-Billing-System

## Project Overview:
The EasyCart Grocery Store application is a console-based tool designed to simulate a shopping experience.  You can enter items by entering product codes '@01, @02,----', specify the desired quantity, and receive an automatically generated bill. The application manages inventory in real time by updating a CSV file, ensuring the store’s stock is always up-to-date. It also generates detailed bills that include discounts, itemized purchases, and total quantities.

## Features:

1. Real-time Inventory Management: Automatically updates product quantities in the CSV file after each transaction.
2. CSV Data Integration: The application reads and writes data to a CSV file that stores product details like product codes, names, prices, and quantities.
3. Billing System: This system generates a detailed bill, calculates total quantities and prices, and applies a discount to the final amount.
4. Out-of-Stock Notification: Notifies users when an item is out of stock and shows available quantities for each product.
5. Sample Output: A console-based bill summary that displays the purchased items, total quantities, prices, and discounts.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/VaibhavGovindwar/EasyCart-Billing-System.git
   ```

2. Navigate to the project directory:
   ```bash
   cd EasyCart-Billing-System
   ```

3. Install the required dependency:
   ```bash
   pip install prettytable
   ```
   ```bash
   pip install csv
   ```
4. Add the Inventory CSV: Ensure the Grocery_list.csv file (formatted as shown below) is present in the project directory.
   
5. Run the program:
   ```bash
   python EasyCart-Billing-System.py
   ```
   
## Sample Dataset (CSV): The Grocery_list.csv file should contain the following format:
```
Product_Code,Product_Name,Price,Quantity
@01,Ariel Detergent,110.0,30
@02,Ariel Liquid,150.0,35
@03,Body Lotion,99.0,40
@04,Bread,49.0,40
@05,Coco-Cola,25.0,28
```
- This file serves as the inventory data, which gets updated dynamically as products are purchased.
- You can customize the dataset according to your requirements of product or you can update the inventory products 

## Sample output: 
```
------ Billing System ------
Enter Product Code (or 'q' to quit): @23
Enter Quantity : 2
Enter Product Code (or 'q' to quit): @13
Enter Quantity : 1
Enter Product Code (or 'q' to quit): @14
Enter Quantity : 24
Enter Product Code (or 'q' to quit): @04
Enter Quantity : 2
Enter Product Code (or 'q' to quit): @26
Enter Quantity : 1
Enter Product Code (or 'q' to quit): @29
Enter Quantity : 1
Enter Product Code (or 'q' to quit): q



+------- Welcome to EasyCart Grocery Store -------+
+----------------+----------+-------+-------------+
|  Product Name  | Quantity | Price | Total Price |
+----------------+----------+-------+-------------+
|   Ice-Cream    |    2     |  45.0 |     90.0    |
|    DishWash    |    1     |  35.0 |     35.0    |
|      Eggs      |    24    |  6.5  |    156.0    |
|     Bread      |    2     |  49.0 |     98.0    |
|      Milk      |    1     |  30.0 |     30.0    |
|  Nestle Coffe  |    1     | 698.0 |    698.0    |
|                |          |       |             |
|                |          |       |             |
| Total Quantity |    31    |   -   |      -      |
|     Price      |    -     |   -   |    1107.0   |
|    Discount    |    -     |   -   |    -55.35   |
|     Total      |    -     |   -   |   1051.65   |
+----------------+----------+-------+-------------+

Your Total Amount is: 1051.65

Thank you for Shopping
Have a Nice Day

```

## Technologies Used
- **Python**: Core logic for the billing system.
- **PrettyTable**: For displaying the itemized bill in a tabular format.
- **CSV**: create a dataset to automate entering the product name
  
## Future Enhancements:

1. Add a graphical user interface (GUI) to improve user experience.
2. Implement search functionality for easier product lookup.
3. Introduce user accounts to save purchase history and preferences.
4. Develop an admin panel for managing inventory and sales data.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request to suggest improvements or fix bugs.

## License: 
This project is licensed under the MIT License. See the LICENSE file for more details.

