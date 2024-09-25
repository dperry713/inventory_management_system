class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Getters
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_quantity(self, quantity):
        self.__quantity = quantity

    def update_quantity(self, quantity):
        self.__quantity += quantity

    def __str__(self):
        return f"ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price}, Quantity: {self.__quantity}"

def load_inventory(filename):
    inventory = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                product_id, name, price, quantity = line.strip().split(',')
                inventory[product_id] = Product(product_id, name, float(price), int(quantity))
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")
    return inventory

def save_inventory(filename, inventory):
    with open(filename, 'w') as file:
        for product in inventory.values():
            file.write(f"{product.get_product_id()},{product.get_name()},{product.get_price()},{product.get_quantity()}\n")

def add_product(inventory):
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    inventory[product_id] = Product(product_id, name, price, quantity)
    print("Product added successfully.")

def update_stock(inventory):
    product_id = input("Enter product ID to update: ")
    if product_id in inventory:
        quantity = int(input("Enter quantity to add: "))
        inventory[product_id].update_quantity(quantity)
        print("Stock updated successfully.")
    else:
        print("Product not found.")

def process_sale(inventory):
    total_sales = 0
    while True:
        product_id = input("Enter product ID to sell (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        if product_id in inventory:
            quantity = int(input("Enter quantity to sell: "))
            if inventory[product_id].get_quantity() >= quantity:
                inventory[product_id].update_quantity(-quantity)
                total_sales += inventory[product_id].get_price() * quantity
                print("Sale processed successfully.")
            else:
                print("Insufficient stock.")
        else:
            print("Product not found.")
    print(f"Total sales: ${total_sales}")

def main():
    inventory = load_inventory('inventory.txt')
    while True:
        print("\n1. Add Product\n2. Update Stock\n3. Process Sale\n4. Save and Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_product(inventory)
            elif choice == '2':
                update_stock(inventory)
            elif choice == '3':
                process_sale(inventory)
            elif choice == '4':
                save_inventory('inventory.txt', inventory)
                print("Inventory saved. Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
