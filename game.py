import enemy
import character
import items
import os
from time import sleep

clear = lambda: os.system("cls")

def start():
    #Establish player
    player = character.establish_player()
    player_health = player[0]
    player_inventory = player[1]

    #Intro
    print("welcome to the end of the world")
    sleep(2)
    print("Inventory:")
    for i in player_inventory:
        print(items.item_name(i))
    sleep(1)
    print("You must now go for as long as you can. Good luck!")
    sleep(5)
    clear()

    #Establish basics for turns
    turns = 0

    #Game loop
    while player_health > 0:
        #Establish enemy
        mob = enemy.zombie()
        mob_health = mob[1]
        mob_attack = mob[2]

        print("A", mob[0], "has appeared infront of you!!!")
        sleep(2)
        
        #Show player action options
        print("Inventory:")
        action_number = 0
        for i in player_inventory:
            action_number += 1
            print(action_number, ",", items.item_name(i))
        

        while player_health > 0 and mob_health > 0:
            action = int(input("Action:"))
            
            if action <= action_number and action > 0:
                effect = items.item_effect(player_inventory[action-1])
                
                if effect[0] == "damage":
                    mob_health -= effect[1]
                    player_health -= mob_attack
                    sleep(1)
                elif effect[0] == "heal":
                    player_health += effect[1]
                    player_health -= mob_attack
                    sleep(1)
                
                print("Player health:", player_health)
                print(mob[0], "health:", mob_health)
                sleep(3)
            
            else:
                print("You can't do that.")
                print("")
                sleep(2)
            
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")
        turns += 1
    print("You have survived", turns, "encounters")
    sleep(10)