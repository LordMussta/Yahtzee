# yatzee.py


import random
import os

try:
    import console
except:
    pass

no_of_dice = 6
rolled_dice = []
display_list = ["A", "B", "C", "D", "E"]
no_of_rolls = 0
saved_dice = []
total_upper_score = None
total_lower_score = None
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


def play():
    global saved_dice
    global no_of_rolls
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
    display_scores()
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
                g = 3 * number
    elif choice == "h" and h == None:  # 4 of a kind --> Done!
        h = 0
        for number in range(1, 6):
            if saved_dice.count(number) >= 4:
                h = 4 * number
    elif choice == "i" and i == None:  # Full house
        i = 0
        for number in range(1, 6):
            pass
    elif choice == "j" and j == None:  # long straight --> Done!
        j = 0
        saved_dice = list(dict.fromkeys(saved_dice))  # removes duplicates
        saved_dice = sorted(saved_dice)
        if saved_dice[0] == 1:
            if saved_dice[1] == 2 and saved_dice[2] == 3 and saved_dice[3] == 4 and saved_dice[4] == 5:
                j = 40
        if saved_dice[0] == 2:
            if saved_dice[1] == 3 and saved_dice[2] == 4 and saved_dice[3] == 5 and saved_dice[3] == 6:
                j = 40
    elif choice == "k" and k == None:  # short straight --> Done!
        k = 0
        saved_dice = list(dict.fromkeys(saved_dice))  # removes duplicates
        saved_dice = sorted(saved_dice)
        if saved_dice[0] == 1:
            input(saved_dice)
            if saved_dice[1] == 2 and saved_dice[2] == 3 and saved_dice[3] == 4:
                k = 30
                # input("short straight A achieved")
        if saved_dice[0] == 2:
            input(saved_dice)
            if saved_dice[1] == 3 and saved_dice[2] == 4 and saved_dice[3] == 5:
                k = 30
                # input("short straight B achieved")
        if saved_dice[0] == 3:
            input(saved_dice)
            if saved_dice[1] == 4 and saved_dice[2] == 5 and saved_dice[3] == 6:
                k = 30
                # input("short straight C achieved")
    elif choice == "l" and l == None:  # Yatzee! --> Done!
        l = 0
        for number in range(1, 6):
            if saved_dice.count(number) >= 5:
                l = 50
    elif choice == "m" and m == None:  # chance --> Done!
        m = 0
        for number in range(1, 6):
            m = m + number
    elif choice == "n":  # Bonus Yatzee! --> Done!
        for number in range(1, 6):
            if saved_dice.count(number) >= 5:
                n = n + 100
    else:
        input("Wrong selection. Try again")
        add_score()
    display_scores()
    reset_dice()


def reset_dice():
    global saved_dice
    global no_of_rolls
    saved_dice = []
    no_of_rolls = 0
    clear_screen()
    play()


def display_scores():
    print("Upper scores:")
    print(f"a) 1s score: {a}")
    print(f"b) 2s score: {b}")
    print(f"c) 3s score: {c}")
    print(f"d) 4s score: {d}")
    print(f"e) 5s score: {e}")
    print(f"f) 6s score: {f}")
    print()
    print("Lower Scores:")
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
        global total_upper_score
        global total_lower_score
        total_upper_score = a + b + c + d + e + f
        total_lower_score = g + h + i + j + k + l + m + n
        total_score = total_upper_score + total_lower_score
        if total_upper_score >= 0:
            print(f"Total Upper Score: {total_upper_score}")
            print(f"Total Lower Score: {total_lower_score}")
            print(f"Total Score: {total_score}")
            input("Game Over")
            quit()
    except:
        input("press a key to continue...")


def dice_to_keep(index, result):
    saved_dice.append(result)


play()

score_sheet = """
Lower:
	g) 3 of a kind (+)
	h) 4 of a kind (+)
	i) full house (25 pts)
	j) long straight (40 pts)
	k) short straight (30 pts)
	l) Yatzee (50 pts)
	m) Chance (+)
"""
