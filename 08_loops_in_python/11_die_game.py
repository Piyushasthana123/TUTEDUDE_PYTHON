"""
write a program to simulate a roll of a die/dice
A dei has 6 faces and numbers 1 to 6 written on them
the program should randomly print a number between 1 and 6
"""
import random
print("welcome to the game of rolling a dice.")
while True:
    choice=input("press 'Enter' to roll a die or 'q' to quit: ")
    choice = choice.strip() #empty space is remove
    if choice=='q':
        print("Thank for playing the game is over!")
        break
    elif choice=='':
        roll=random.randint(1,6)
        print(f"your nimber is {roll}")
    else:
        print("invalid input")

