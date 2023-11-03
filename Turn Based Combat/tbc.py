import random
"""
A combat system module that has
the ability to create a character
with certain attributes. As well 
as having the fight function that
allows the characters to fight

Nolan Meyer, Max Hill

October 17, 2023
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
            print("You need a str value. Setting to Hero")
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
                 print("Positive integers greater than or equal to 0 only. Setting to 10")
                 self.__hitPoints = 10
        
        else:
            print("Only integers allowed. Setting to 10")
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
                print("Value must be between 0-100. Setting to 50.")
                self.__hitChance = 50
        
        else:
            print("Type must be integers. Setting to 50")
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
                print("Damage must be greater than 0. Setting to 10")
                self.__maxDamage = 10
        
        else:
            print("Only integers allowed. Setting to 10")
            self.__maxDamage = 10
    

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
                print("Must be greater than or equal to 0. Setting to 0")
                self.__armor = 0
        
        else:
            print("Positive integers allowed. Setting to 0")
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
    

#Fight function that allows two characters to fight
def fight(playerCharacter,monster):
    keepGoing = True
    userChoice = ""

    while keepGoing:    

       playerCharacter.hit(monster)
       monster.hit(playerCharacter)

       print("")
       print(f"{playerCharacter.name}: {playerCharacter.hitPoints} HP")
       print(f"{monster.name}: {monster.hitPoints} HP")
                
       if playerCharacter.hitPoints > 0:
           
            if monster.hitPoints > 0:

                userChoice = input("Press ENTER for another round or Q to quit: ")

            else:
                print(f"{playerCharacter.name} wins!")
                keepGoing = False

       else:
            print(f"{monster.name} wins!")
            keepGoing = False


       if userChoice.capitalize() == "Q":
           keepGoing = False


#Main function for testing purposes
def main():
    hero = Character()
    monster = Character("Werewolf",20,30,5,0)
    
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    hero.printStats()
    monster.printStats()

    fight(hero,monster)

#Calling of main
if __name__ == "__main__":
    main()