# Source Code for tic tac toe game
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_opponent_move(board, difficulty):
    if difficulty == "easy":
        # Easy: Random move
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        return random.choice(empty_cells)
    elif difficulty == "medium":
        # Medium: Random move if available, otherwise, make a winning move if possible
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        if empty_cells:
            return random.choice(empty_cells)
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        if check_winner(board, 'O'):
                            board[i][j] = ' '
                            return i, j
                        board[i][j] = ' '
            return random.choice(empty_cells)
    else:
        # Hard: Attempt to block the player or make a winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    if check_winner(board, 'O'):
                        return i, j
                    board[i][j] = ' '

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    if check_winner(board, 'X'):
                        board[i][j] = 'O'
                        return i, j
                    board[i][j] = ' '

        # If no winning move, play in a random available cell
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        return random.choice(empty_cells)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_name = input("Enter your name: ")
    opponent_name = input("Enter opponent name: ")
    difficulty = input("Choose difficulty (easy, medium, hard): ")

    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        else:
            print(f"{opponent_name}'s turn:")
            row, col = get_opponent_move(board, difficulty)

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                if current_player == 'X':
                    print(f"{player_name} wins!")
                else:
                    print(f"{opponent_name} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
