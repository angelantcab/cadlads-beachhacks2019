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

player_hp = 125

def dungeon_map():
    dungeon = [[0, 0, 0], [0, 0, 0], [0, 0, 0],
               [0, 0, 0], [0, 0, 0], [0, 0, 0],
               [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(9):
        for j in range(3):
            dungeon[i][j] = random.randint(0, 1)
    return dungeon

def get_player_name():
    name = input("What is your name? ")
    return name

def is_conflict(conflict):
    if conflict == 0:
        return 0
    return 1

def get_enemy_name():
    enemy_name = ["Goblin", "Golem", "Giant Rat", "Troll", "Imp"]
    choose_enemy = random.randint(0, 4)
    name = enemy_name[choose_enemy]
    return name

def print_battle_options(enemy_name):
    if enemy_name == ("Goblin" or "Giant Rat" or "Imp"):
        enemy_hp = random.randint(30, 50)
        enemy_ad_range = "20 - 30"
    else:
        enemy_hp = random.randint(65, 75)
        enemy_ad_range = "35 - 40"
    newline()
    print("\nYou are met with a {0}!\nEnemy HP = {1}\n"
          "Enemy AD Range = {2}\n\nBattle Options:\n1. Attack\n2. "
          "Bag\n3. Run".format(enemy_name,
                                enemy_hp, enemy_ad_range))

def get_battle_option():
    choice = input("Enter your choice: ")
    return choice

def battle(enemy):
    print_battle_options()
    choice = get_battle_option()
    player_ad = random.randint(20, 25)
    if choice == 1:
        print("You attack {0} for {1} damage!".format(enemy,
                                                      player_ad))
    elif choice == 2:
        if len(bag) == 0:
            print("You have nothing in your bag.")
        else:
            print("In Bag:")
            for i in bag:
                print(i)
    elif choice == 3:
        print("You attempt to run away.")

def main():
    player = get_player_name()
    dungeon = dungeon_map()
    print(dungeon)
    corridor = 0
    area = 0
    room = dungeon[corridor][area]
    system = True
    while system:
        fight = is_conflict(room)
        if fight == 0:
            if area == 2:
                corridor += 1
                area = 0
            else:
                area += 1
        else:
            enemy_name = get_enemy_name()
            print_battle_options(enemy_name)
            choice = get_battle_option()
            battle(enemy_name)

main()
