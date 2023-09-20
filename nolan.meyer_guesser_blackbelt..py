"""
Number Guesser Game 

A game where the user tries
to guess a number 0 through 
100 in 7 tries. The user will
lose in 7 tries. This version
uses expetion handling, and has 
an option for the computer to 
guess the number using a binary
search algorithim. This is organized
using functions

Nolan Meyer

September 14, 2023
"""
import random

#You guess the computers number function-----------------------------------------------
def humanGuessGame():
    ranNum = random.randint(0,100)
    tries = 0
    keepGoing = True 
    
    #Start of loop 
    while keepGoing:
        if tries < 7:
            tries += 1
            guess = input(f"{tries}) Please enter a guess: ")
        
            #Tries to convert to int if it gets valueError runs code below. Then starts proccess again.
            try:
                guess = int(guess)

                #Too High
                if guess > ranNum:
                    print("Too high")
                    
                #Too low
                elif guess < ranNum:
                    print("Too low")
            
                        #You win
                elif guess == ranNum:
                    print(f"You got it right in {tries} turns!")
                    keepGoing = False
                    
            except ValueError:
                print("Please enter a numeric response!")

                #You lost
        else:
            print(f"You lost! The number was {ranNum}.")
            keepGoing = False

#The computer guesses your number---------------------------------------------------
def computerGuessGame():    
        tries = 1
        compGuess = 50
        start = 0
        end = 100
        keepGoing = True
        
        while keepGoing:
            print(f"{tries}) I guess {compGuess}")
            humanInput = input("Was I high, low, or correct(h,l,c): ")

            if humanInput.upper() == "H":
                end = compGuess
                compGuess = round((start + compGuess)//2)
                tries += 1

            elif humanInput.upper() == "L":
                start = compGuess
                compGuess = round((end + compGuess)//2)
                tries += 1
    
            elif humanInput.upper() == "C":
                print(f"The computer got it right in {tries} tries!")
                keepGoing = False
        
            else:
                print("Please enter a valid response(h,l,c)")
                tries += 1
#------------------------------------------------------------------------------------------

#Checks to see which game you're going to play 
print("""Welcome! There are two games you can play
      1: You guess the computer's number
      2: The computer guesses your number""")
keepGoing = True

#Decides which game you're playing
while keepGoing:
    choice = input("Please enter which one you would like to play(1,2): ")
    if choice == "1":
        keepGoing = False
        humanGuessGame()

    elif choice == "2":
        keepGoing = False
        computerGuessGame()

    else:
        print("Please enter a valid response(1,2)")