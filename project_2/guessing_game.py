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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        """this becomes significant after few guesses when the possibility of multiple numbers remain.
           when the low and high are not equal like 4 and 7 then 5 and 6 are still possible but when 5 
           is high and low then that is the correct number."""
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay the computer guessed your number, {guess} correctly!") 



guess_the_number(10)
computer_guess(10)


    
