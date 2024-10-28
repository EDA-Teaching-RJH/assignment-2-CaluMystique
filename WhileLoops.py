### Part Two -- your code goes here. 
import random

number = random.randint(1, 100)
print("I picked a number between 1 and 100. Try and guess it!")

Guessed = False

while Guessed == False:
    guess = int(input("What number is it? "))
    if guess == number:
        print("Correct! Good Job!")
        Guessed = True
    else:
        print("Wrong. Try again")