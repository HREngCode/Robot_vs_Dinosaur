class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        print(self.name)
        print(self.attack_power)
        print(self.health)

    def attack(self, robot):
        self.name = robot
        self.health -= self.attack_power
        print(f'explain what happened') 