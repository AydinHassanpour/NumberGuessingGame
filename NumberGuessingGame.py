import random

def guess_number():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")

guess_number()
