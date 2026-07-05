def print_board(board):
    # Prints the matrix beautifully row by row
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen
            board[i][col] = 'Q'

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col] (Backtrack)
            board[i][col] = '.'

    return False

def solve_n_queens():
    print("--- N-Queens Solver ---")
    try:
        n = int(input("Enter the size of the board (N x N, e.g., 4 or 8): "))
    except ValueError:
        print("Please enter a valid number.")
        return
        
    if n < 4 and n != 1:
        print("Solutions do not exist for board sizes less than 4 (except 1)!")
        return

    # Create an N x N board filled with '.' spaces
    board = [['.' for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return

    print(f"\nFound a safe layout for {n} Queens:")
    print_board(board)

# Run the solver
solve_n_queens()
