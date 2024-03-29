# yatzee.py


import random
import os
import data
from datetime import date
import pyfiglet

try:
    import console
except:
    pass


def clear_screen():
    try:
        os.system("clear")
    except:
        console.clear()


no_of_dice = 6
rolled_dice = []
display_list = ["A", "B", "C", "D", "E"]
no_of_rolls = 0
saved_dice = []
# total_upper_score = None
# total_lower_score = None
a = None
b = None
c = None
d = None
e = None
f = None
g = None
h = None
i = None
j = None
k = None
l = None
m = None
n = None
# user_scores = [a,b,c,d,e,f]


def clear_screen():
    try:
        os.system("clear")
    except:
        console.clear()


def roll_dice(no_of_dice):
    all_rolls = []
    for dice in range(no_of_dice):
        roll = random.randint(1, 6)
        all_rolls.append(roll)
    return all_rolls


def insert_dummy_data():
    users_name = input("Please enter your name: ")
    fake_user_name = users_name[0:9]
    fake_score = input("Enter your score: ")
    if int(fake_score) > 0 and int(fake_score) < 1000:
        save_high_score(fake_score, fake_user_name)
    else:
        input("What the f#!& was that!")
        insert_dummy_data()


def display_high_scores():
    try:
        high_scores = data.select_all_data()
        print(f"DATE       SCORE        NAME      ")
        for score in high_scores:
            # score[o] = date
            # score[1] = name
            # score[2] = score
            print(f"{score[0]} --{score[2]} ------ {score[1]}")
        input("Press a key to continue...")
        menu()
    except:
        menu()


def reset_high_scores():
    data.delete_table()
    data.create_table()


def menu():
    clear_screen()
    title = pyfiglet.figlet_format("Yahtzee")
    print(title)
    print()
    print("1) Play Yahtzee!")
    print("2) High Scores")
    print("--------------------")
    print("8) Reset Scores")
    print("9) Quit")
    print()
    selection = input("> ")
    if selection == "1":
        input("Loading game... ")
        play()
    elif selection == "2":
        input("Loading scores...")
        display_high_scores()
    elif selection == "3":
        insert_dummy_data()
    elif selection == "8":
        input("Resetting scores...")
        reset_high_scores()
    elif selection == "9":
        data.close_connection()
        quit()
    else:
        input("Invalid command!")
    menu()


def play():
    global saved_dice
    global no_of_rolls
    clear_screen()
    display_scores(title=True)
    input("Press a key to roll dice...")
    no_of_dice_to_reroll = 5 - len(saved_dice)
    result = roll_dice(int(no_of_dice_to_reroll))
    no_of_rolls += 1
    result.extend(saved_dice)
    saved_dice = []
    input(f"Result: {result}")
    letters = "ABCDE"
    for index, dice in enumerate(result):
        print(f"{letters[index]}: {dice}")
    # print("Would you like to keep any of the dice?")
    if no_of_rolls <= 2:
        for letter in letters:
            choice = input(f"Keep '{letter}'? (y/n): ")
            if choice == "y" or choice == "Y":
                letter_index = letters.index(letter)
                value = result[letter_index]
                dice_to_keep(letter_index, value)
    else:
        for letter in letters:
            letter_index = letters.index(letter)
            value = result[letter_index]
            dice_to_keep(letter_index, value)
    print(f"The dice that you have saved are: {saved_dice}")
    if no_of_rolls >= 3:
        add_score()
    else:
        choice2 = input("Would you like to keep rolling? (y/n)")
        if choice2 == "y" or choice2 == "Y":
            play()
        else:
            add_score()


def add_score():
    global saved_dice
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n
    display_scores(title=False)
    # print(score_sheet)
    choice = input("What item do you want to add your values to? (a-n) ")
    if choice == "a" and a == None:
        a = 0
        for number in saved_dice:
            if number == 1:
                a += 1
    elif choice == "b" and b == None:
        b = 0
        for number in saved_dice:
            if number == 2:
                b = b + 2
    elif choice == "c" and c == None:
        c = 0
        for number in saved_dice:
            if number == 3:
                c = c + 3
    elif choice == "d" and d == None:
        d = 0
        for number in saved_dice:
            if number == 4:
                d = d + 4
    elif choice == "e" and e == None:
        e = 0
        for number in saved_dice:
            if number == 5:
                e = e + 5
    elif choice == "f" and f == None:
        f = 0
        for number in saved_dice:
            if number == 6:
                f = f + 6

### lower scores ###

    elif choice == "g" and g == None:  # 3 of a kind --> Done!
        g = 0
        for number in range(1, 6):
            if saved_dice.count(number) >= 3:
                dice_with_three = number
        g = 3 * dice_with_three
    elif choice == "h" and h == None:  # 4 of a kind --> Done!
        h = 0
        for number in range(1, 6):
            if saved_dice.count(number) >= 4:
                h = 4 * number
    elif choice == "i" and i == None:  # Full house --> NOT DONE !!!
        i = 0
        two_values = list(dict.fromkeys(saved_dice))  # removes duplicates
        if len(two_values) == 2:
            # input("There are only two values in this list! Good job")
            valueA = 0
            valueB = 0
            saved_dice = sorted(saved_dice)
            for dice in saved_dice:
                if dice == two_values[0]:
                    valueA += 1
                elif dice == two_values[1]:
                    valueB += 1
            if valueA == 2 and valueB == 3:
                # input("scenario A successful")
                i = 25
            elif valueA == 3 and valueB == 2:
                # input("scenario B successful")
                i = 25
        else:
            pass

    elif choice == "j" and j == None:  # long straight --> Done!
        j = 0
        saved_dice = list(dict.fromkeys(saved_dice))  # removes duplicates
        saved_dice_long = sorted(saved_dice)
        if saved_dice_long[0] == 1:
            if saved_dice_long[1] == 2 and saved_dice_long[2] == 3 and saved_dice_long[3] == 4 and saved_dice_long[4] == 5:
                j = 40
        elif saved_dice_long[0] == 2:
            if saved_dice_long[1] == 3 and saved_dice_long[2] == 4 and saved_dice_long[3] == 5 and saved_dice_long[4] == 6:
                j = 40
    elif choice == "k" and k == None:  # short straight --> Done!
        k = 0
        saved_dice = list(dict.fromkeys(saved_dice))  # removes duplicates
        saved_dice = sorted(saved_dice)
        if saved_dice[0] == 1:
            # input(saved_dice)
            if saved_dice[1] == 2 and saved_dice[2] == 3 and saved_dice[3] == 4:
                k = 30
                # input("short straight A achieved")
        elif saved_dice[0] == 2:
            input(saved_dice)
            if saved_dice[1] == 3 and saved_dice[2] == 4 and saved_dice[3] == 5:
                k = 30
        elif saved_dice[0] == 3:
            input(saved_dice)
            if saved_dice[1] == 4 and saved_dice[2] == 5 and saved_dice[3] == 6:
                k = 30
    elif choice == "l" and l == None:  # Yatzee! --> Done!
        l = 0
        for number in range(1, 6):
            if saved_dice.count(number) >= 5:
                l = 50
    elif choice == "m" and m == None:  # chance --> Done!
        m = 0
        m = sum(saved_dice)
    elif choice == "n":  # Bonus Yatzee! --> Done!
        for number in range(1, 6):
            if saved_dice.count(number) >= 5:
                n = n + 100
    else:
        input("Wrong selection. Try again")
        add_score()
    display_scores(title=False)
    reset_dice()


def reset_dice():
    global saved_dice
    global no_of_rolls
    saved_dice = []
    no_of_rolls = 0
    clear_screen()
    play()


def save_high_score(score, name):
    data.create_table()
    today = date.today()
    str_today = str(today)
    data.insert_data(str_today, name, score)


def display_scores(title):
    global n
    if title == True:
        print("Yahtzee!!!")
    else:
        pass
    print("")
    print("Upper scores:")
    print("")
    print(f"a) 1s score: {a}")
    print(f"b) 2s score: {b}")
    print(f"c) 3s score: {c}")
    print(f"d) 4s score: {d}")
    print(f"e) 5s score: {e}")
    print(f"f) 6s score: {f}")
    print()
    print("Lower Scores:")
    print("")
    print(f"g) 3 of a kind: {g}")
    print(f"h) 4 of a kind: {h}")
    print(f"i) full house: {i}")
    print(f"j) long straight: {j}")
    print(f"k) short straight: {k}")
    print(f"l) Yatzee: {l}")
    print(f"m) Chance: {m}")
    print(f"n) Bonus Yatzee: {n}")
    print()
    try:
        # global total_upper_score
        # global total_lower_score
        if n == None:
            n = 0
        total_upper_score = a + b + c + d + e + f
        total_lower_score = g + h + i + j + k + l + m + n
        total_score = total_upper_score + total_lower_score
        if total_upper_score >= 0:
            print(f"Total Upper Score: {total_upper_score}")
            print(f"Total Lower Score: {total_lower_score}")
            print(f"Total Score: {total_score}")
            input("Game Over")
            users_name = input("Please enter your name: ")
            # this is where I add code to save the high scores
            save_high_score(total_score, users_name)
            menu()
    except:
        upper_list = [a, b, c, d, e, f]
        lower_list = [g, h, i, j, k, l, m, n]
        upper_scores = sum_integers(upper_list)
        lower_scores = sum_integers(lower_list)
        grand_total = upper_scores + lower_scores
        print(f"Total Upper Score: {upper_scores}")
        print(f"Total Lower Score: {lower_scores}")
        print(f"Total Score: {grand_total}")
        print("")


def dice_to_keep(index, result):
    saved_dice.append(result)


def sum_integers(list_to_review):
    total = 0
    for item in list_to_review:
        item_type = type(item)
        if item_type == int:
            total += item
    return total
    # input(f"Total of the list was {total}")


# sum_integers([4, 3, 7, 23, 4, "seven"])

menu()
