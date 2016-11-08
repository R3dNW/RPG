import time
import random
from Prabhjots_libary import *


new_page()

level = 1
classes = ["Class1 : Fighter", "Class2 : Mage", "Class3 : Archer", ]
players = {}


class Floor():
    dificulty = random.randint(1,3)
    enemies = []
    no_enemies = random.randint(0,)


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
    combat_level = strength + attack + defense

    def __init__(self):
        name = ui_input("Name this player : ")
        self.name = name
        ui("WARRIOR CLASSES", *classes)
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
        if player_class == "Class1 : Fighter":
            self.hp = self.level * 20
            self.strength = self.level * 5
            self.defense = self.level * 5
            self.attack = self.level * 2
            self.speed = self.level * 2
            self.luck = random.randint(1, 2)
        elif player_class == "Class2 : Mage":
            self.hp = self.level * 9
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 3
            self.luck = random.randint(2, 4)
        elif player_class == "Class3 : Archer":
            self.hp = self.level * 9
            self.strength = self.level * 2
            self.defense = self.level * 2
            self.attack = self.level * 5
            self.speed = self.level * 5
            self.luck = random.randint(1, 2)
        else:
            ui("HUGE ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    def display_all_player_info(self):
        name = "Name : " + self.name
        level = "Level : " + str(self.level)
        combat_level = "Combat level : " + str(self.combat_level)
        hp = "HitPoints : " + str(self.hp)
        strength = "Strength" + str(self.strength)
        attack = "Attack : " + str(self.attack)
        defense = "Defense" + str(self.defense)
        speed = "Speed : " + str(self.speed)
        ui_title(name)
        ui(level,
           combat_level,
           hp,
           strength,
           attack,
           speed,
           defense)


def validate_num(num):
    try:
        num = int(num)
        return int(num)
    except ValueError:
        return "False"


def start():
    new_page()
    ui_title("Welcome to THE UNDER WORLD!!!")
    ui("[N] Any number to Play",
       "[L] Any letter to Quit")
    try:
        next = ui_input("Pick a choice")
    except ValueError:
        ui("Too Scared? Goodbye")
        quit()
    generate_players()


def generate_players():
    new_page()
    ui("Make and name your Players")
    player1 = Players()
    ui("Player Made")
    player2 = Players()
    ui("Player Made")
    player3 = Players()
    ui("Player Made")
    player4 = Players()
    ui("Player Made")
    players["player1"] = player1
    players["player2"] = player2
    players["player3"] = player3
    players["player4"] = player4

start()

