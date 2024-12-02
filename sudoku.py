def solve(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, row, col):
    # Check row
    if any(board[row][i] == num for i in range(len(board[0]))):
        return False

    # Check column
    if any(board[i][col] == num for i in range(len(board))):
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def sudoku_solver(board):
    # Validate the board
    for row in board:
        if len(row) != 9:
            raise ValueError("Each row must have exactly 9 elements.")
        for value in row:
            if not isinstance(value, int):
                raise ValueError("All values in the board must be integers.")
            if value < 0 or value > 9:
                raise ValueError("Values must be between 0 and 9.")
    
    if solve(board):
        return board
    return None  # Return None if the board cannot be solved
