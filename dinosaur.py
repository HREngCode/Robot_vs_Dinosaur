
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.check_if_alive = True
        self.health = 100
    def attack(self):
        self.health -= self.attack_power

    def is_alive(self):
        if self.health > 0:
            self.check_if_alive == True
        else:
            self.check_if_alive == False
