import game
import os
from time import sleep

clear = lambda: os.system("cls")

def main():
    #Intro screen
    print("Welcom to my rogue like game")
    print("Please select what you would like to do")
    print("1,New Game\n2,Load Save\n3,Exit")
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