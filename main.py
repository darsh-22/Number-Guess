# ==================================================== #
#                                                      #
#  Created By: Darhil Aslaliya -  GitHub :- darsh-22   #
#                                                      #
# ==================================================== #

# required module
import random

# generate random number from 1 to 10
randon_number = random.randint(1, 10)
userGuess = None
guesses = 0

# main loop
while(userGuess != randon_number):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randon_number):
        print("You guessed it right!")
    else:
        if(userGuess>randon_number):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")


# saving high score in file
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

# check if high score is break or not
if(guesses<highscore):
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
