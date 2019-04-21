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

dungeon = [[0, 0, 0], [0, 0, 0], [0, 0, 0],
           [0, 0, 0], [0, 0, 0], [0, 0, 0],
           [0, 0, 0], [0, 0, 0], [0, 0, 0]]

player_hp = 100
player_ad = 25

enemy_hp = 80
enemy_ad = 20

def dungeon_enemies(map):
    for corridor in map:
        for room in corridor:
            room = random.randint(0, 1)

def get_player_name():
    name = input("What is your name? ")
    return name

def is_conflict(conflict):
    if conflict == 0:
        return 0
    return 1

def print_battle_options():
    enemy_name = ["Goblin", "Golem", "Troll", "Giant Rat",
                  "Dragon", "Imp"]
    choose_enemy = random.randint(0, 5)
    print("You are met with a {0}!\nEnemy Health = {1}\n"
          "Enemy Damage = {2}\n\nBattle Options:\n1. Attack\n2. "
          "Bag\n3. Run".format(enemy_name[choose_enemy],
                                enemy_hp, enemy_ad))

print_battle_options()

def get_battle_option():
    choice = input("Enter your choice: ")
    return choice

'''
def battle():
    print_battle_options()
    choice = get_battle_option():
    if choice == 1:
        if
'''

Enters room
def options() :
    conflict
        print("Defeat enemies)
    
    move on
        print("Find the next room")
              
Next room
def options() :
