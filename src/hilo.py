import random


def main():
    resp = input("Would you like to play a game?[y/n]")
    if resp.lower() == 'y':
        play_game()


def play_game():
    number = random.randint(0, 100)
    guess = -1
    while guess != number:
        guess = int(input("Pick a number between 0 - 99. "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
    print("You got it!")


if __name__ == '__main__':
    main()
