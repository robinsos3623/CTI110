# This is a program that gives simple math quizzes.
# 07-12-2020
# CTI-110 P5HW2 - Math Quiz
# Sinclair Robinson

# Write a program that gives simple math quizzes. The program should display
# two random numbers  that are to be added.

import random

randomNumber1 = random.randint( 1, 250 )
randomNumber2 = random.randint( 1, 250 )

def askQuestion():
    global randomNumber1
    global randomNumber2
    int(input( "What is " + str(randomNumber1) + " + " + \
               str( randomNumber2) + "?: " ) )
    return userAnswer

def checkAnswer( userAnswer ):
    global randomNumber1
    global randomNumber2

    correctAnswer = randomNumber1 + randomnumber2
    if userAnswer == correctAnswer:
        print("\nCongratulations:")
    else:
        print("\nIt's wrong. The correct answer is", correctAnswer )




    def main():
        userAnswer = askQuestion()
        checkAnswer( userAnswer )

    main()
        

