# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2023,Created started script
# mariika,2.12.23,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open ("ToDoList.txt", 'w')
dicRow = {"task": "Do homework" , "priority":"Medium"}
lstTable.append(dicRow)
objFile.write(dicRow["task"]+','+dicRow["priority"]+'\n')
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data in the table.
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File.
    5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        if len(lstTable) == 0: print("The table is empty")
        else:
            for dicRow in lstTable:
                print(dicRow["task"]+","+dicRow["priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        dicRow={"task":input("Please enter a task: "),
                "priority":input("Please enter a priority: ")}
        lstTable.append(dicRow)
        print("Entered items are added to the list, but not saved\n")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
       if len(lstTable) == 0: print("The table is empty\n")
       else:
           del lstTable[-1]
           print("The last added item removed\n")
       continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", 'w')
        for dicRow in lstTable:
            objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
        objFile.close()
        print("File updated!\n")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("See you next time \nProgram finished\n")
        exit()  # Exit the program
    else: 
        print("Please enter one of next options ['1' or '2' or '3' or '4' or '5']")
        continue