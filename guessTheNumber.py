# эта игра на угадывание чисел
import random

guessesTaken = 0

print("Hello! What's your name?")
#myName = input()
myName = 'Nikita'

number = random.randint(1,30)
print("So, " + myName + ", I guess a number from 1 till 30")

for guessesTaken in range(6):
    print("try to guess")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your number is too small")

    if guess > number:
        print("Your number is too big")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Well done ' + myName + '! You did it for ' + guessesTaken + ' time(s)')

if guess != number:
    number = str(number)
    print('Sorry. I had guessed the number ' + number + '.')