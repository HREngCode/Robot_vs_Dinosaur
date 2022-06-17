from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Club", 10)

    def attack(self, dinosaur):
        self.name = dinosaur
        self.attack_power = self.active_weapon.attack_power
        self.health -= self.attack_power