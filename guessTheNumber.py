#THIS IS A GUESS THE NUMBER GAME
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#ask the player to guess 6 times
for guessesTaken in range(1, 7):
    guess = int(input('Take a guess: '))

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this condition is the correct guess
if guess == secretNumber:
    print('Good job!')
else:
    print('Nope. The number I was thinking of was: ' + str(secretNumber))
