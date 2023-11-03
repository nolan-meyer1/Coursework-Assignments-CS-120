import random
import json
import os
"""
Module for a combat system
that allows you two players to 
battle each other. This version
allows you to concentrate, heal,
fight, and possibly get a a random
power up. You can also create your
own custom monsters. 

Nolan Meyer

October 19, 2023
"""
class Character(object):

    #Initizales the object
    def __init__(self,name = "Character", hitPoints = 1,hitChance = 0,maxDamage = 1,armor = 0 ):
        super().__init__
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    #Name property
    @property
    def name(self):
        return self.__name
    
    
    #Name setter
    @name.setter
    def name(self,value):
        if type(value) == str:
            self.__name = value
        
        else:
            print("Name: You need a str value. Setting to Hero")
            self.__name = "Hero"


    #Hitpoints property
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    
    #Hitpoints setter
    @hitPoints.setter
    def hitPoints(self,value):
        if type(value) == int:
            if value >= 0:
                self.__hitPoints = value
            
            else:
                 print("Hit Points: Positive integers greater than or equal to 0 only. Setting to 10")
                 self.__hitPoints = 10
        
        else:
            print("Hit Points: Only integers allowed. Setting to 10")
            self.__hitPoints = 10

    
    #Hitchance property
    @property
    def hitChance(self):
        return self.__hitChance
    

    #Hitchance setter
    @hitChance.setter
    def hitChance(self,value):
        if type(value) == int:
            if value <= 100:
                if value >= 0:
                    self.__hitChance = value
            
            else:
                print("Hit Chance: Value must be between 0-100. Setting to 100.")
                self.__hitChance = 100
        
        else:
            print("Hit Chance: Type must be integers. Setting to 50")
            self.__hitChance = 50
    

    #Maxdamage property
    @property
    def maxDamage(self):
        return self.__maxDamage
    

    #Maxdamage setter
    @maxDamage.setter
    def maxDamage(self,value):
        if type(value) == int:
            if value > 0:
                self.__maxDamage = value
            
            else:
                print("Max Damage: Damage must be greater than 10. Setting to 10")
                self.__maxDamage = 1
        
        else:
            print("Max Damage: Only integers allowed. Setting to 10")
            self.__maxDamage = 1
    

    #Armor property
    @property
    def armor(self):
        return self.__armor
    

    #Armor setter
    @armor.setter
    def armor(self,value):
        if type(value) == int:
            if value >= 0:
                self.__armor = value
            
            else:
                print("Armor: Must be greater than or equal to 0. Setting to 0.")
                self.armor__ = 0
        
        else:
            print("Armor: Positive integers allowed. Setting to 0")
            self.__armor = 0
    
    #print stats method
    def printStats(self):

        print(" ")
        print(self.name)
        print("==================")
        print(f"Hit points: {self.hitPoints}")
        print(f"Hit chance: {self.hitChance}")
        print(f"Max damage: {self.maxDamage}")
        print(f"Armor: {self.armor}")

    #Hit method that decides if a character hit's or doesn't hit
    def hit(self,character):
        ranNum = random.randint(0,100)
        damage = random.randint(1,self.maxDamage)

        if ranNum <= self.hitChance:
            print(" ")
            print(f"{self.name} hits {character.name}")
            print(f"For {damage}")
            print(f"{character.name} armor can absorb {character.armor}")

            if damage > character.armor:
                if character.hitPoints - (damage - character.armor) >= 0:
                    character.hitPoints -= damage - character.armor
                
                else:
                    character.hitPoints = 0
        
        else:
            print(f"{self.name} missed!")


    #Allows the user to decide if he is going to fight, heal, or concentrate. 
    def userAction(self,character):
        keepGoing = True
        print(" ")
        print(f"{self.name} what will you do? ")
        print("1) Fight")
        print("2) Heal")
        print("3) Concentrate")
        
        userChoice = input("Your choice?: ")

        while keepGoing:
            if userChoice == "1":
                self.hit(character)
                keepGoing = False
            
            elif userChoice == "2":
                ranNum = random.randint(0,20)
                print(f"{self.name} healed {ranNum} HP!")
                self.hitPoints += ranNum
                keepGoing = False

            elif userChoice == "3":
                ranNum = random.randint(0,10)
                print(f"{self.name} gained {ranNum} Hit Chance!")
                self.hitChance += ranNum
                keepGoing = False
            
            else:
                print("Invalid Response. Please enter 1,2, or 3")
                userChoice = input("What will you do?: ")


    #Method that allows the user to possibly get a random power up
    def powerUp(self):

        ranNum = random.randint(0,100)

        if ranNum <= 1:
            print(f"{self.name} found a Smash Ball from Super Smash Bros. Brawl. Setting max damage to 1,000")
            self.maxDamage = 1000
        
        elif ranNum <= 10:
            print(f"{self.name} found a UAV from Call of Duty. You gained 40 hit chance!")
            self.hitChance += 40
        
        elif ranNum <= 15:
            print(f"{self.name} found a Golden Apple from Minecraft. Healing 20 HP, and adding 5 to armor")
            self.hitPoints += 20
            self.armor += 5
        
        elif ranNum <= 20:
            print(f"{self.name} found a Mushroom from Mario. Adding 3 to armor.")
            self.armor += 3
        
        elif ranNum <= 30:
            print(f"{self.name} found a Mini Shield from Fortnite. Adding 10 to health")
        


#End of class
#------------------------------------------------------------------------------------------------------------------------------------- 

#Allows the user to build their character/ Add exception for error handling
def buildCharacter(player):

    print(" ")
    try:
        print(player)
        nameInput = input("What will your character's name be?: ")
        hpInput = int(input("What will you HP be?: "))
        hitChanceInput = int(input("What will your hit chance be?: "))
        maxDamageInput = int(input("What will you max damage be?: "))
        armorInput = int(input("What will your armor be?: "))

        return Character(nameInput,hpInput,hitChanceInput,maxDamageInput,armorInput)
    
    except ValueError:
        print("Error. Make sure you're entering the correct type.")
        buildCharacter(player)


#Starting menu options
def menu():
    print(" ")
    print("Welcome to Combat! Which would you like to do")
    print("1) Fight againts a friend!")
    print("2) Fight againts a built in character")
    print("3) Create your own monster")
    print("4) Quit")

    userChoice = input("You choice: ")
    return userChoice


#Fight function between player and monster    
def fightMonster(player,monster,monsters):
    keepGoing = True
    userChoice = ""

    while keepGoing:    

       player.userAction(monster)
       player.powerUp()
       monster.hit(player)

       print("")
       print(f"{player.name}: {player.hitPoints} HP")
       print(f"{monster.name}: {monster.hitPoints} HP")
                
       if player.hitPoints > 0:
           
            if monster.hitPoints > 0:

                userChoice = input("Press <ENTER> for another round or Q to quit: ")

            else:
                print(f"{player.name} wins!")
                userPlayAgain = input("Click <ENTER> to play again with random values or Q to quit: ")

       else:
            print(f"{monster.name} wins!")
            userPlayAgain = input("Click <ENTER> to play again with random values or Q to quit: ")

       
       if userChoice.capitalize() == "Q":
           keepGoing = False
    
       try:
            if userPlayAgain == "":
                player.hitPoints = random.randint(0,40)
                player.hitChance = random.randint(0,100)
                player.maxDamage = random.randint(1,15)
                player.maxArmor = random.randint(0,5)

                monster.hitPoints = monsters[monster.name][1]
                monster.hitChance = monsters[monster.name][2]
                monster.maxDamage = monsters[monster.name][3]
                monster.maxArmor = monsters[monster.name][4]

                player.printStats()
                monster.printStats()


                fightMonster(player,monster,monsters)
        
            elif userChoice.capitalize() == "Q":
                keepGoing = False
        
            else:
                print("Invalid Response. Quitting game")
                keepGoing = False
    
       except UnboundLocalError:
           pass


#Allows you to fight between two players
def fightPlayer(player1,player2):
    keepGoing = True

    while keepGoing:
       
       if player1.hitPoints > 0:
           
            if player2.hitPoints > 0:
                 
                 player1.userAction(player2)
                 player1.powerUp()
                 player2.userAction(player1)
                 player2.powerUp()

                 print("")
                 print(f"{player1.name}: {player1.hitPoints} HP")
                 print(f"{player2.name}: {player2.hitPoints} HP")

            else:
                print(f"{player1.name} wins!")
                userChoice = input("Click <ENTER if you would like to play again with random values or Q to quit: ")

       else:
            print(f"{player2.name} wins!")
            userChoice = input("Click <ENTER> if you would like to play again with random values or Q to quit: ")

       try:
            if userChoice.capitalize() == "Q":
                keepGoing = False
                
            elif userChoice == "":
                print(" ")
                print("Playing again...")

                player1.hitPoints = random.randint(0,40)
                player1.hitChance = random.randint(0,100)
                player1.maxDamage = random.randint(1,15)
                player1.armor = random.randint(0,5)

                player2.hitPoints = random.randint(0,40)
                player2.hitChance = random.randint(0,100)
                player2.maxDamage = random.randint(1,15)
                player2.armor = random.randint(0,5)

                player1.printStats()
                player2.printStats()

                fightPlayer(player1,player2)
            
            else:
                print("Invalid Response. Quitting game")
                keepGoing = False
            
       except UnboundLocalError:
           pass
           #Intentionally left blank. I did this because I don't wnat the program to crash when the user hasn't lost yet and its checking to play again.
           

#Loads the monsters into a dictionary
def load(filePath):

    try:
        with open(filePath,"r") as file:
            monsters = json.load(file)
        
        return monsters
    
    except TypeError:
        print("File not found. Please make sure 'tbc_gameData' is in the current directory.")
    
    
#Find the file if it is in the current directory and creates the file path
def findFile(fileName):
     rootDir = os.getcwd()

     for dirPath,dirName,files in os.walk(rootDir):
        
        if fileName in files:

            fullPath = os.path.join(rootDir,dirPath,fileName)

            return fullPath


#Creates a monster and saves it to the file
def createMonster(monsters,filePath):
    print(" ")

    try:
        nameInput = input("What will your monster's name be?: ")
        hpInput = int(input("What will it's HP be?: "))
        hitChanceInput = int(input("What will it's hit chance be?: "))
        maxDamageInput = int(input("What will it's max damage be?: "))
        armorInput = int(input("What will it's armor be?: "))

        monsters[nameInput] = [nameInput,hpInput,hitChanceInput,maxDamageInput,armorInput]

        with open(filePath, "w") as file:
            monsters = json.dump(monsters,file,indent=2)
        
    
    except ValueError:
        print("Error. Make sure you are entering the correct type")
        createMonster(monsters,filePath)
    
    except TypeError:
        print("Cannot use this feature without the game file. Please make sure 'tbc_gameData.json' is in the current directory.")
    

#Main function for testing purposes
def main():
    keepGoing = True

    while keepGoing:
        userChoice = menu()
    
        if userChoice == "1":
            player1 = buildCharacter("player1")
            player2 = buildCharacter("player2")
            player1.printStats()
            player2.printStats()
            fightPlayer(player1,player2)

        
        elif userChoice == "4":
            keepGoing = False

#Calling of main
if __name__ == "__main__":
    main()