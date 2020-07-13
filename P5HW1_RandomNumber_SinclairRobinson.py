# This is a program that gives a random number game.
# 07-12-2020
# CTI-110 P5HW1 - Random Number
# Sinclair Robinson

# Write a program that gives simple math quizzes. The program should display
# two random numbers  that are to be added.

import random

flag = True
while flag:
    num = input('Type a number for an upper bound: ')

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print('Invalid input! Try Again!')

secret = random.randit(1,num)

guess = None
count = 1

while guess != secret:
    guess = input('Please type a number between 1 and ' + str(num) + ": ")
    if guess.isdigit() :
        guess = int(guess)

    if guess == secret:
         print('You got it!')
    else:
        print('Please try again!')
        count += 1
  
