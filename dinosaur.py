
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.check_if_alive = True

    def attack(self, robot):
        self.health -= robot

    def is_alive(self):
        if self.health > 0:
            self.check_if_alive == True
        else:
            self.check_if_alive == False
