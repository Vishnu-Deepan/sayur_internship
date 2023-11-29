# Problem #2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions



import random

def initialize_board():
    return [['*' for _ in range(6)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(' '.join(row))

def roll_dice():
    return random.randint(1, 6)

def play_game():
    board = initialize_board()
    score_a = 0
    score_b = 0

    def update_board(player, row, col):
        nonlocal score_a, score_b

        if board[row][col] == 'A' and player == 'B':
            score_a += 1
            board[row][col] = 'A'
        elif board[row][col] == 'B' and player == 'A':
            score_b += 1
            board[row][col] = 'B'
        else:
            board[row][col] = player

    print("Game starts here!")

    while score_a < 5 and score_b < 5:
        input("Player A, press Enter to roll the dice...")
        row_a, col_a = roll_dice() - 1, roll_dice() - 1
        update_board('A', row_a, col_a)

        print("\nPlayer A's turn:")
        print_board(board)
        print(f"Scores - A: {score_a}, B: {score_b}\n")

        input("Player B, press Enter to roll the dice...")
        row_b, col_b = roll_dice() - 1, roll_dice() - 1
        update_board('B', row_b, col_b)

        print("\nPlayer B's turn:")
        print_board(board)
        print(f"Scores - A: {score_a}, B: {score_b}\n")

    if score_a == 5:
        print("Player A wins!")
    else:
        print("Player B wins!")

# starting the game
play_game()
