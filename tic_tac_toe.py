def display_menu():
    print("-"*15)
    print("Tic Tac Toe!")
    print("-"*15, "\n")

def display_board(board):
    print("-"*15)
    for i in range(0, len(board)):
        print(board[i])
    print("-"*15)

def play_game(row1):

    plays = 9
    while plays > 0:
        user_choice = int(input("\nSelect a space: "))

        if user_choice < 1 or user_choice > 3:
            print("\nInvalid Selection -- Choose a number between 1 and 3!")
        # check for string input -- loop again if not a number or not in range

        # check for empty space or not -- loop again if space is taken

        # append input and reload the board

        row1[0][0] = " "
        row1[1][0] = "X"
        row1[1][1] = " "
        row1[1][2] = "X"
        row1[0][2] = "X"
        row1[2][1] = "O"
        row1[2][2] = "O"
        plays -= 1
        display_board(row1)

        token = ''
        count = 0
        ocount = 0

        # include diagonal wins
        for i in range(len(row1)):
            for j in range(len(row1[i])):
                if row1[i][j] == "X" and row1[i][j] != " ":
                    count += 1
                    if count == 3:
                        token = "X"
                        score_card(token)
                else:
                    count = 0
                if row1[i][j] == "O" and row1[i][j] != " ":
                    ocount += 1
                    if ocount == 3:
                        token = "O"
                        score_card(token)
                else:
                    ocount = 0
        for p in range(len(row1)):
            for r in range(len(row1[p])):
                if row1[r][p] == "X" and row1[r][p] != " ":
                    count += 1
                    if count == 3:
                        token = "X"
                        score_card(token)
                else:
                    count = 0
                if row1[r][p] == "O" and row1[r][p] != " ":
                    ocount += 1
                    if ocount == 3:
                        token = "O"
                        score_card(token)
                else:
                    ocount = 0
    score_card(token)

def score_card(token):
    if token == "X":
        print("X is the winner!")
    elif token == "O":
        print("O is the winner!")
    else:
        print("There was a tie!")



def main():

    row1 = [[" "] * 3, [" "] * 3, [" "] * 3]

    # include prompts in menu for playing again
    # allow choice of player names
    # randomize x or o
    # allow selection of token
    display_menu()
    display_board(row1)
    play_game(row1)


if __name__ == "__main__":
    main()