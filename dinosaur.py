class Dinosaur:
    def __init__(self):
        self.name = ""
        self.attack_power = 25
        self.health = 50

    def attack(self,robot):
        robot.health -= self.attack_power
        print(f'explain what happened')    
        pass 