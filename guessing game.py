import random

guessesTaken = 0
number = random.randint(1, 20)
name = input('Hello! What is your name? ')
print('well ' + name + ' This is a guessing number game')
for guessesTaken in range(6):
    # print(guessesTaken in range(6))
    # print('take a guess')
    # guess = input()
    def user_input():
        a = input("Please Enter a number: ")
        return a
    i = 1
    while i <= 1:
        try:
            guess = int(user_input())
            break
        except ValueError as err:
            print("Invalid Input !")
    if guess > number:
        print('guess is too high')
    if guess < number:
        print('guess is too low')
    if guess == number:
        break
if guess == number:
    guessesTaken = guessesTaken + 1
    print('Good ' + name + ' you guessed the number in ' + str(guessesTaken) + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope The number i thought was ' + number + '.')
