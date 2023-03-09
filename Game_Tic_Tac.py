# Tic Tac Toe game

# Define the board
board = [' ' for x in range(10)]

# Function to print the board
def print_board():
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')

# Function to check if a player has won
def check_win(player):
    return (board[1] == board[2] == board[3] == player or
            board[4] == board[5] == board[6] == player or
            board[7] == board[8] == board[9] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[3] == board[6] == board[9] == player or
            board[1] == board[5] == board[9] == player or
            board[3] == board[5] == board[7] == player)

# Function to check if the board is full
def check_tie():
    return ' ' not in board[1:]

# Function to get the player's move
def get_move(player):
    position = input("Player " + player + "'s turn. Enter a position from 1-9: ")
    while position not in '1 2 3 4 5 6 7 8 9'.split() or board[int(position)] != ' ':
        position = input("Invalid move. Enter a position from 1-9: ")
    return int(position)

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Player 1 move
        position = get_move("X")
        board[position] = "X"
        print_board()
        if check_win("X"):
            print("Congratulations, Player X has won!")
            break
        elif check_tie():
            print("The game is a tie!")
            break

        # Player 2 move
        position = get_move("O")
        board[position] = "O"
        print_board()
        if check_win("O"):
            print("Congratulations, Player O has won!")
            break
        elif check_tie():
            print("The game is a tie!")
            break

play_game()
