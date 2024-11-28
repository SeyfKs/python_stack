from classes.product import Product
from classes.store import Store

if __name__ == "__main__":
    bread = Product(name="Bread", price=2.50, category="Food")
    milk = Product(name="Milk", price=3.00, category="Food")
    phone = Product(name="Phone", price=500.00, category="Electronics")
    grocery_store = Store(name="Super Grocery")

    print("\nProducts in the store:")
    for product in grocery_store.products:
        product.print_info()


    print("\nSelling a product:")
    grocery_store.sell_product(0)  


    print("\nApplying inflation:")
    grocery_store.inflation(0.10)  

    print("\nApplying clearance:")
    grocery_store.set_clearance("Food", 0.20)  

    print("\nFinal Products in the store:")
    for product in grocery_store.products:
        product.print_info()