class Car:

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print("Price:", self.price, "Speed:", self.speed, "Fuel:", self.fuel, "Mileage:", self.mileage)

car1 = Car(2000, 95, "full", "75mpg")
car2 = Car(2500, 120, "empty", "80mpg")
car3 = Car(3000, 130, "3/4 full", "35mpg")
car4 = Car(4000, 100, "1/2 full", "50mpg")
car5 = Car(1000, 105, "full", "40mpg")
car6 = Car(5000, 110, "full", "100mpg")


