import math                                                    # Importing math functions
import random                                                  # Importing random functions such as randint()
import os


def unique_pick(n):                                            # Makes sure that unique numbers are picked.
    pick = random.randint(1, 60)
    if pick in n:
        return unique_pick(n)
    else:
        return pick

def lottery():              # This randomly generates the numbers you would pick.


    my_numbers = []
    i = 0

    while i < 5:
        pick = unique_pick(my_numbers)




        my_numbers.append(pick)
        i += 1

    return my_numbers


def generate_winning_picks():                          # This generates the winning numbers to the lottery.

    winning_picks =  []
    i = 0

    while i < 5:
        winning_pick = unique_pick(winning_picks)
        winning_picks.append(winning_pick)
        i += 1

    return winning_picks


def game():

    my_picks = lottery()

    winning_nums = generate_winning_picks()

    wins = 0
    for i in winning_nums:
        if i in my_picks:
            wins+=1

    return wins



def main():

    total = 10000000

    list_of_wins = []
    for i in range(0,total):
        list_of_wins.append(game())

    for i in range(0, 6):
        num_of_win = list_of_wins.count(i)
        print("Winning", i, "Ball:", num_of_win, "-", (num_of_win/total)*100)








main()
