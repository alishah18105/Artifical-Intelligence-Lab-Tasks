# N-Queen Problem using Backtracking (Display with 'Q')

def print_board(board, n):
    """Prints the chessboard with 'Q' for queens and '.' for empty cells."""
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print("\n")

def is_safe(board, row, col, n):
    """Checks if a queen can be safely placed at board[row][col]."""
    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, n):
    """Recursive helper function to solve N-Queen problem."""
    # Base case: All queens placed
    
    if col >= n:
        print_board(board, n)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen

            if solve_nq_util(board, col + 1, n):
                return True  # ✅ Stop after first solution

            board[i][col] = 0  # Backtrack

    return False

def solve_nq(n):
    """Main function to solve the N-Queen problem."""
    board = [[0] * n for _ in range(n)]
    if not solve_nq_util(board, 0, n):
        print("No solution exists.")
    else:
        print("One valid solution is shown above.")

# Run for N = 8 (8-Queens Problem)
solve_nq(8)
