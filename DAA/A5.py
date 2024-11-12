# Python3 program to solve N Queen Problem using backtracking

N = 4  # Global variable for board size

def print_solution(board):
    """Print the board solution."""
    for row in board:
        print(' '.join(map(str, row)))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    
    # Check this row on the left side
    if 1 in board[row][:col]:
        return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nq_util(board, col):
    """Recursive utility function to solve N Queen problem."""
    
    # Base case: If all queens are placed, return True
    if col >= N:
        return True
    
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Recur to place rest of the queens
            if solve_nq_util(board, col + 1):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0
    
    # If the queen can't be placed in any row in this column col, return False
    return False

def solve_nq():
    """
    Solve the N Queen problem using Backtracking.
    This function solves the N Queen problem using Backtracking.
    It returns False if queens cannot be placed, otherwise returns True
    and prints the placement of queens in the form of 1s.
    Note that there may be more than one solution, this function prints one of the feasible solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False
    
    print_solution(board)
    return True


if __name__ == "__main__":
    print("Placed Queens where N =",N)
    solve_nq()