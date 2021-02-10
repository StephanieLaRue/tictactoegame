
def create_board():
    board = board = [[" "] * 3, [" "] * 3, [" "] * 3]
    return board

def display_menu():
    print("-"*15)
    print("Tic Tac Toe!")
    print("-"*15, "\n")
    print("1. Play two Player Game")
    print("2. Play Computer")
    print("3. Quit")

    selection = input("Make a selection: ")
    return selection

def display_board(board):
    print("-"*15)
    for i in range(0, len(board)):
        print(board[i])
    print("-"*15)

def choose_token():
    player_one = input("Player One, choose your token: ")
    return player_one

def play_game(board, player):

    plays = 0
    current_turn = player.upper()

    while True:
        taken = "n"
        token = " "

        try:
            print("It's ", current_turn, "'s turn.")
            row = int(input("\nPostion One: "))
            col = int(input("\nPostion Two: "))

            for i in range(len(board)):
                if board[row][col] != " ":
                    taken = "y"

            if row < 0 or row > 2:
                print("\nInvalid Row Selection -- Choose a number between 0 and 2!")
            if col < 0 or col > 2:
                print("\nInvalid Column Selection -- Choose a number between 0 and 2!")
            elif taken == "y":
                print("Space is taken. Choose another space.")
                display_board(board)
            else:
                board[row][col] = current_turn
                current_turn = switch_token(current_turn)
                display_board(board)
                plays += 1
        except ValueError:
            continue

        if plays > 3:
            token = check_score(board)
        if token == "X" or token == "O":
            break
        if plays == 9 and token == " ":
            score_card(token)
            break


def check_score(board):
    token = " "
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and board[row][0] != " ":
            token = board[row][0] 
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] != " ":
            token = board[0][col] 
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != " ":
        token = board[0][0] 
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != " ":
        token = board[0][2] 

    if token != " ":
        score_card(token)
        return token


def score_card(token):
    if token == "X":
        print("\nX is the winner!\n")
    elif token == "O":
        print("\nO is the winner!\n")
    else:
        print("\nThere was a tie!\n")

def switch_token(player_token):
    if player_token == "X":
        return "O"
    elif player_token == "O":
        return "X"

def main():
    while True:
        board = create_board()
        choice = display_menu()

        if choice == "3":
            break
        elif choice == "2":
            display_board(board)
            print("\nIn Progress....\n")
        elif choice == "1":
            display_board(board)
            player = choose_token()
            play_game(board, player)
        else:
            print("\nInvalid selection.\n")
            
    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()