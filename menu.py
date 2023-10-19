# menu.py
import os
import pyfiglet


def clear_screen():
    try:
        os.system("clear")
    except:
        console.clear()


def menu():
    clear_screen()
    title = pyfiglet.figlet_format("Yahtzee")
    print(title)
    print()
    print("1) Play Yahtzee!")
    print("2) High Scores")
    print("--------------------")
    print("8) Reset High Scores")
    print("9) Quit")
    print()
    selection = input("> ")
    if selection == "1":
        input("Loading game... ")
    elif selection == "2":
        input("Loading scores...")
    elif selection == "8":
        input("Resetting scores...")
    elif selection == "9":
        input("Quiting...")
    else:
        print("Invalid command!")
    menu()


menu()
