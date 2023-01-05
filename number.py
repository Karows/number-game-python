import random

r = random.randint(1, 99)
guess = int(input("Guess the number between 1-99: "))
while True:
    if guess > r:
        print("Too High, Guess Again")
        guess = int(input("Guess the number between 1-99: "))
    elif guess < r:
        print("Too Low, Guess Again")
        guess = int(input("Guess the number between 1-99: "))
    else:
        answer = str(input("WINNER!! Would you like to play again? [y/n]: "))
        if answer in ('n'):
            print("GoodBye, Thanks for playing <3")
            break
            if answer in ('y'):
                print("test")
