# Practical No. 3
# Taking number of queens as input from user
print("Enter the number of queens")
N = int(input())

# Create a chessboard: NxN matrix with all elements set to 0
board = [[0] * N for _ in range(N)]

# Function to check if a queen can attack another
def attack(i, j):
    # Checking vertically and horizontally
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Checking diagonally
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True

    return False

# Function to solve the N-Queens problem
def N_queens(n):
    if n == 0:
        return True  # All queens have been placed successfully

    for i in range(0, N):
        for j in range(0, N):
            if not attack(i, j) and board[i][j] != 1:
                board[i][j] = 1  # Place the queen

                if N_queens(n - 1):  # Recursive call to place the next queen
                    return True

                board[i][j] = 0  # Backtrack and remove the queen

    return False  # Trigger backtracking

# Solve the N-Queens problem and print the board
if N_queens(N):
    for row in board:
        print(row)
else:
    print("No solution exists for", N, "queens.")
