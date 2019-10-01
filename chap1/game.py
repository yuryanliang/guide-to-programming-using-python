import os
import time
from random import randint


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print("welcome!")

secret = randint(1, 10)

while True:
    g = input("Guess the number: ")
    guess = int(g)
    if guess > secret:
        print("Too high!")
        time.sleep(1)
    elif guess < secret:
        print("Too low!")
    else:
        print("You win!")
        break

print("Game Over!")
