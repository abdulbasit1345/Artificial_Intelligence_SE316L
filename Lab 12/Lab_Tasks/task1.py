import math


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False


def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return 10 if row[0] == "X" else -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return 10 if board[0][col] == "X" else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == "X" else -10

    # If no winner
    return 0


def minimax(board, depth, is_max):
    score = evaluate(board)

    # If the maximizer or minimizer has won the game
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth

    # If no moves are left and no winner, it's a tie
    if not is_moves_left(board):
        return 0

    # Maximizer's move
    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"  # Maximizer's move
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"  # Undo the move
        return best

    # Minimizer's move
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"  # Minimizer's move
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"  # Undo the move
        return best


def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"  # Maximizer's move
                move_val = minimax(board, 0, False)
                board[i][j] = "_"  # Undo the move

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move


# Initialize the board
board = [
    ["X", "O", "X"],
    ["O", "O", "X"],
    ["_", "_", "_"]
]

print("Initial Board:")
print_board(board)

# Find the best move for 'X'
best_move = find_best_move(board)
print(f"\nThe Optimal Move is at Row: {best_move[0]} Column: {best_move[1]}")

# Apply the move
board[best_move[0]][best_move[1]] = "X"
print("\nBoard after Optimal Move:")
print_board(board)
