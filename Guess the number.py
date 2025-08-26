import random
attempts=0
print("WELCOME TO GUESS THE NUMBER GAME...")
print("Let be think the number between 1 to 50")
level=input("If you want difficulty method then type 'hard' .otherwise for easy level type 'easy':\n").lower()
if level == "hard":
    attempts=5
    print("You have 5 attempts to guess the number..")
else:
    attempts=10
    print("You have 10 attempts to guess the number..")
computer_guess=random.randint(1,50)

def guess(attempts):
    flag=True
    while flag:

        guess=int(input("Guess the number :\n"))
        if guess == computer_guess:
            print(f"your guess is correct ....it is {computer_guess} ")
            flag=False

        else:
            attempts=attempts-1
            if attempts==0:
                print(f"you loss the game...Guessed the number is {computer_guess}")
                flag=False
            else:

                print(f"your guess is wrong.you have {attempts} attempts left.")
                if guess > computer_guess:
                    print("Your guess is higher")
                else:
                    print("Your guess is lower")


guess(attempts)