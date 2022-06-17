from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot("Sparky")
        self.dinousaur = Dinosaur("Rocky", 10)
        self.robot_name = self.robot.name
        self.dinousaur_name = self.dinousaur.name

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the Main Event. This match is scheduled for one fall!')

    def battle_phase(self):
        while self.robot.health > 0 or self.dinousaur.health > 0:
            self.robot.attack(self.dinousaur)
            print(f'{self.robot_name} has taken a crushing blow and is at  {self.robot.health} health')
            print("")
            self.dinousaur.attack(self.robot)
            print(f'{self.dinousaur_name} has taken quite a shot and is at  {self.dinousaur.health} health')
            print("")

    def display_winner(self):
        pass