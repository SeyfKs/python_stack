class Pet:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.energy = 50
        self.health = 50

    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s Energy: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s Energy: {self.energy}")
        print(f"{self.name}'s health: {self.health}")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name}'s health: {self.health}")
        return self

    def noise(self):
        print(f"The {self.type} named {self.name} makes a sound: {self.sound}")
        return self


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}.")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name} some {self.pet_food}.")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()
        return self



pet_nibbles = Pet(name="Mr.Nibbles", type="dog", sound="bark")

ninja_john = Ninja(first_name="John", last_name="Claude", treats="Meat", pet_food="dog food", pet=pet_nibbles)

ninja_john.walk().feed().bathe()



