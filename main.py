# Global Variables
player_turn = "X"
is_game_over = True
winner = None

# Board to be displayed
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

def display_board():
    ''' This is the function for display the board'''
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    ''' This is the main function where the whole game is run'''
    display_board()

    while is_game_over:
        handle_turn(player_turn)

        game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")

def handle_turn(player):
    '''This is the function to handle the turn of the players'''
    print(player + "'s turn.")
    validInput = ["1","2","3","4","5","6","7","8","9"]
    valid = False
    while not valid:
        pos = input("Choose a position from 1-9: ")
        while pos not in validInput:
            pos = input("Choose a position from 1-9: ")
        pos = int(pos)-1

        if board[pos] == "-":
          valid = True
        else:
          print("You can't go there. Try again!")
    board[pos] = player
    display_board()

def game_over():
    '''Function to make the decision of the game'''
    game_winner()
    game_tie()

def game_winner():
    '''Function to make the decision of the winner'''
    global winner

    row_win = row_match()
    col_win = column_match()
    diag_win = diagonal_match()
    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diag_win:
        winner = diag_win
    else:
        winner = None

def row_match():
    '''Function to check row match'''
    global is_game_over

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        is_game_over = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def column_match():
    '''Function to check column match'''
    global is_game_over

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        is_game_over = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def diagonal_match():
    '''Function to check diagonal match'''
    global is_game_over

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        is_game_over = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return  


def game_tie():
    '''Function to make the tie decision'''
    global is_game_over

    if "-" not in board:
      is_game_over = False
    return

def flip_player():
    '''Function to flip the chance of the players'''
    global player_turn

    if player_turn == "X":
      player_turn = "O"
    else:
      player_turn = "X"
    return
    
if __name__ == "__main__": 
    # Staring point of the game
    play_game()