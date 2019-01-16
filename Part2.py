# This program prompts the user for the classes they are taking, then lists those
# classes.

def gatherInput():
    classList = []
    print('-------------\nThis program will ask for your current classes, then list them.')
    print('Enter \'q\' when you are finished.')
    while True:
        userInput = input('Please write out a class you are taking!:\n')
        print('Thanks!\n--------------')
        if userInput == 'Q' or userInput == 'q':
            break
        classList.append(userInput)
    return classList

def displayInfo(classList):
    print('Here are your classes!')
    for i in classList:
        print(i)

def main():
    classList = gatherInput()
    displayInfo(classList)

main()
