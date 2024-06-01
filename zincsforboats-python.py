import csv

# Function to load products from a CSV file
def load_products(csv_file_path):
    products = {}
    with open(csv_file_path, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row
        for rows in reader:
            product_name = rows[0].strip().lower()
            product_url = rows[1].strip()
            products[product_name] = product_url
    return products

# Function to find product URL by name
def find_product_url(product_name, products):
    return products.get(product_name.lower())

# Load products from CSV
csv_file_path = 'products.csv'  # Path to your CSV file
products = load_products(csv_file_path)

# Example search
product_name = "4 1/4 shaft anode"
product_url = find_product_url(product_name, products)
print(product_url)  # Output: https://zincsforboats.com/products/4-1-4-shaft-anode
