class Product:

    def __init__(self, price, name, weight, brand, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self):
        self.price += self.price * .08
        return self
    
    def return_item(self):
        self.status = "returned"
        return self

    def display_info(self):
        print(self.price, self.name, self.weight, self.brand, self.status)


item1 = Product(10, "T-Shirt", "8 ounces", "Hanes", "for sale")




