"""
Card Dealer/Black Jack

This is a Card Dealer framework
that doesn't store card names
but comes up with them using 
a database. Using that database
you can play the card game
Black Jack. Ace's do count
as one in this game.

Nolan Meyer

September 21, 2023
"""
import random
import time

#Constants
num = 52
rankName = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

suitName = ("clubs", "hearts", "spades", "diamonds")
hands = ("deck", "player", "computer")

deck = 0
player = 1
computer = 2

#Scores
playerScore = 0
computerScore = 0

#--------------------------------------------------------------------------------------------------   

#Initizlaes the card database by creating a list of 52 integers
def initCards():
    cards = []

    for number in range(num):
        cards.append(0)
    
    return cards

#--------------------------------------------------------------------------------------------------   

#Prints the Card Database
def showDB(cardDB):
    for cardNum,location in enumerate(cardDB):
        print(f"{cardNum}) {getCardName(cardNum)}{hands[location]:>20}")
        
#--------------------------------------------------------------------------------------------------   

#Creates the name of the card
def getCardName(cardID):
    suit = cardID//13
    rank = cardID % 13

    return f"{rankName[rank]} of {suitName[suit]}"

#--------------------------------------------------------------------------------------------------   

#Assigns a card to a hand
def assignCard(cardDB, hand):
    ranNum = random.randrange(num)
    keepGoing = True

    while keepGoing:
        if cardDB[ranNum] == deck:
            cardDB[ranNum] = hand
            keepGoing = False
        
        else:
            ranNum = random.randrange(num)

#--------------------------------------------------------------------------------------------------   

#Shows the hands
def showHand(cardDB, hand):
    print(" ")
    print(f"Cards in {hands[hand]}s hand: ")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print(getCardName(cardNum))

#--------------------------------------------------------------------------------------------------   

#Keeps track of the score of the player and computers deck
def score(cardDB,hand):
    dummyscore = 0
    score = 0
    for cardNum, location in enumerate(cardDB):
        rank = 0
        if location == hand:
            rank = (cardNum % 13) + 1
            if rank > 10:
                dummyscore += 10
            
            else:
                dummyscore += rank
    
    score = dummyscore
        
    return score

#--------------------------------------------------------------------------------------------------   

#This function runs the dealers turns
def dealer(cardDB):
    assignCard(cardDB,computer)
    showHand(cardDB,computer)
    print(" ")
    print(f"Dealer score is {score(cardDB,computer)}")
    keepGoing = True

    while keepGoing:
        if score(cardDB, computer) > 21:
            keepGoing = False

        elif score(cardDB,computer) >= 17:
                print(" ")
                print("I will stand")
                keepGoing = False

        
        elif score(cardDB,computer) <= 16:
            print("I will hit")
            assignCard(cardDB,computer)
            print(" ")
            time.sleep(3)
            showHand(cardDB,computer)
            print(" ")
            print(f"Dealer score is: {score(cardDB,computer)}")

    gameOutcome(score(cardDB,computer),score(cardDB,player))

#--------------------------------------------------------------------------------------------------      

#Decides the outcome of the game
def gameOutcome(computerScore,playerScore):

    if playerScore == computerScore:
        print("Push")
    
    elif computerScore == 21:
        print("Black Jack! Dealer wins!")
    
    elif playerScore == 21:
        print("Black Jack! Player wins!")
    
    elif (computerScore > 21) and (playerScore > 21):
        print("We both bust! You lose!")
    
    elif computerScore > 21:
        print("Bust! Player wins")
    
    elif playerScore > 21:
        print("Bust! Dealer wins")
    
    elif playerScore > computerScore:
        print("Player wins!")
    
    elif playerScore < computerScore:
        print("Computer wins!")

#--------------------------------------------------------------------------------------------------   
    
#Function that controls the game
def playBlackJack(cardDB):
    print(" ")
    print("Dealing has begun!")

    #Deals the player two card and the computer one
    for i in range(2):
        assignCard(cardDB,player)
    assignCard(cardDB, computer)

    print(" ")
    showHand(cardDB, player)
    print(" ")
    print(f"Your score is: {score(cardDB, player)}")

    print(" ")
    showHand(cardDB, computer)
    print(f"The dealer's score is: {score(cardDB, computer)}")
    print(" ")

    #Starts the process for the player to either hit or stand
    keepGoing = True

    while keepGoing:
        userChoice = input("What would you like to do? Hit(H), Stand(S)?: ")
        

        if userChoice.upper() == "H":
            assignCard(cardDB, player)
            showHand(cardDB,player)

            if score(cardDB,player) > 21:
                print(" ")
                print(f"Your score is: {score(cardDB, player)}")
                print("Bust! Dealer's turn")
                dealer(cardDB)
                keepGoing = False
            
            
            elif score(cardDB,player) < 21:
                print(" ")
                print(f"Your score is {score(cardDB,player)}")
            
            elif score(cardDB,player) == 21:
                print("Black Jack!")
                print("Dealers turn")
                dealer(cardDB)
            
        elif userChoice.upper() == "S":
            print("You stand! Dealers Turn")
            dealer(cardDB)
            keepGoing = False

#--------------------------------------------------------------------------------------------------   

#Menu for the game
def menu():
    print("""Welcome! Please select one of the options:
            1. Print the Card Database
            2. Play Black Jack""")
    choice = input("What will you choose?: ")

    return choice

#--------------------------------------------------------------------------------------------------   

#Main function that runs the program
def main():
    cardDB = initCards()
    userChoice = menu()

    if userChoice == "1":
        showDB(cardDB)
    
    if userChoice == "2":
        playBlackJack(cardDB)

#Runs the program
main()