"""
create a simple number guessing game.
The user gets 10 chances to guess the number.
if the user guesses the number before 10 chances , stop asking the number from the user,say congrats and end the game
if the user never guesses the number after 10 chances then end the game.
"""
import random
number=random.randint(1,50)
print("Welcome to the number guessing game")
print("guess the number between 1 and 50 and before the 10 chances")
attempts =10
for i in range(10):
    guessed_number = int(input("please enter your guessed number: "))
    attempts -= 1
    print(f"you have {attempts} attempts left")
    if attempts==0:
        break
    if guessed_number == number:
        print(f"your guessed number {guessed_number} is correct you won the game")
        break
    elif guessed_number < number:
        print(f"your guessed number {guessed_number}  please guess 'higher' number")
    elif guessed_number > number:
        print(f"your guessed number {guessed_number}  please guess 'lower' number")
print("game is over")


