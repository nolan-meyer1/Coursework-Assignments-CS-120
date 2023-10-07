import json
"""
Adventure Game Editor

Text adventure editor. Where you can input
a game file, save a game file, and edit 
a game file. 

Nolan Meyer, Carter Leckron

October 4, 2023

"""

#Prints the menu and lets the user make a choice
def getMenuChoice():
    print(""" 
0) exit
1) load default game
2) load a game file
3) save the current game
4) edit or add a node
5) play the current game
 """)
    
    keepGoing = True

    while keepGoing:
        userChoice = input("What will you do?: ")

        if userChoice in ("0","1","2","3","4","5"):
            keepGoing = False
        
        else:
            print("Invalid Response. Please enter 0,1,2,3,4 or 5")
        

    return userChoice


#Creates the default game [desc,menuA,nodeA,menuB,nodeB]
def getDefaultGame():

    game = {

        "start": ["Default start node","Start over","start","Quit","quit"]
    }

    return game


#Plays the current game
def playGame(gameDB):

    keepGoing = True
    currentNode = playNode(gameDB,"start")
    
    while keepGoing:
        
        if currentNode == "quit":
            keepGoing = False
        
        else:
            currentNode = playNode(gameDB,currentNode)
        

#Plays the node
def playNode(gameDB,node):
    
    if node in gameDB.keys():

        print(" ")
        print(gameDB[node][0])
        print(f"1) {gameDB[node][1]}")
        print(f"2) {gameDB[node][3]}")
        userChoice = input("Your choice: ")

        if userChoice == "1":
            newNode = gameDB[node][2]
    
        elif userChoice == "2":
            newNode = gameDB[node][4]
    
        else:
            print("Invalid Response. Please enter 1 or 2")
            newNode = node
    
    else:
        print(f"Invalid node. {node} doesn't exist")
        newNode = "quit"

    
    return newNode

#Saves the current game to a json file
def saveGame(gameDB):

    with open("game.json","w") as file:
        json.dump(gameDB,file,indent=2)
    
    print(" ")
    print("Saved game to game.json")
    print(json.dumps(gameDB,indent=2))


#Loads the game.json file
def loadGame():
    
    with open("game.json","r") as file:
        game = json.load(file)
    
    print("Loaded game.json")
    
    return game


#Allows you to edit the node/create a game
def editNode(gameDB):
    
    print("Current status of entire game")
    print(gameDB)
    print(" ")
    print("Current nodes: ")

    for node in gameDB.keys():
        print(node)
    
    userInput = input("Choose node to edit or enter a new node name: ")

    if userInput in gameDB.keys():
        editField(gameDB,userInput)
    
    else:
        gameDB[userInput] = [" ", " ", " ", " ", " "]
        editField(gameDB,userInput)


#Allows you to edit the fields of the node
def editField(gameDB,node):
    
    gameStructure = ("Description", "Menu A", "Node A", "Menu B","Node B")

    for index,item in enumerate(gameDB[node]):
        
        userInput = input(f"{gameStructure[index]} ({gameDB[node][index]}): ")

        if userInput == "":

            gameDB[node][index] = item
        
        else:
            gameDB[node][index] = userInput


#Main function
def main():
    keepGoing = True
    gameDB = getDefaultGame()

    while keepGoing:
        userChoice = getMenuChoice()

        if userChoice == "0":
            keepGoing = False
        
        elif userChoice == "1":
            gameDB = getDefaultGame()
        
        elif userChoice == "2":
            gameDB = loadGame()
        
        elif userChoice == "3":
            saveGame(gameDB)
        
        elif userChoice == "4":
            editNode(gameDB)
            
        elif userChoice == "5":
            playGame(gameDB)

    
#Checks if the namespace is main. If it is then it will run the main function
if __name__ == "__main__":
    main()