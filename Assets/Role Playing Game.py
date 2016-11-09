__author__ = 'prabh_000'

import time
import random
from Prabhjots_library import *
from RPG_classes import *
from Player import Player


with open("ITEMS.txt", "r") as f:
    file = f.read()
items = file.split("\n")
for i in range(0, len(items)):
    items[i] = items[i].split(",")
print(items)

new_page()




def generate_players():
    new_page()
    ui("Make and name your Players")
    player1 = Player()
    print("")
    ui("PLAYER 2")
    player2 = Player()
    print("")
    ui("PLAYER 3")
    player3 = Player()
    print("")
    ui("PLAYER 4")
    player4 = Player()
    player1.display_all_player_info()
    players["player1"] = player1
    players["player2"] = player2
    players["player3"] = player3
    players["player4"] = player4
    players_list.append(player1)
    players_list.append(player2)
    players_list.append(player3)
    players_list.append(player4)


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


start()


def game():
    dungeon = Floor()


game()