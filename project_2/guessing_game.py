import random

def guess_the_number(x):
    random_number = random.randint(1, x)
    guess = 0

    """ we are generating number between 1 and x while initalising the guess at 0, so guess will never
    be same as generated number and while loop will always be true"""
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"sorry, guess again. Too low")
        elif guess > random_number:
            print(f"sorry guess again. Too high")
    
    print(f"Yay, congrats. you have guessed the {random_number} correctly")


guess_the_number(10)


    
