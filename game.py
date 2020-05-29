import enemy
import character
import os
from time import sleep

clear = lambda: os.system("cls")

def start():
    #Intro
    print("welcome to the end of the world")
    sleep(2)
    print("Inventory:\nHand Gun: 2 DMG\nAmmo: 5\nRusty Butter Knife: 1 DMG")
    sleep(1)
    print("You must now go for as long as you can. Good luck!")
    sleep(5)
    clear()

    #Establish basics for turns
    turns = 0
    status = "alive"
    mHealth = 1
    #Game loop
    while status == "alive":
        mob = enemy.zombie()
        mHealth = mob[1]
        print("A", mob[0], "has appeared infront of you!!!")
        sleep(2)
        print("1,Shoot\n2,Stab")
        while status == "alive" and mHealth > 0:
            action = int(input("Action:"))
            if action == 1:
                mHealth -= 2
                print(mHealth)
            elif action == 2:
                mHealth -= 1
                print(mHealth)
            else:
                print("You can't do that.")
        turns += 1
    print("You have survived", turns, "encounters")