class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        print(f"{new_product.name} has been added to {self.name}.")
        return self

    def sell_product(self, id):
        if 0 <= id < len(self.products):
            product = self.products.pop(id)
            print(f"Sold Product Info:")
            product.print_info()
        else:
            print(f"Invalid product ID: {id}. No product sold.")
        return self

    def inflation(self, percent_increase):
        print(f"Applying inflation: All prices will increase by {percent_increase * 100:.2f}%.")
        for product in self.products:
            product.update_price(percent_increase, is_increased=True)
        return self

    def set_clearance(self, category, percent_discount):
        print(f"Applying clearance: All {category} products will be discounted by {percent_discount * 100:.2f}%.")
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, is_increased=False)
        return self