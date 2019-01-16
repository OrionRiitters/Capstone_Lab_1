# This program asks the user for their name and birthday month, then returns that
# information.

def gatherInput():
    nameInput = input("What is your name?\n")
    monthInput = input("What month were you born in?\n")
    nameLength = len(nameInput)
    return nameInput, monthInput, nameLength

def displayInfo(nameInput, monthInput, nameLength):
        print("---------------\nHello, " + nameInput + "!")
        if monthInput.lower() == "january":
            print("Happy birthday month!")
        print("There are " + str(nameLength) + " letters in your name!")

def main():
    nameInput, monthInput, nameLength = gatherInput()
    displayInfo(nameInput, monthInput, nameLength)

main()
