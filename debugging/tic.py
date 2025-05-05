#!/usr/bin/env python3
"""
    Prints the Tic-Tac-Toe board.

    Description: This function displays the current state of the game board to the players.
    It prints out each row and adds a separator line between them.

    Parameters:
        board (list): A 2D list (3x3) representing the Tic-Tac-Toe game board.

    Returns:
        None: This function does not return any value.
"""
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Coordinates must be between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            exit()

def tic_tac_toe():
    while True:
        play_game()
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice != "y":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
