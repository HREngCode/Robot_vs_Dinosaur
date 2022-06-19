from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Sparky")
        self.dinousaur = Dinosaur("Rocky", 15)
        self.robot_name = self.robot.name
        self.dinousaur_name = self.dinousaur.name

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('Welcome to the Main Event. This match is scheduled for one fall!')
        print("")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinousaur.health > 0:
            self.dinousaur.attack()
            print(f'{self.dinousaur.name} delivers a powerful blow!!') 
            print("")
            print(f'{self.robot_name} takes a shot and is at  {self.robot.health} health')
            print("")
            self.robot.attack()
            print(f'{self.robot.name} lands a crushing shot!!!') 
            print("")
            print(f'{self.dinousaur_name} gets knocked back and is at  {self.dinousaur.health} health')
            print("")

        if self.dinousaur.health > 0:
            winner = self.dinousaur.name
            print(f'The winner of the match and new champion is {winner}')
            print("")

        else:
            winner = self.robot.name
            print(f'The winner of the match and new champion is {winner}')
            print("")
                
        # return winner

    # def display_winner(self):
    #     print(f'The winner of the match and new champion is {winner}')