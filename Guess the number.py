import random

num = random.randint (1,100)
num_guess = 7

entry = input("I'm thinking of a number between 1 - 100.\nYour guess: ")
entry = int(entry)


while(entry != num and num_guess > 0):
    if (entry > num):
        print("Too high!")
    elif (entry < num):
        print("Too low!")
    num_guess -= 1
    print("Guesses left: %d \n"%num_guess)
    if (num_guess > 0):
        entry = input("Guess again: ")
        entry = int(entry)

if (num_guess <= 0):
    print("Game over, you don't have any more guesses!")
else:
    print("\nYou guessed it!")

