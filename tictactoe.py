import sys

ROW1 = ["[0]","[1]","[2]"]
ROW2 = ["[3]","[4]","[5]"]
ROW3 = ["[6]","[7]","[8]"]
START = True
def display(a,b,c):
    """ displays the entire game board """
    clear_output()
    print("""

""")
    print(a)
    print(b)
    print(c)
    print("""

""")
def tie_game():
    """ Looks for conditions that constitute a tie"""
    if (ROW1[0] == "[o]" or ROW1[0] == "[x]"):
        if (ROW1[1] == "[o]" or ROW1[1] == "[x]"):
            if(ROW1[2] == "[o]" or ROW1[2] == "[x]"):
                if(ROW2[0] == "[o]" or ROW2[0] == "[x]"):
                    if(ROW2[1] == "[o]" or ROW2[1] == "[x]"):
                        if(ROW2[2] == "[o]" or ROW2[2] == "[x]"):
                            if(ROW3[0] == "[o]" or ROW3[0] == "[x]"):
                                if(ROW3[1] == "[o]" or ROW3[1] == "[x]"):
                                    if(ROW3[2] == "[o]" or ROW3[2] == "[x]"):
                                        print("""


                                                """)
                                        print("tie!")
                                        print("*************************************")
                                        display(ROW1, ROW2, ROW3)
                                        print("*************************************")
                                        start_menu()
def game_end():
    """Looks for conditions by which the game will end"""
    if ROW1[0] == "[x]" and ROW1[1] == "[x]" and ROW1[2] == "[x]":
        print("""


""")
        print("x wins! Straight across the first ROW!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[0] == "[x]" and ROW2[1] == "[x]" and ROW3[2] == "[x]":
        print("""


""")
        print("""


""")
        print("x wins! Diagonal win!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[2] == "[x]" and ROW2[1] == "[x]" and ROW3[0] == "[x]": 
        print("""


""")
        print("x wins! Diagonal win!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW2[0] == "[x]" and ROW2[1] == "[x]" and ROW2[2] == "[x]":
        print("""


""")

        print("x wins! Straight across the second ROW!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW3[0] == "[x]" and ROW3[1] == "[x]" and ROW3[2] == "[x]":
        print("""


""")
        print("x wins! Straight across the third ROW!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[0] == "[x]" and ROW2[0] == "[x]" and ROW3[0] == "[x]":
        print("""


""")
        print("x wins! Straight down the first column!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[1] == "[x]" and ROW2[1] == "[x]" and ROW3[1] == "[x]":
        print("""


""")
        print("x wins! Straight down the second column!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[2] == "[x]" and ROW2[2] == "[x]" and ROW3[2] == "[x]":
        print("""


""")
        print("x wins! Straight down the third column!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[0] == "[o]" and ROW1[1] == "[o]" and ROW1[2] == "[o]":
        print("""


""")
        print("o wins! Straight across the first ROW!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[0] == "[o]" and ROW2[1] == "[o]" and ROW3[2] == "[o]":
        print("""


""")
        print("o wins! Diagonal win!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[2] == "[o]" and ROW2[1] == "[o]" and ROW3[0] == "[o]":
        print("""


""")
        print("o wins! Diagonal win!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW2[0] == "[o]" and ROW2[1] == "[o]" and ROW2[2] == "[o]":
        print("""


""")
        print("o wins! Straight across the second ROW!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW3[0] == "[o]" and ROW3[1] == "[o]" and ROW3[2] == "[o]":
        print("""


""")
        print("o wins! Straight across the third ROW!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[0] == "[o]" and ROW2[0] == "[o]" and ROW3[0] == "[o]":
        print("""


""")
        print("o wins! Straight down the first column!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[1] == "[o]" and ROW2[1] == "[o]" and ROW3[1] == "[o]":
        print("""


""")
        print("o wins! Straight down the second column!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    elif ROW1[2] == "[o]" and ROW2[2] == "[o]" and ROW3[2] == "[o]":
        print("""


""")
        print("o wins! Straight down the third column!")
        print("*************************************")
        display(ROW1, ROW2, ROW3)
        print("*************************************")
        start_menu()
    else:
        tie_game()

def start_menu():
    """Creates a start menu that can start a game and end the program"""
    while START:
        play = input("Play a game? y/n? ")
        if play == "y":
            global ROW1, ROW2, ROW3
            ROW1 = ["[0]","[1]","[2]"]
            ROW2 = ["[3]","[4]","[5]"]
            ROW3 = ["[6]","[7]","[8]"]
            tic_tac_toe()
        elif play == "n":
            sys.exit()
        else:
            print("Please type 'y' or 'n'")
def tic_tac_toe():
    """the code of the game itself"""
    turnx = True
    while True:
        while turnx:
            game_end()
            display(ROW1, ROW2, ROW3)
            try:
                user = int(input("Which square would you like to add an x to? "))
                if user in range(0,3):
                    if ROW1[user] == "[x]":
                        print("choose a square that is not taken already")                        
                    elif ROW1[user] == "[o]":
                        print("choose a square that is not taken already")                            
                    else:
                        ROW1[user] = "[x]"
                        turnx = False
                elif user in range(3,6):
                    if ROW2[user-3] == "[x]":
                        print("choose a square that is not taken already")                    
                    elif ROW2[user-3] == "[o]":
                        print("choose a square that is not taken already")                    
                    else:
                        ROW2[user-3] = "[x]"
                        turnx = False
                elif user in range(6,9):
                    if ROW3[user-6] == "[x]":
                        print("choose a square that is not taken already")                   
                    elif ROW3[user-6] == "[o]":
                        print("choose a square that is not taken already")                        
                    else:
                        ROW3[user-6] = "[x]"
                        turnx = False
            except:
                print("Type a valid number")
        while not turnx:
            game_end()
            display(ROW1, ROW2, ROW3)
            try:
                user = int(input("Which square would you like to add an o to? "))
                if user in range(0,3):
                    if ROW1[user] == "[x]":
                        print("choose a square that is not taken already")
                    elif ROW1[user] == "[o]":
                        print("choose a square that is not taken already")
                    else:
                        ROW1[user] = "[o]"
                        turnx = True
                elif user in range(3,6):
                    if ROW2[user-3] == "[x]":
                        print("choose a square that is not taken already")
                    elif ROW2[user-3] == "[o]":
                        print("choose a square that is not taken already")
                    else:
                        ROW2[user-3] = "[o]"
                        turnx = True
                elif user in range(6,9):
                    if ROW3[user-6] == "[x]":
                        print("choose a square that is not taken already")
                    elif ROW3[user-6] == "[o]":
                        print("choose a square that is not taken already")
                    else:
                        ROW3[user-6] = "[o]"
                        turnx = True
            except:
                print("Type a valid number")      
start_menu()
