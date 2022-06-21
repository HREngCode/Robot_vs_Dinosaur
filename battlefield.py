from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Sparky")
        self.dinosaur = Dinosaur("Rocky", 15)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('Welcome to the Main Event. This match is scheduled for one fall!')
        print("")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur.attack_power)
            print(f'{self.robot.name} lands a crushing shot with a total damage of {self.robot.attack_power}!!!')
            print(f'{self.dinosaur.name} gets knocked back and is now at  {self.dinosaur.health} health')
            print("")
            self.dinosaur.attack(self.robot.attack_power)
            print(f'{self.dinosaur.name} delivers a powerful blow causing a damage of {self.dinosaur.attack_power}!!') 
            print(f'{self.robot.name} takes a shot and is now at {self.robot.health} health')
            print("")

        self.display_winner()
                

    def display_winner(self):
        if self.dinosaur.health > 0:
            winner = self.dinosaur.name
            print(f'The winner of the match and new champion is {winner}')
            print("")

        else:
            winner = self.robot.name
            print(f'The winner of the match and new champion is {winner}')
            print("")