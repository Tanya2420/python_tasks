import random

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function for the computer's move (random)
def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe against the computer!")

    while True:
        display_board(board)

        if current_player == "X":
            row = int(input("Player X, enter row (0, 1, 2): "))
            col = int(input("Player X, enter column (0, 1, 2): "))
        else:
            print("Computer's turn (Player O)...")
            row, col = computer_move(board)
            print(f"Computer chose row {row}, column {col}")

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. That cell is already occupied. Try again.")
            continue

        if check_winner(board, current_player):
            display_board(board)
            if current_player == "X":
                print("Player X wins! Congratulations!")
            else:
                print("Computer wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
