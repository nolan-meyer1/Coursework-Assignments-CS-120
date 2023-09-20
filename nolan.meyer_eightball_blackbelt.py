"""
Magic 8-Ball game blackbelt

Magic 8-Ball game where you can print out all fortunes,
select a fortune based on a number you give, and recieve
a random fortune, and lastly add a fortune. 

Nolan Meyer

September 8, 2023

"""
import random 

#List of all possible fortunes
fortunes = ["Without a doubt", "It is certain", "Signs point to yes", "Cannot predict now", "Ask again later", "My reply is no", "Don't count on it", "Very doubtful"]

#List of str responses
invResponse = ["one", "two", "three","four", "five", "six","seven","eight",
               "nine", "ten", "eleven", "tweleve", "thirteen","fourteen","fifteen",
               "sixteen", "seventeen","eighteen","nineteen", "twenty"]

#Function that contains the code
def fortuneSelector():

    print(""" Welcome to Magic 8-Ball! What will you do? 
    1) Print all fortunes
    2) Print a specific fortune
    3) Get a random fortune
    4) Create you own fortune""")

    choice = input("Please choose 1,2,3, or 4: ")

    #If statement that decides what the choice is and checks for a numeric response
    if choice in invResponse:
        print("Please enter the numeric response")

    elif choice == "1": 
        print("YOUR FORTUNES:")
        for (index, fortune) in enumerate(fortunes): 
            print(f"{index}) {fortune}")

        fortuneSelector()

    #Elif for choice 2 which you select the fortune
    elif choice == "2":
        fortuneNumber = input(f"What number would you like(0-{(len(fortunes))-1})?: ")
        if fortuneNumber in invResponse:
            print("Please enter a numeric response")
            fortuneSelector()
        elif int(fortuneNumber) in range(len(fortunes)):
            print(fortunes[int(fortuneNumber)])
            fortuneSelector()        
        else: 
            print(f"Invalid Response. Please try again by picking a number 0 to {len(fortunes)-1}")
            fortuneSelector()

    #Elif for 3rd choice which is recieve a random fortune
    elif choice == "3":
        randomIndex = random.randrange(len(fortunes))
        question = input("Your question: ")
        print(fortunes[randomIndex])
        fortuneSelector()

    #Elif for 4th choice which is create a fortune
    elif choice == "4":
        newFortune = input("Please create a new fortune: ")
        fortunes.append(newFortune)
        fortuneSelector()

    #Else if the wrong numbers are entered
    else:
        print("Please enter a valid number. (1,2,3, or 4)")
        fortuneSelector()

#Starts running the code
fortuneSelector()