class Bike:

    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def display_info(self):
        print(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        print("Riding")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing")
        self.miles = self.miles - 5
        return self

bike1 = Bike(100, 20, 20)
bike2 = Bike(150, 22, 30)
bike3 = Bike(200, 25, 20)

bike1.ride().ride().ride().reverse().display_info()

bike2.ride().ride().reverse().reverse().display_info()

bike3.reverse().reverse().reverse().display_info()



