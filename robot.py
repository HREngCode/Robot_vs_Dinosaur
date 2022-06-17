from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Club", 10)

    def attack(self, dinosaur):
        dinosaur = self.name
        self.attack_power = self.active_weapon.attack_power
        self.health -= self.attack_power
        print(f'{dinosaur} is really dishing out punishment!!') 
        print("")