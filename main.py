import game
import os
from time import sleep

clear = lambda: os.system("cls")

def main():
    #Intro screen
    print("Welcom to my rogue like game")
    print("Please select what you would like to do")
    sleep(0.5)
    print("1, New Game")
    sleep(0.5)
    print("2, Load Game")
    sleep(0.5)
    print("3, Exit Game")
    sleep(0.5)
    enter = input("Choice:")
    enter = int(enter)
    if enter == 1: #New Game
        clear()
        sleep(2)
        game.start()
        clear()
        main()
    elif enter == 2: #Load Game
        pass
    elif enter == 3: #Exit option
        return()
    

main()