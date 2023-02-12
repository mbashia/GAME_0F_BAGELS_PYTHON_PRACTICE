# in bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game
# offers one of the following hints: "Pico" when your guess has a correct digit in the wrong place, "Fermi" when
# your guess has a correct digit in the correct place and  "bagels" if your guess has no correct values. You have
# ten tries to guess the secret number.
import random


def generate_random_num():
    secretNum = ''
    for i in range(3):
        number = random.randint(0, 9)
        numbers = str(number)
        secretNum += numbers
    return secretNum


def generate_clues(guess, secretnumber):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretnumber[i]:
            clues.append("fermini")
        elif guess[i] in secretnumber:
            clues.append("pico")
        clues.sort()

    if len(clues)==0:
        return "bagels"

    return " ".join(clues)


def main():
    print("welcome to the game of bagels.... Enjoy!!1")
    print("you have a maximum of 10 tries")
    numguess = 0

    isplaying = True
    while isplaying:
        secretnumber = generate_random_num()
        print("i have the secret number.... i guess is time for guessing")
        print("you have a maximum of 10 guesses")
        while numguess <= 10:
            guess = input("enter guess:")
            if guess == secretnumber:
                print("lucky bastard you've gotten it")
                break
            clues = generate_clues(guess, secretnumber)
            print(clues)
            if numguess == 7:
                print("only 3 guesses remaining")
            elif numguess ==10:
                print(f"you have run out of guesses the correct numbers was {secretnumber}")
            numguess += 1
        play_again = input("do want to play again (y/n)")
        if not play_again.lower() or not play_again.startswith("y"):
            isplaying = False
    print("thanks for playing dont come back again")
if __name__ == '__main__':
    main()