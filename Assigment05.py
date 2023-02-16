# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KClarke,2.14.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
lstRow = []  # to hold a line from a file
dicRow = {}    # A row of data separated into elements {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
isRunning = True  # starts and controls the outermost menu loop
isFound = False  # for removing items

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of
# dictionaries rows (like Lab 5-2)
try:  # try to read in a file
    objFile = open(strFile, "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable += [dicRow]
    objFile.close()
except:  # if a file isn't found don't worry about it
    print("\nFile not found.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while isRunning:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? /"
                      "[1 to 5] - ").strip()
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice == '1':
        if len(lstTable) == 0:
            print("Carpe diem!")
        else:
            for row in lstTable:
                print(row['Task'] + ", " + row['Priority'])

    # Step 4 - Add a new item to the list/Table
    elif strChoice == '2':
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority + "\n"}
        lstTable += [dicRow]
        strChoice = input("Exit? ('y/n'): ").strip()
        if strChoice.lower() == "y":
            isRunning = False

    # Step 5 - Remove a new item from the list/Table
    elif strChoice == '3':
        strItem = input("Task to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strItem.lower():
                isFound = True
                lstTable.remove(row)
        if isFound:
            print("Task removed!")
        else:
            print("Task not found.")

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice == '4':
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Data saved.")

    # Step 7 - Exit program
    elif strChoice == '5':
        isRunning = False  # and Exit the program

    else:
        print("Please enter [1 to 5]")
