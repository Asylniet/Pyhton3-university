import random

def game(a) :
    name = input('Hello! What is your name? \n')

    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    count = 0
    guess = int(input('Take a guess. \n'))
    while(guess != a) :
        if guess < a :
            print('Your guess is too low.')
        elif guess > a :
            print('Your guess is too high.')
        count += 1
        guess = int(input('Take a guess. \n'))
    
    print(f'Good job, {name}! You guessed my number in {count} guesses!')


a = random.randint(1,  20)
game(a)