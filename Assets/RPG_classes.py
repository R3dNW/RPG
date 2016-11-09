import random
from Prabhjots_library import *

__author__ = 'prabh_000'

players = {}
players_list = []
classes = ["Fighter", "Mage", "Archer", ]
classes1 = ["Class1 : Fighter", "Class2 : Mage", "Class3 : Archer"]
level = 1


class Enemies:
    choices = ["norm", "miss", "crit"]
    hp = 0
    strength = 0
    attack = 0
    defence = 0

    def __init__(self, difficulty):
        self.hp = (difficulty * level) / 2
        print(players_list)
        self.strength = (5 / 4) * difficulty
        self.attack = difficulty
        self.defence = (5 / 4) * difficulty

    def hit(self):
        move = random.randint(0, 100)
        if move > 0 and move < 50:
            move = self.choices[0]  # norm hit
        elif move > 50 and move < 75:
            move = self.choices[1]  # miss hit
        elif move > 75 and move < 100:
            move = self.choices[2]  # crit hit

        target = players_list[random.randint(0, 3)]


class Floor:
    difficulty = 0
    enemies = []
    no_enemies = 0

    def __init__(self):
        difficulty = random.randint(1, 3)
        enemies = []
        no_enemies = random.randint(4, 8)
        for i in range(0, no_enemies):
            enemies.append(Enemies(difficulty))
