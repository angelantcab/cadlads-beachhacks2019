# Cabral, Angel
# Docuyanan, Dillon
# Lopez, Michael
# 4/20/19

# CadLads - BeachHacks 2019

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random

def newline():
    print("\n----------------------------")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

room = random.randint(0, 1)

dungeon = [[room, room, room], [room, room, room], [room, room, room],
           [room, room, room], [room, room, room], [room, room, room],
           [room, room, room], [room, room, room], [room, room, room]]

def get_player_name():
    name = input("What is your name? ")
    return name

def is_conflict(conflict):
    if conflict == 0:
        return 0
    return 1

def print_battle_options():
    print("Fight Options\n\n1. Attack\n2. Bag\n3. Run")

def get_battle_option():
    choice = input("Enter your choice: ")
    return choice

def battle():
    print_battle_options()
    choice = get_battle_option():
    if choice == 1:
        
