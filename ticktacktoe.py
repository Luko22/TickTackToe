
def playttt():
    #I considered each row as a list in a dictionary
    d= {"row1": [" ", " ", " "], "row2": [" ", " ", " "], "row3": [" ", " ", " "]}
    #then I made a function to display the board
    def disp(row1, row2, row3):
        print(row1)
        print(row2)
        print(row3)
        print()

    print("Welcome to Tic Tac Toe")
    
    disp(d["row1"], d["row2"], d["row3"])

    #I used trial and error to figure out how to address them specific rows and columns
    # print(list(d.values()))
    # print(any(" " in row for row in list(d.values())))

    def check_winner(d):
        # Check row win
        for row in d.values():
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        # Check column win
        for col in range(3):
            if d["row1"][col] == d["row2"][col] == d["row3"][col] and d["row1"][col] != " ":
                return d["row1"][col]
        # Check diagonal win
        if d["row1"][0] == d["row2"][1] == d["row3"][2] and d["row1"][0] != " ":
            return d["row1"][0]
        elif d["row1"][2] == d["row2"][1] == d["row3"][0] and d["row1"][2] != " ":
            return d["row1"][2]
        return None
    
    #used even and odd to determine which player is playing
    player=0
    #used this to check if the row input is valid
    acc_values = [1,2,3]
    #used an empt list to store the played positions as tuples
    alr_played = []

    while any(" " in row for row in list(d.values())) and check_winner(d) == None:
        if player%2 == 0:
            row = input("Player 1 Enter a row (1-3)")

            while (row.isdigit==False) or (int(row) not in acc_values):
                print("Wrong value, enter a DIGIT from 1 to 3 ")
                row = input("Player 1 Enter a row (1-3) ")

            col = int(input("Player 1 enter a column "))-1
            while (type(col)!=int) :
                print("Wrong value, enter a DIGIT from 1 to 3")
                col = int(input("Player 1 enter a column "))-1

            d["row"+row][col]= "X"
            print(f"player 1 played {row},{col+1}")
            
            player+=1
            
        else:
            row = input("Player 2 Enter a row (1-3) ")
            while (row.isdigit==False) or (int(row) not in acc_values):
                print("Wrong value, enter a DIGIT from 1 to 3")
                row = input("Player 1 Enter a row (1-3) ")

            col = int(input("Player 2 enter a column "))-1
            while (type(col)!=int) :
                print("Wrong value, enter a DIGIT from 1 to 3")
                int(input("Player 2 e2nter a column "))-1

            d["row"+row][col]= "O"
            print(f"player 2 played {row},{col+1}")
            player+=1

        disp(d["row1"], d["row2"], d["row3"])
    

        if (int(row),col+1) not in alr_played
                alr_played.append((int(row),col+1))
            else:
                print("This position is already played, please choose another one")
                player-=1
        #end of while loop

        
    print ("Game Over")

    winner = check_winner(d)
    if winner == None:
        print("It's a tie!")
    elif winner == "X":
        print(f"Player 1 wins!")
    else:
        print(f"Player 2 wins!")
    

playttt()
