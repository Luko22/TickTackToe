
def playttt():
    d= {"row1": [" ", " ", " "], "row2": [" ", " ", " "], "row3": [" ", " ", " "]}

    def disp(row1, row2, row3):
        print(row1)
        print(row2)
        print(row3)
        print()

    print("Welcome to Tic Tac Toe")
    
    disp(d["row1"], d["row2"], d["row3"])

    # print(list(d.values()))
    # print(any(" " in row for row in list(d.values())))

    def check_winner(d):
        # Check rows
        for row in d.values():
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        # Check columns
        for col in range(3):
            if d["row1"][col] == d["row2"][col] == d["row3"][col] and d["row1"][col] != " ":
                return d["row1"][col]
        # Check diagonals
        if d["row1"][0] == d["row2"][1] == d["row3"][2] and d["row1"][0] != " ":
            return d["row1"][0]
        elif d["row1"][2] == d["row2"][1] == d["row3"][0] and d["row1"][2] != " ":
            return d["row1"][2]
        return None
    
    player=0
    acc_values = [1,2,3]

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

    print ("Game Over")

    winner = check_winner(d)
    if winner == None:
        print("It's a tie!")
    elif winner == "X":
        print(f"Player 1 wins!")
    else:
        print(f"Player 2 wins!")
    

playttt()
