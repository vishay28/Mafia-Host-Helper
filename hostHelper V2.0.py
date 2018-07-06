#Import tkinter which is the GUI package
from tkinter import *

#A function to generate the check buttons
def generateCheckbutton(textValues, window, startingRow):
    #Creating a list to store the generated check buttons in in order to refer back to them
    checkButtons = {}
    #Assigning the starting row to the variable row
    row=startingRow
    #Setting the value of column to 0
    column=0
    #Creating a for loop to generate the check buttons
    for text in textValues:
        #Checking if the check button ha exceeded the dimensions of the window
        if row > 3:
            #Going to the next column
            column += 1
            #Resetting the row to the start row
            row = startingRow
        #Creating a variable to store the check button status
        checkButtons[text] = IntVar()
        #Creating the check button
        checkButton = Checkbutton(window, text=text, variable = checkButtons[text])
        #Defining where the check button will be located
        checkButton.grid(row=row, column=column, sticky=W)
        #Adding one to the row
        row += 1
    #Returning the generated check buttons
    return checkButtons

#A function to generate labels from a list of text
def generateLabels(labelText, window, startingRow, startingColumn, rowIncriment, columnIncriment, maxRow, **options):
    #Setting the variables of row and column to their starting value
    row = startingRow
    column = startingColumn
    #Creating a for loop to create the labels
    for text in labelText:
        #Checking if the label has exceeded the dimensions of the window
        if row > maxRow:
            #If it does exceed the window the column will incriment
            column = column + columnIncriment
            #The row is resetted to the starting value
            row = startingRow
        #Creating the label
        lbl = Label(window, text=text)
        #Assigning where the label will be placed
        lbl.grid(row=row, column=column, **options)
        #Incrimenting the row
        row = row + rowIncriment

#A function to generate entries from a list of text
def generateEntries(entryName, window, startingRow, startingColumn, rowIncriment, columnIncriment, maxRow, **options):
    #Setting the variables of row and column to their starting value
    row = startingRow
    column = startingColumn
    #Creating a list to store the generated entries in to refer back to them later
    entries = {}
    #Creating a for loop to create the entries
    for name in entryName:
        #Checking if the check button has exceeded the dimensions of the window
        if row > maxRow:
            #If it does exceed the window the column will incriment
            column = column + columnIncriment
            #The row is resetted to the starting value
            row = startingRow
        #Creating the entry
        entry = Entry(window)
        #Assigning where the entry will be placed
        entry.grid(row=row, column=column, **options)
        #Incrimenting the row
        row = row + rowIncriment
        #Storing the generated entry in the array
        entries[name] = entry
    #Returning the generated entries
    return entries

#A function to generate option menus
def generateRoleOptionMenus(optionMenuName, optionList, window, startingRow, startingColumn, rowIncriment, columnIncriment, maxRow, **options):
    #Setting the variables of row and column to their starting value
    row = startingRow
    column = startingColumn
    #Creating a list to store the generated option menus in to refer back to them later
    optionMenus = {}
    #Creating a for loop to create the option menus
    for name in optionMenuName:
        #Assigning the option menu a variable to check the value of it later
        optionMenus[name] = StringVar(window)
        #Setting the values of the option menu using the option list
        optionMenus[name].set(optionList[len(optionList)-1])
        #Checking if the check button has exceeded the dimensions of the window
        if row > maxRow:
            #If it does exceed the window the column will incriment
            column = column + columnIncriment
            #The row is resetted to the starting value
            row = startingRow
        #Creating the option menu
        optionMenu = OptionMenu(window, optionMenus[name], *optionList).grid(row=row, column=column, **options)
        #Incrimenting the row
        row = row + rowIncriment
    #Retuning the variables of the generated option menus
    return optionMenus

#A function to generate a list of all the roles that are being played with
def generateOptionsList():
    #Creating a list to store the options in
    optionsList = []
    #Creating a for loop to check which roles are being played with
    for role in roles:
        #Checking if the role has been selected
        if setupCheckButtons[role].get():
            #If it has then adding it to the list
            optionsList.append(role)
    #Returning the list with all roles that the user wants to play with
    return optionsList

#A function to run after the first setup window
def submit1Complete():
    #Creating a global variable for the number of players
    global numberOfPlayers
    #Assigning the value for the number of players
    numberOfPlayers = numberOfPlayersEntry.get()
    numberOfPlayers = int(numberOfPlayers)
    #Destroying the first setup window
    setup.destroy()

#A function to run after the second setup window
def submit2Complete():
    #Creating a global variable for the list that sorts out the players by role
    global playersByRoles
    #Creating a global variable for the list of player names
    global playerNames
    playerNames = []
    #Creating a for loop to generate the players name list
    for name in playerLabels:
        #Adding each player's name to the list
        playerNames.append(nameEntry[name].get())
    #Setting the two counters to 0
    a=0
    b=0
    #Creating the two dimensional list for the amount of players playing
    playersByRoles = [[0 for i in range(2)] for j in range(numberOfPlayers)]
    #Creating a for loop to populate the list
    for role in currentRolesList:
        for name in playerLabels:
            if roleOptionMenus[name].get()==role:
                playersByRoles[a][b] = nameEntry[name].get()
                playersByRoles[a][b+1] = role
                a = a + 1
    #Destroying the second setup window
    setup.destroy()

#A function to generate the gameplay screen
def generateGameplay(window, currentRolesList, numberOfPlayers, playersByRoles):
    #Setting the value for column to 0
    column=0
    #Creating a list to store the generated tick boxes
    checkButtons = {}
    #Creating a for loop to generate the check buttons
    for role in currentRolesList:
        #Setting the value of the counter to 0
        a=0
        #Setting the value of where the check buttons should start
        row = 2
        #Creating a while loop to iterate through all the players
        while a<numberOfPlayers:
            #Checking which is the current role selected by the for loop
            if playersByRoles[a][1]==role:
                #Assigning a variable to the check button
                checkButtons[playersByRoles[a][0]] = IntVar()
                #Creating the check button and assigning the location of it
                chkBut = Checkbutton(window, text=(playersByRoles[a][0]), variable=checkButtons[playersByRoles[a][0]]).grid(row=row, column=column, padx=10, pady=5, sticky=W)
                #Incrimenting the row
                row = row + 1
            #Incrimenting the counter
            a = a + 1
        #Incrimenting the column
        column = column + 1
    #Returning the generated check buttons
    return checkButtons

#A function to run once the mafia have selected who to kill
def mafiaSubmit():
    #Creating a global variable to store who the mafia killed
    global killedByMafia
    #Creating a for loop to determine who was chosen by the mafia to be killed
    for name in playerNames:
        #Checking if the player was selected
        if playerCheckButtons[name].get():
            #Assigning the variable to the player that was selected to be killed
            killedByMafia = name
    #Destroying the gameplay window
    gameplay.destroy()

#A function to run once the doctor have selected who to save
def doctorSubmit():
    #Creating a global variable to store who the doctor saved
    global savedByDoctor
    #Creating a for loop to determine who was chosen by the doctor to be saved
    for name in playerNames:
        #Checking if the player was selected
        if playerCheckButtons[name].get():
            #Assigning the variable to the player that was selected to be saved
            savedByDoctor = name
    #Destroying the gameplay window
    gameplay.destroy()

#A function to run once the investigator has selected who to investigate
def investigatorSubmit():
    #Creating a global variable to store the name and role of the person investigated
    global investigatedArray
    #Creating a for loop to determine who was chosen by the investigator
    for name in playerNames:
        #Checking if the player was selected
        if playerCheckButtons[name].get():
            #Assigning the variable to the player that was selected to be investigated
            investgated = name
    #Creating a for loop to check what the role was of the player selected
    for i, j in enumerate(playersByRoles):
        if investgated in j:
            #Adding the name and role to an array
            investigatedArray = playersByRoles[i]
    #Destroying the window for the investigator input
    gameplay.destroy()

def destroyInvestigatorWindow():
    investigatorWindow.destroy()
    
def destroyArsonistWindow():
    global arsonLight
    arsonLight = True
    arsonistWindow.destroy()
    
def nextArsonistWindow():
    arsonistWindow.destroy()
    
def arsonistSubmit():
    for name in playerNames:
        #Checking if the player was selected
        if playerCheckButtons[name].get():
            #Assigning the variable to the player that was selected to be investigated
            doused = name
    arsonedArr.append(doused)
    gameplay.destroy()

def endGameSubmit():
    endGameWindow.destroy()

def nightInfoSubmit():
    nightInfo.destroy()

#A function to run once the mafia have selected who to kill
def votedSubmit():
    #Creating a global variable to store who the mafia killed
    global votedOff
    #Creating a for loop to determine who was chosen by the mafia to be killed
    for name in playerNames:
        #Checking if the player was selected
        if playerCheckButtons[name].get():
            #Assigning the variable to the player that was selected to be killed
            votedOff = name
    #Destroying the gameplay window
    dayWindow.destroy()


#-------------------------------SETUP 1-----------------------------------------
#Creating a window and titling it
setup = Tk()
setup.title("Setup")

#Setting the height and width of the setup window
width, height = setup.winfo_screenwidth(), setup.winfo_screenheight()
#Setting the height and width to a fourth of the screen size
setup.geometry('%dx%d+0+0' % (width/4,height/9))
#Ensuring the setup window is ontop of the root window
setup.attributes("-topmost", True)

#Creating a label for the number of players entry field
numberOfPlayersLabel = Label(setup, text="How many players are there?")
#Assigning the location of the label
numberOfPlayersLabel.grid(row=0, column=0, sticky=W)

#Creating an entry field for the user to input the number of players
numberOfPlayersEntry = Entry(setup)
#Assigning the location of the entry field
numberOfPlayersEntry.grid(row=0, column=1, sticky=W)

#Creating a label for the roles check buttons
whatRolesLabel = Label(setup, text="What roles are you playing with?")
#Assigning the location of the label
whatRolesLabel.grid(row=1, column=0, sticky=W)

#Creating a list of all the availible roles
roles = ["Mafia", "Doctor", "Investigator", "Arsonist"]
#Creating a blank list to store the check buttons for the roles
setupCheckButtons = {}
#Creating the check buttons for the role selection
setupCheckButtons = generateCheckbutton(roles, setup, 2)

#Creating a button to submit the inputted information
submit1Button = Button(setup, text="Submit", command=submit1Complete)
#Assigning the location of the button
submit1Button.grid(column=0, sticky = SE)

#Creating a mainloop for the window
setup.mainloop()


#-------------------------------SETUP 2-----------------------------------------
#Creating a global variable to store the number of players
global numberOfPlayers
#Creating a window and titling it
setup = Tk()
setup.title("Name & Role Input")

#Setting the height and width of the setup window
width, height = setup.winfo_screenwidth(), setup.winfo_screenheight()
#Setting the height and width to a fourth of the screen size
setup.geometry('%dx%d+0+0' % (width/3,height/2.8))
#Ensuring the setup window is ontop of the root window
setup.attributes("-topmost", True)

#Creating a list for the headers
headerLabels = ["Player", "Name", "Role"]
#Generating the labels for the headers
generateLabels(headerLabels, setup, 0, 0, 1, 1, 0)

#Setting the counter to 1
i=1
#Creating a blank list to store the labels for the players
playerLabels=[]
#Creating a while loop to generate the labels for the players
while i<=numberOfPlayers:
    #Adding the player number to the list
    playerLabels.append("Player " + str(i) + ":")
    #Iterating the counter
    i += 1
#Generating the player labels
generateLabels(playerLabels, setup, 1, 0, 1, 3, 8, padx=5, pady=10, sticky=W)
#Generating the entries for the player's names
nameEntry = generateEntries(playerLabels, setup, 1, 1, 1, 3, 8, sticky=W)
#Creating a list of the roles that are being played with
currentRolesList = generateOptionsList()
#Adding the Townsman to the role list
currentRolesList.append("Townsman")
#Generating the option menus to select the roles
roleOptionMenus = generateRoleOptionMenus(playerLabels, currentRolesList, setup, 1, 2, 1, 3, 8, sticky=W)

#Creating the submit button
submitButton = Button(setup, text="Submit", command=submit2Complete)
#Assigning the location of the submit button
submitButton.grid(column=3, sticky = S)

#Creating a mainloop for the window
setup.mainloop()

#----------------------------------GAMEPLAY-------------------------------------
#Creating a global variable for the check buttons for the players
global playerCheckButtons
#Creating a global variable for the list that stores the players by role
global playersByRoles

global arsonedArr
arsonedArr = []
a = 0
while a<numberOfPlayers:
    #Checking which is the current role selected by the for loop
    if playersByRoles[a][1]=="Arsonist":
        arsonedArr.append(playersByRoles[a][0])
    a = a+1

#Creating a while loop to ru the main gameplay section
while True:
    #Clearing the values assigned to the killedByMafia and savedByDoctor variable
    killedByMafia = ""
    savedByDoctor = ""
    investgated = ""
    arsonLight = False
    arsoned = ""

#-------------------------MAFIA GAMEPLAY----------------------------------------
    #Checking if there are any mafia players still left
    if any("Mafia" in sublist for sublist in playersByRoles):
        #Creating a window for the gameplay and titling it
        gameplay = Tk()
        gameplay.title("Gameplay")
        #Setting the height and width of the setup window
        width, height = gameplay.winfo_screenwidth(), gameplay.winfo_screenheight()
        #Setting the height and width to a fourth of the screen size
        gameplay.geometry('%dx%d+0+0' % (width/3,height/2.8))
        #Ensuring the setup window is ontop of the root window
        gameplay.attributes("-topmost", True)
        #Assigning the action text to a variable
        actionText = StringVar()
        #Creating the action variable
        actionLabel = Label(gameplay, textvariable = actionText).grid(row=0, column=0, sticky=W)
        #Generating the labels for the current roles being played with
        generateLabels(currentRolesList, gameplay, 1, 0, 1, 1, 1, padx=10, sticky=W)
        #Creating the players check buttons
        playerCheckButtons = generateGameplay(gameplay, currentRolesList, numberOfPlayers, playersByRoles)

        #Setting the action text to tell the user to select who the mafia want to kill
        actionText.set("Who do the mafia want to kill?")
        #Create a submit button
        submitButton = Button(gameplay, text="Submit", command=mafiaSubmit)
        #Assigning the location of the button
        submitButton.grid(column=2, sticky = S)

        #Creating a mainloop for the gameplay window
        gameplay.mainloop()


#---------------------------------DOCTOR GAMEPLAY-------------------------------
    #Checking if any doctors are still left, if so then carrying out their role
    if any("Doctor" in sublist for sublist in playersByRoles):
        gameplay = Tk()
        gameplay.title("Gameplay")
        #Setting the height and width of the setup window
        width, height = gameplay.winfo_screenwidth(), gameplay.winfo_screenheight()
        #Setting the height and width to a fourth of the screen size
        gameplay.geometry('%dx%d+0+0' % (width/3,height/2.8))
        #Ensuring the setup window is ontop of the root window
        gameplay.attributes("-topmost", True)
        actionText = StringVar()
        actionLabel = Label(gameplay, textvariable = actionText).grid(row=0, column=0, sticky=W)
        generateLabels(currentRolesList, gameplay, 1, 0, 1, 1, 1, padx=10, sticky=W)
        playerCheckButtons = generateGameplay(gameplay, currentRolesList, numberOfPlayers, playersByRoles)

        #Setting the action text to tell the user to select who the doctors want to save
        actionText.set("Who do the doctors want to save?")
        #Create a submit button
        submitButton = Button(gameplay, text="Submit", command=doctorSubmit)
        #Assigning the location of the button
        submitButton.grid(column=2, sticky = S)

        #Creating a mainloop for the gameplay window
        gameplay.mainloop()

#-------------------------INVESTIGATOR GAMEPLAY---------------------------------
    #Checking if there are any mafia players still left
    if any("Investigator" in sublist for sublist in playersByRoles):
        #Creating a window for the gameplay and titling it
        gameplay = Tk()
        gameplay.title("Gameplay")
        #Setting the height and width of the setup window
        width, height = gameplay.winfo_screenwidth(), gameplay.winfo_screenheight()
        #Setting the height and width to a fourth of the screen size
        gameplay.geometry('%dx%d+0+0' % (width/3,height/2.8))
        #Ensuring the setup window is ontop of the root window
        gameplay.attributes("-topmost", True)
        #Assigning the action text to a variable
        actionText = StringVar()
        #Creating the action variable
        actionLabel = Label(gameplay, textvariable = actionText).grid(row=0, column=0, sticky=W)
        #Generating the labels for the current roles being played with
        generateLabels(currentRolesList, gameplay, 1, 0, 1, 1, 1, padx=10, sticky=W)
        #Creating the players check buttons
        playerCheckButtons = generateGameplay(gameplay, currentRolesList, numberOfPlayers, playersByRoles)

        #Setting the action text to tell the user to select who the investigator wants to investigate
        actionText.set("Who does the investigator want to investigate?")
        #Create a submit button
        submitButton = Button(gameplay, text="Submit", command=investigatorSubmit)
        #Assigning the location of the button
        submitButton.grid(column=2, sticky = S)

        #Creating a mainloop for the gameplay window
        gameplay.mainloop()

        #Creating a window to display the response to the investigator
        investigatorWindow = Tk()
        #Titling the window
        investigatorWindow.title("Investigator")
        investigatorWindow.attributes("-topmost", True)
        #Creating a string to store the name and role of the investigated player
        investigatedText = (investigatedArray[0] + " is " + investigatedArray[1])
        #Creating a label to output the information to the user
        investigatedLabel = Label(investigatorWindow, text=investigatedText)
        #Packing the label into the window
        investigatedLabel.pack()
        #Creating a button so that the user can continue
        investigatedButton = Button(investigatorWindow, text="Next", command=destroyInvestigatorWindow)
        #Packing the button into the window
        investigatedButton.pack()

        #Creating a mainloop in which to run the window
        investigatorWindow.mainloop()

#-------------------------------ARSONIST GAMEPLAY-------------------------------

    if any("Arsonist" in sublist for sublist in playersByRoles):
        arsonistWindow = Tk()
        arsonistWindow.title("Arsonist")
        arsonistWindow.attributes("-topmost", True)
        actionText = "Does the arsonist want to set the arsoned alight?"
        actionLabel = Label(arsonistWindow, text=actionText)
        actionLabel.pack()
        yesButton = Button(arsonistWindow, text="Yes", command=destroyArsonistWindow)
        yesButton.pack()
        noButton = Button(arsonistWindow, text="No", command=nextArsonistWindow)
        noButton.pack()
        arsonistWindow.mainloop()
        
        if not arsonLight:
            gameplay = Tk()
            gameplay.title("Gameplay")
            #Setting the height and width of the setup window
            width, height = gameplay.winfo_screenwidth(), gameplay.winfo_screenheight()
            #Setting the height and width to a fourth of the screen size
            gameplay.geometry('%dx%d+0+0' % (width/3,height/2.8))
            #Ensuring the setup window is ontop of the root window
            gameplay.attributes("-topmost", True)
            #Assigning the action text to a variable
            actionText = StringVar()
            #Creating the action variable
            actionLabel = Label(gameplay, textvariable = actionText).grid(row=0, column=0, sticky=W)
            #Generating the labels for the current roles being played with
            generateLabels(currentRolesList, gameplay, 1, 0, 1, 1, 1, padx=10, sticky=W)
            #Creating the players check buttons
            playerCheckButtons = generateGameplay(gameplay, currentRolesList, numberOfPlayers, playersByRoles)

            #Setting the action text to tell the user to select who the investigator wants to investigate
            actionText.set("Who does the arsonist want to douse in oil?")
            #Create a submit button
            submitButton = Button(gameplay, text="Submit", command=arsonistSubmit)
            #Assigning the location of the button
            submitButton.grid(column=2, sticky = S)

            #Creating a mainloop for the gameplay window
            gameplay.mainloop()

#----------------------------LOGIC----------------------------------------------
    #Assigning a variable to keep track if the doctor and the mafia picked the same people
    noneDied = False
    #Checking if the mafia and the doctors picked different people
    if killedByMafia != savedByDoctor:
        #Creating a for loop to determine the player that was killed
        for i, j in enumerate(playersByRoles):
            if killedByMafia in j:
                #Deleting the player from the playersByRoles and playerNames lists
                del playersByRoles[i]
                playerNames.remove(killedByMafia)
        #Reducing the number of players by 1
        numberOfPlayers = numberOfPlayers-1
    if arsonLight:
        if (killedByMafia != savedByDoctor):
            if killedByMafia in arsonedArr:
                arsonedArr.remove(killedByMafia)
        for arsoned in arsonedArr:
            for i, j in enumerate(playersByRoles):
                if arsoned in j:
                    #Deleting the player from the playersByRoles and playerNames lists
                    del playersByRoles[i]
                    playerNames.remove(arsoned)
        numberOfPlayers = numberOfPlayers-len(arsonedArr)
    #If not changing the variable to true
    else:
        noneDied = True


#--------------------------NIGHT INFO-------------------------------------------

    #Creating a window to display what happened in the night
    nightInfo = Tk()
    nightInfo.title("Night")
    nightInfo.attributes("-topmost", True)
    #Checking if no-one died
    if noneDied:
        whoDied = "Died: No-one died"
    #If not telling the user who died in the night
    elif killedByMafia == savedByDoctor:
        whoDied = ("Died: " + " ".join(arsonedArr))
    else:
        whoDied = ("Died: " + killedByMafia + " " + " ".join(arsonedArr))

    #Creating a label to display who died in the night
    deathLabel = Label(nightInfo, text = whoDied)
    deathLabel.pack()

    #Creating a button to move on to the next window
    nightInfoButton = Button(nightInfo, text = "Ok", command = nightInfoSubmit)
    nightInfoButton.pack()

    #Creating the main loop to run the window
    nightInfo.mainloop()
#------------------------------------------------------------------------------

    #Checking if the end of the game has occurred
    if (len(playersByRoles)<=2) | (not(any("Mafia" in sublist for sublist in playersByRoles))):
        break

#--------------------------------DAY--------------------------------------------
    votedOff = ""
    #Creating a window for the voting
    dayWindow = Tk()
    dayWindow.title("Day")
    #Setting the height and width of the setup window
    width, height = dayWindow.winfo_screenwidth(), dayWindow.winfo_screenheight()
    #Setting the height and width to a fourth of the screen size
    dayWindow.geometry('%dx%d+0+0' % (width/3,height/2.8))
    #Ensuring the setup window is ontop of the root window
    dayWindow.attributes("-topmost", True)
    #Creating all the labels and check buttons for the user to input who was voted off
    actionText = StringVar()
    actionLabel = Label(dayWindow, textvariable = actionText).grid(row=0, column=0, sticky=W)
    generateLabels(currentRolesList, dayWindow, 1, 0, 1, 1, 1, padx=10, sticky=W)
    playerCheckButtons = generateGameplay(dayWindow, currentRolesList, numberOfPlayers, playersByRoles)

    #Setting the action text to tell the user to select who was voted off
    actionText.set("Who was voted off?")
    #Create a submit button
    submitButton = Button(dayWindow, text="Submit", command=votedSubmit)
    #Assigning the location of the button
    submitButton.grid(column=2, sticky = S)

    #Creating a mainloop for the dayWindow window
    dayWindow.mainloop()
#-------------------------------------------------------------------------------

    if not(votedOff == ""):
        #Creating a for loop to determine the player that was voted off
        for i, j in enumerate(playersByRoles):
            if votedOff in j:
                #Deleting the player from the playersByRoles and playerNames lists
                del playersByRoles[i]
                playerNames.remove(votedOff)
        #Reducing the number of players by 1
        numberOfPlayers = numberOfPlayers-1

    #Checking if the game has ended
    if (len(playersByRoles)<=2) | (not(any("Mafia" in sublist for sublist in playersByRoles))):
        break


#------------------------END OF GAME--------------------------------------------

#Creating a window to let the user know who has won
endGameWindow = Tk()
endGameWindow.title("Game Over")
endGameWindow.attributes("-topmost", True)
gameOverLabel = Label(endGameWindow, text = "Game over!")
gameOverLabel.pack()

#Checking who has won
if not(any("Mafia" in sublist for sublist in playersByRoles)):
    whoWon = "Town Won"
elif any("Mafia" in sublist for sublist in playersByRoles):
    whoWon = "Mafia Win"
else:
    whoWon = "N/A"

#Creating a label to display who won
whoWonLabel = Label(endGameWindow, text = whoWon)
whoWonLabel.pack()
#Creating a button to end the game
endGameButton = Button(endGameWindow, text = "End Game", command = endGameSubmit)
endGameButton.pack()

#Creating a main loop for the window to run in
endGameWindow.mainloop()
