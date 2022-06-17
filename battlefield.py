from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot("Sparky")
        self.dinousaur = Dinosaur("Rocky", 10)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the Main Event. This match is scheduled for one fall!')

    def battle_phase(self):
        self.dinousaur.attack(self.robot)
        print(f'Robot in battlefield {self.robot.health}')
        self.robot.attack(self.dinousaur)
        print(f'Dinosaur in battlefield {self.dinousaur.health}')

    def display_winner(self):
        pass