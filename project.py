# NUMBER GUESSING GAME


import random

#loop creation because it ask the user wheather they want to play new game.

while(True):

    # Generate the random number.
    num=random.randint(1,100)

    # creation of loop because to run the condition again and again until user guess the correct number.
    while(True):

    # If the user enter the invalid number then our program will not show the value error
        try:
            Makeaguess = int(input("enter your number betwwen 1 and 100: "))
    # Check the condition
            if(Makeaguess==num):
                print("Congratulation! your guess is correct")
                break
            elif(Makeaguess<num):
                print(" Please enter the larger number")
            else:
                print("Please enter the smaller number")
        except ValueError:
            print("Please enter valid number that is between 1 to100")
    # Ask the user if they wanted to play the new game
    anotherchance=input("Do you want to play again? (yes/no:) ").strip().lower()
    if(anotherchance!="yes"):
        print("thanks for playing the game ")
        break

