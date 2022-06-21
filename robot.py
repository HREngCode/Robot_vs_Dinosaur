from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.check_if_alive = True
        self.active_weapon = Weapon("Club", 10)
        self.attack_power = (self.active_weapon.attack_power)

    def attack(self, dinosaur):
        self.health -= dinosaur
        return self.health


    def is_alive(self):
        if self.health > 0:
            self.check_if_alive == True
        else:
            self.check_if_alive == False