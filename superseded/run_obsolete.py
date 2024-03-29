import data
import os
from datetime import datetime

data.create_table()


def clear_screen():
    try:
        os.system("clear")
    except:
        console.clear()


while True:
    clear_screen()
    print("1) Input an entry")
    print("2) View all entries")
    print("9) Quit")
    selection = input("Enter your selection: ")
    if selection == "1":
        date = datetime.today().strftime("%Y-%m-%d %H:%M")
        user = input("Enter your name: ")
        score = input("Enter your score: ")
        data.insert_data(date, user, score)
    elif selection == "2":
        result = data.select_all_data()
        counter = 1
        print("")
        print("High Scores")
        print("")
        for row in result:
            print(f"{counter}) {row[0]} {row[1]} {row[2]}")
            counter += 1
        input("...")
    elif selection == "9":
        data.close_connection()
        input("Goodbye...")
        quit()
    else:
        input("Invalid selection.")
