class Pirate:
    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, ninja):
        print(f"{self.name} attacks {ninja.name}!")
        ninja.health -= self.strength
        if ninja.health < 0:
            ninja.health = 0
        print(f"{ninja.name}'s health is now {ninja.health}.")
        return self

    def superPower(self, ninja):
        if self.health >= 20: 
            print(f"{self.name} uses SUPER POWER on {ninja.name}!")
            damage = self.strength * 2
            ninja.health -= damage
            self.health -= 20 
            if ninja.health < 0:
                ninja.health = 0
            print(f"{ninja.name}'s health is now {ninja.health}. {self.name}'s health is now {self.health}.")
        else:
            print(f"{self.name} doesn't have enough health to use the SUPER POWER!")
        return self
