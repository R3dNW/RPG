__author__ = 'prabh_000'
from Prabhjots_libary import *
import random

players = {}
players_list = []
classes = ["Fighter", "Mage", "Archer", ]
classes1 = ["Class1 : Fighter", "Class2 : Mage", "Class3 : Archer"]
level = 1

class Players():
    name = ""
    player_class = ""
    level = 1
    hp = 0
    strength = 0
    attack = 0
    defense = 0
    speed = 0
    luck = 0
    combat_level = 0

    def __init__(self):
        name = ui_input("Name this player : ")
        border(inner_width=60, border_width=5, border_symbol="=")
        self.name = name

        ui("WARRIOR CLASSES", *classes1)
        player_class = ui_input("Pick a  Warrior Class [1-3]")
        check = validate_num(player_class)

        while check == "False":
            ui("Not a Number")
            player_class = ui_input("Pick a  Warrior Class [1-3]")
            check = validate_num(player_class)

        check = int(check)

        while check > 3 or check < 1:
            ui("Not Between 1 and 3")
            player_class = ui_input("Enter Again : ")
            check = player_class

        player_class = int(player_class)
        player_class -= 1
        player_class = classes[player_class]

        self.player_class = player_class

        if player_class == "Fighter":
            self.hp = self.level * 20
            self.strength = self.level * 5
            self.defense = self.level * 5
            self.attack = self.level * 2
            self.speed = self.level * 2
            self.luck = random.randint(1, 2)
            self.combat_level = self.strength + self.attack + self.defense
        elif player_class == "Mage":
            self.hp = self.level * 15
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 3
            self.luck = random.randint(2, 4)
            self.combat_level = self.strength + self.attack + self.defense
        elif player_class == "Archer":
            self.hp = self.level * 15
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 5
            self.luck = random.randint(1, 2)
            self.combat_level = self.strength + self.attack + self.defense
        else:
            ui("HUGE ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    def display_all_player_info(self):
        name = "Name : " + self.name
        level = "Level : " + str(self.level)
        player_class = "Class : " + self.player_class
        combat_level = "Combat level : " + str(self.combat_level)
        hp = "HitPoints : " + str(self.hp)
        strength = "Strength : " + str(self.strength)
        attack = "Attack : " + str(self.attack)
        defense = "Defense : " + str(self.defense)
        speed = "Speed : " + str(self.speed)
        ui_title(name)
        ui(player_class,
           level,
           combat_level,
           hp,
           strength,
           attack,
           speed,
           defense)


class Enemies():
    choices = ["norm", "miss", "crit"]
    hp = 0
    strength = 0
    attack = 0
    defence = 0

    def __init__(self, difficulty):
        self.hp = (difficulty * level) / 2
        print(players_list)
        self.strength = (players_list[0].strength / 4) * difficulty
        self.attack = difficulty
        self.defence = (players_list[0].strength / 4) * difficulty

    def hit(self):
        move = random.randint(0, 100)
        if move > 0 and move < 50:
            move = self.choices[0]  # norm hit
        elif move > 50 and move < 75:
            move = self.choices[1]  # miss hit
        elif move > 75 and move < 100:
            move = self.choices[2]  # crit hit

        target = players_list[random.randint(0, 3)]


class Floor():
    difficulty = random.randint(1, 3)
    enemies = []
    no_enemies = random.randint(4, 8)
    for enemy in range(0, no_enemies):
        enemies.append(Enemies(difficulty))
