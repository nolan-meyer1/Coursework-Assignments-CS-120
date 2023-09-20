"""
Magic 8-Ball game 

Magic 8-Ball game where you can print out all fortunes,
select a fortune based on a number you give, and recieve
a random fortune. 

Nolan Meyer, Ace  Stout

September 7, 2023

"""
import random 
#List of all possible fortunes
fortunes = ["Without a doubt", "It is certain", "Signs point to yes", "Cannot predict now", "Ask again later", "My reply is no", "Don't count on it", "Very doubtful"]

#List of str responses
invResponse = ["one", "two", "three","four", "five", "six","seven"]

print(""" Welcome to Magic 8-Ball! What will you do? 
 1) Print all fortunes
 2) Print a specific fortune
 3) Get a random fortune""")

choice = input("Please choose 1,2, or 3: ")

#If statement that decides what the choice is and checks for a numeric response
if choice in invResponse:
    print("Please enter the numeric response")

elif choice == "1": 
    print("YOUR FORTUNES:")
    for (index, fortune) in enumerate(fortunes): 
        print(f"{index}) {fortune}")

#Elif for choice 2 which you select the fortune
elif choice == "2":
    fortuneNumber = input("What number would you like(0-7)?: ")
    if fortuneNumber in invResponse:
        print("Please enter a numeric response")
    elif int(fortuneNumber) in range(len(fortunes)):
        print(fortunes[int(fortuneNumber)])
    
    else: 
        print("Invalid Response. Please try again by picking a number 0 to 7")

#Elif for 3rd choice which is recieve a random fortune
elif choice == "3":
    randomIndex = random.randrange(len(fortunes))
    question = input("Your question: ")
    print(fortunes[randomIndex])

#Else if the wrong numbers are entered
else:
    print("Please enter a valid number. (1,2, or 3)")