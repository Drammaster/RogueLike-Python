import game
import os
from time import sleep

clear = lambda: os.system("cls")

def main():
    #Intro screen
    print("Welcom to my rogue like game")
    print("Please select what you would like to do")
    print("1,Start\n2,Exit")
    enter = input("Choice:")
    enter = int(enter)
    if enter == 1:
        clear()
        sleep(5)
        game.start()
        clear()
        main()
    elif enter == 2:
        return()
    

main()