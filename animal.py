class Animal:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(self.health)

class Dog(Animal):

    def __init__(self):
        super().__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):

    def __init__(self):
        super().__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(Animal):
        print("I am a Dragon")


cat1 = Animal("Tigger", 100)
cat1.run().display_health()