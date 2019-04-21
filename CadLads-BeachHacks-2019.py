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
        enemy_ad_range = "20 - 30"
    else:
        enemy_hp = random.randint(65, 75)
        enemy_ad_range = "35 - 40"
    newline()
    print("\nYou are met with a {0}!\nEnemy HP = {1}\n"
          "Enemy AD Range = {2}\n\nBattle Options:\n1. Attack\n2. "
          "Bag\n3. Run".format(enemy_name[choose_enemy],
                                enemy_hp, enemy_ad_range))
    return enemy_name[choose_enemy]

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

def check_battle_over():
    conflict = is_conflict
    if conflict == 1:
        return True
    return False

def main():
    player = get_player_name()
    dungeon_enemies(dungeon)
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
            enemy_name = print_battle_options()
            choice = get_battle_option()
            battle(enemy_name)

main()
