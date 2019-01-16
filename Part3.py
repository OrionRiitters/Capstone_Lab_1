# This program generates a 'random' number within a certain range, and then prompts
# the user to guess the generated number. Hints are provided at each prompt.

from random import randint

def generateNumber():
    randomInt = randint(1, 10)
    return randomInt

def compare(i, j):
    if i < j:
        print('You guessed too low!')
        return False
    elif i > j:
        print('You guessed too high!')
        return False
    else:
        print('You guessed correctly')
        return True

def prompt():
    userInput = int(input('What is my number?\n'))
    return userInput

def main():
    randomInt = generateNumber()
    whileBool = False
    print('--------------\nI (the program) have generated a number between 1 and 10.')
    while whileBool == False:
        userInput = prompt()
        whileBool = compare(userInput, randomInt)

main()
