

start = True
def display(a,b,c):
    print("""

""")
    print(a)
    print(b)
    print(c)
    print("""

""")


def gameend():
   

    
    
        
        
        
        
    
        
    if row1[0] == "[x]" and row1[1] == "[x]" and row1[2] == "[x]":
        print("""


""")
        print("x wins! Straight across the first row!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row1[0] == "[x]" and row2[1] == "[x]" and row3[2] == "[x]":
        print("""


""")
        print("""


""")
        print("x wins! Diagonal win!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row1[2] == "[x]" and row2[1] == "[x]" and row3[0] == "[x]": 

        print("""


""")
        print("x wins! Diagonal win!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row2[0] == "[x]" and row2[1] == "[x]" and row2[2] == "[x]":
        print("""


""")

        print("x wins! Straight across the second row!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row3[0] == "[x]" and row3[1] == "[x]" and row3[2] == "[x]":
        print("""


""")
        print("x wins! Straight across the third row!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif row1[0] == "[x]" and row2[0] == "[x]" and row3[0] == "[x]":
        print("""


""")
        print("x wins! Straight down the first column!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif row1[1] == "[x]" and row2[1] == "[x]" and row3[1] == "[x]":
        print("""


""")
        print("x wins! Straight down the second column!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif row1[2] == "[x]" and row2[2] == "[x]" and row3[2] == "[x]":
        print("""


""")
        print("x wins! Straight down the third column!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif row1[0] == "[o]" and row1[1] == "[o]" and row1[2] == "[o]":
        print("""


""")
        print("o wins! Straight across the first row!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row1[0] == "[o]" and row2[1] == "[o]" and row3[2] == "[o]":
        print("""


""")
        print("o wins! Diagonal win!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row1[2] == "[o]" and row2[1] == "[o]" and row3[0] == "[o]":
        print("""


""")
        print("o wins! Diagonal win!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row2[0] == "[o]" and row2[1] == "[o]" and row2[2] == "[o]":
        print("""


""")
        print("o wins! Straight across the second row!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row3[0] == "[o]" and row3[1] == "[o]" and row3[2] == "[o]":
        print("""


""")
        print("o wins! Straight across the third row!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()
    elif row1[0] == "[o]" and row2[0] == "[o]" and row3[0] == "[o]":
        print("""


""")
        print("o wins! Straight down the first column!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif row1[1] == "[o]" and row2[1] == "[o]" and row3[1] == "[o]":
        print("""


""")
        print("o wins! Straight down the second column!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif row1[2] == "[o]" and row2[2] == "[o]" and row3[2] == "[o]":
        print("""


""")
        print("o wins! Straight down the third column!")
        print("*************************************")
        display(row1, row2, row3)
        print("*************************************")
        startmenu()

    elif (row1[0] == "[o]" or row1[0] == "[x]"):
        if (row1[1] == "[o]" or row1[1] == "[x]"):
            if(row1[2] == "[o]" or row1[2] == "[x]"):
               if(row2[0] == "[o]" or row2[0] == "[x]"):
                   if(row2[1] == "[o]" or row2[1] == "[x]"):
                        if(row2[2] == "[o]" or row2[2] == "[x]"):
                            if(row3[0] == "[o]" or row3[0] == "[x]"):
                               if(row3[1] == "[o]" or row3[1] == "[x]"):
                                   if(row3[2] == "[o]" or row3[2] == "[x]"):
                                        print("""


                                                """)
                                        print("tie!")
                                        print("*************************************")
                                        display(row1, row2, row3)
                                        print("*************************************")
                                        startmenu()


        else:
            pass
    else:
        pass

def startmenu():
    
    while start == True:
        play = input("Play a game? y/n? ")
        if play == "y":
            global row1, row2, row3

            row1 = ["[0]","[1]","[2]"]
            row2 = ["[3]","[4]","[5]"]
            row3 = ["[6]","[7]","[8]"]
            tictactoe()
            break
        
        elif play == "n":
                     
            quit()
        else:
            print("Please type 'y' or 'n'")

def tictactoe():
    
    turnx = True
    
    while True:
        
        
        while turnx == True:
                gameend()
                display(row1, row2, row3)
                try:
                    user = int(input("Which square would you like to add an x to? "))

            

                    if user in range(0,3):
                        if row1[user] == "[x]":
                            print("choose a square that is not taken already")
                        
                        elif row1[user] == "[o]":
                            print("choose a square that is not taken already")
                            
                        else:
                            row1[user] = "[x]"
                            turnx = False

                    elif user in range(3,6):
                        if row2[user-3] == "[x]":
                            print("choose a square that is not taken already")
                    
                        elif row2[user-3] == "[o]":
                            print("choose a square that is not taken already")
                    
                        else:
                            row2[user-3] = "[x]"
                        
                            turnx = False

                    elif user in range(6,9):

                        if row3[user-6] == "[x]":
                            print("choose a square that is not taken already")
                    
                        elif row3[user-6] == "[o]":
                            print("choose a square that is not taken already")
                        
                        else:
                            row3[user-6] = "[x]"
                        
                            turnx = False

                except:
                    print("Type a valid number")

        while turnx == False:
                gameend()
                display(row1, row2, row3)
                try:
                    user = int(input("Which square would you like to add an o to? "))
            
                    if user in range(0,3):
                        if row1[user] == "[x]":
                            print("choose a square that is not taken already")
                        
                        elif row1[user] == "[o]":
                            print("choose a square that is not taken already")
                        
                        else:
                            row1[user] = "[o]"
                            turnx = True

                    elif user in range(3,6):
                        if row2[user-3] == "[x]":
                            print("choose a square that is not taken already")
                    
                        elif row2[user-3] == "[o]":
                            print("choose a square that is not taken already")
                    
                        else:
                            row2[user-3] = "[o]"
                            turnx = True

                    elif user in range(6,9):

                        if row3[user-6] == "[x]":
                            print("choose a square that is not taken already")
                    
                        elif row3[user-6] == "[o]":
                            print("choose a square that is not taken already")
                    
                        else:
                            row3[user-6] = "[o]"
                            turnx = True
                except:
                    print("Type a valid number")


    
        
startmenu()

