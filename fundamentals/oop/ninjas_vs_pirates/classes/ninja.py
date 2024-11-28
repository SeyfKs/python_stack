class Ninja:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, pirate):
        print(f"{self.name} attacks {pirate.name}!")
        pirate.health -= self.strength
        if pirate.health < 0:
            pirate.health = 0
        print(f"{pirate.name}'s health is now {pirate.health}.")
        return self

    def superPower(self, pirate):
        if self.health >= 20:  
            print(f"{self.name} uses SUPER POWER on {pirate.name}!")
            damage = self.strength * 2
            pirate.health -= damage
            self.health -= 20  
            if pirate.health < 0:
                pirate.health = 0
            print(f"{pirate.name}'s health is now {pirate.health}. {self.name}'s health is now {self.health}.")
        else:
            print(f"{self.name} doesn't have enough health to use the SUPER POWER!")
        return self
