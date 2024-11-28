class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f"Product Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}")
        return self





# Example Usage
if __name__ == "__main__":
    # Create products
    bread = Product(name="Bread", price=2.50, category="Food")
    milk = Product(name="Milk", price=3.00, category="Food")
    phone = Product(name="Phone", price=500.00, category="Electronics")

    # Create a store
    grocery_store = Store(name="Super Grocery")

    # Add products to the store
    grocery_store.add_product(bread).add_product(milk).add_product(phone)

    # Print all product info
    print("\nProducts in the store:")
    for product in grocery_store.products:
        product.print_info()

    # Sell a product
    print("\nSelling a product:")
    grocery_store.sell_product(0)  # Sell the product at index 0

    # Apply inflation
    print("\nApplying inflation:")
    grocery_store.inflation(0.10)  # Increase all prices by 10%

    # Apply clearance
    print("\nApplying clearance:")
    grocery_store.set_clearance("Food", 0.20)  # Discount food products by 20%

    # Print final product list
    print("\nFinal Products in the store:")
    for product in grocery_store.products:
        product.print_info()
