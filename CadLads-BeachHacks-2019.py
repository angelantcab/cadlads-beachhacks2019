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

player_hp = 125
player_ad = 25

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
    enemy_name = ["Goblin", "Golem", "Giant Rat", "Troll", "Imp"]
    choose_enemy = random.randint(0, 4)
    if choose_enemy % 2 == 0 :
        enemy_hp = random.randint(30, 50)
        enemy_ad = random.randint(20, 30)
        enemy_ad_range = "20 - 30"
    else:
        enemy_hp = random.randint(65, 75)
        enemy_ad = random.randint(35, 40)
        enemy_ad_range = "35 - 40"
    newline()
    print("\nYou are met with a {0}!\nEnemy HP = {1}\n"
          "Enemy AD Range = {2}\n\nBattle Options:\n1. Attack\n2. "
          "Bag\n3. Run".format(enemy_name[choose_enemy],
                                enemy_hp, enemy_ad_range))

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
