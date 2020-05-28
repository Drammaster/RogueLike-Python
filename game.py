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

    #Game loop
    while status == "alive":
        print("A zombie has appeared infront of you!!!")
        sleep(2)
        print("1,Shoot\n2,Stab")

        action = int(input("Action:"))
        if action == 1:
            pass
        elif action == 2:
            pass
        else:
            print("You can't do that.")
        turns += 1
    print("You have survived", turns, "encounters")