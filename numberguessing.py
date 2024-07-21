"""
Created on Sun Jul 21 15:49:16 2024

@author: acer
"""

import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0
flag = False

# for calculation of minimum number of
# guesses depends upon range
while count < total_chances:
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!