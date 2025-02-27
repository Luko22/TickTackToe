def playttt():
    # I considered each row as a list in a dictionary
    d = {"row1": [" ", " ", " "], "row2": [" ", " ", " "], "row3": [" ", " ", " "]}
    
    # Function to display the board
    def disp(row1, row2, row3):
        print(row1)
        print(row2)
        print(row3)
        print()

    print("Welcome to Tic Tac Toe")
    disp(d["row1"], d["row2"], d["row3"])

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

    player = 0
    acc_values = [1, 2, 3]
    alr_played = []
    
    def plays(row, col):
        if (int(row), col+1) not in alr_played:
            alr_played.append((int(row), col+1))
            return True
        else:
            print("This position is already played, please choose another one")
            return False

    while any(" " in row for row in list(d.values())) and check_winner(d) is None:
    
        if player % 2 == 0:
            row = input("Player 1 Enter a row (1-3): ")
            while not row.isdigit() or int(row) not in acc_values:
                print("Wrong value, enter a DIGIT from 1 to 3")
                row = input("Player 1 Enter a row (1-3): ")

            col = input("Player 1 enter a column (1-3): ")
            while not col.isdigit() or int(col) not in acc_values:
                print("Wrong value, enter a DIGIT from 1 to 3")
                col = input("Player 1 enter a column (1-3): ")
            col = int(col) - 1

            if plays(row, col):
                if d["row" + row][col] == " ":
                    d["row" + row][col] = "X"
                    print(f"Player 1 played {row},{col + 1}")
                    # alr_played.append((int(row), col))
                    player += 1
                else:
                    print("This position is already played, please choose another one")
            print()
            print(alr_played)
            print()

        else:
            row = input("Player 2 Enter a row (1-3): ")
            while not row.isdigit() or int(row) not in acc_values:
                print("Wrong value, enter a DIGIT from 1 to 3")
                row = input("Player 2 Enter a row (1-3): ")

            col = input("Player 2 enter a column (1-3): ")
            while not col.isdigit() or int(col) not in acc_values:
                print("Wrong value, enter a DIGIT from 1 to 3")
                col = input("Player 2 enter a column (1-3): ")
            col = int(col) - 1

            if plays(row, col):
                if d["row" + row][col] == " ":
                    d["row" + row][col] = "O"
                    print(f"Player 2 played {row},{col + 1}")

                    # alr_played.append((int(row), col))
                    player += 1
                else:
                    print("This position is already played, please choose another one")
            print()
            print(alr_played)
            print()

        disp(d["row1"], d["row2"], d["row3"])

    print("Game Over")

    winner = check_winner(d)
    if winner is None:
        print("It's a tie!")
    elif winner == "X":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

playttt()
