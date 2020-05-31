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
        sleep(0.5)
        print(items.item_name(i[0]))
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
            print(action_number, ",", items.item_name(i[0]))
        print("Player health:", player_health)
        print(str(mob[0]) + " health:", mob_health)

        #Begin Combat
        while player_health > 0 and mob_health > 0:
            action = int(input("Action:")) #User Action
            
            if action <= action_number and action > 0: #Check action is doable
                if player_inventory[action-1][1] > 0: #Check item can still be used
                    effect = items.item_effect(player_inventory[action-1][0]) #Load Item effect
                    
                    if effect[0] == "ranged":
                        mob_health -= effect[1]
                        player_health -= mob_attack
                        player_inventory[action-1][1] -= 1
                        sleep(0.5)

                    elif effect[0] == "melee":
                        mob_health -= effect[1]
                        player_health -= mob_attack * 2
                        player_inventory[action-1][1] -= 2
                        sleep(0.5)

                    elif effect[0] == "heal":
                        player_health += effect[1]
                        player_health -= mob_attack
                        player_inventory[action-1][1] -= 1
                        sleep(0.5)
                    
                    #Update Health
                    print("\033[A                             \033[A")
                    print("\033[A                             \033[A")
                    print("\033[A                             \033[A")
                    print("Player health:", player_health)
                    print(mob[0], "health:", mob_health)
                    sleep(0.5)

                else:
                    print("You don't have anymore of this item")
            
            else: #Invalid index exceptionb handler
                print("You can't do that.")
                print("")
                sleep(2)
                print("\033[A                             \033[A")
                print("\033[A                             \033[A")
                print("\033[A                             \033[A")
          
        turns += 1
        clear()
    print("You have survived", turns, "encounters")
    sleep(10)