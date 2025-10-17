# Functions for a Connect 4 game

def make_board(num_rows=6, num_cols=7):
    """
    Creates a new game board of the specified dimensions with all slots empty.
    
    Args:
        num_rows (int): The number of rows on the board. Default is 6.
        num_cols (int): The number of columns on the board. Default is 7.
    
    Returns:
        list: A 2D list representing the board with empty slots (denoted by 0).
    """
    board = []

    for _ in range(num_rows):
        row = [0] * num_cols
        board.append(row)

    return board


def row_is_valid(board, row):
    """
    Checks if the given row index is within the valid range of the board's rows.
    
    Args:
        board (list): The game board.
        row (int): The row index to check.
    
    Returns:
        bool: True if the row is within the valid range, False otherwise.
    """
    # Unused, but potentially useful in other games 
    return 0 <= row < len(board)


def column_is_valid(board, column):
    """
    Checks if the given column index is within the valid range of the board's columns.
    
    Args:
        board (list): The game board.
        column (int): The column index to check.
    
    Returns:
        bool: True if the column is within the valid range, False otherwise.
    """
    return 0 <= column < len(board[0])


def location_is_valid(board, row, column):
    """
    Checks if the given row and column are within the valid bounds of the board.
    
    Args:
        board (list): The game board.
        row (int): The row index to check.
        column (int): The column index to check.
    
    Returns:
        bool: True if both row and column are valid, False otherwise.
    """
    return row_is_valid(board, row) and column_is_valid(board, column)


def place_token(board, token, row, column):
    """
    Places a token at the specified location on the board.
    
    Args:
        board (list): The game board.
        token (int): The token to place (1 for player 1, 2 for player 2).
        row (int): The row index where the token should be placed.
        column (int): The column index where the token should be placed.
    """
    board[row][column] = token


def location_empty(board, row, column):
    """
    Checks if the given location on the board is empty.
    
    Args:
        board (list): The game board.
        row (int): The row index to check.
        column (int): The column index to check.
    
    Returns:
        bool: True if the location is empty (denoted by 0), False otherwise.
    """
    return board[row][column] == 0


def column_available(board, column):
    """
    Checks if the given column has an available slot for a token to be placed.
    
    Args:
        board (list): The game board.
        column (int): The column index to check.
    
    Returns:
        bool: True if the column is available (top row is empty), False otherwise.
    """
    return location_empty(board, 0, column)


def drop_token(board, column, token):
    """
    Drops a token into the specified column, placing it in the lowest available row.
    
    Args:
        board (list): The game board.
        column (int): The column index where the token should be dropped.
        token (int): The token to place (1 for player 1, 2 for player 2).
    
    Returns:
        int: The row index where the token was placed, or -1 if the column is full.
    """
    if not column_available(board, column):
        return -1
    
    row = len(board) - 1
    
    while not location_empty(board, row, column):
        row -= 1

    place_token(board, token, row, column)

    return row


def get_row(board, row):
    """
    Retrieves the specified row from the board.
    
    Args:
        board (list): The game board.
        row (int): The row index to retrieve.
    
    Returns:
        list: The row of the board at the specified index.
    """
    return board[row]


def get_column(board, column):
    """
    Retrieves the specified column from the board.
    
    Args:
        board (list): The game board.
        column (int): The column index to retrieve.
    
    Returns:
        list: A list containing all values in the specified column.
    """
    return [row[column] for row in board]


def get_left_diagonal(board, row, column):
    """
    Retrieves the left diagonal (top-left to bottom-right) that contains the value at [row, column].
    
    Args:
        board (list): The game board.
        row (int): The starting row index.
        column (int): The starting column index.
    
    Returns:
        list: A list of tokens along the left diagonal.
    """
    distance_to_top = row
    distance_to_left_edge = column
    offset_to_top_left = min(distance_to_top, distance_to_left_edge)

    current_row = row - offset_to_top_left
    current_column = column - offset_to_top_left

    diagonal = []

    while current_row < len(board) and current_column < len(board[0]):
        diagonal.append(board[current_row][current_column])
        current_row += 1
        current_column += 1

    return diagonal


def get_right_diagonal(board, row, column):
    """
    Retrieves the right diagonal (top-right to bottom-left) that contains the value at [row, column].
    
    Args:
        board (list): The game board.
        row (int): The starting row index.
        column (int): The starting column index.
    
    Returns:
        list: A list of tokens along the right diagonal.
    """
    distance_to_top = row
    distance_to_right_edge = len(board[0]) - column - 1
    offset_to_top_right = min(distance_to_top, distance_to_right_edge)

    current_row = row - offset_to_top_right
    current_column = column + offset_to_top_right

    diagonal = []

    while current_row < len(board) and current_column >= 0:
        diagonal.append(board[current_row][current_column])
        current_row += 1
        current_column -= 1

    return diagonal


def has_streak(sequence, token, length):
    """
    Checks if there is a streak of the specified length in the given sequence.
    
    Args:
        section (list): A list representing a row, column, or diagonal.
        token (int): The token to check for (1 for player 1, 2 for player 2).
        length (int): The length of the streak to check for.
    
    Returns:
        bool: True if a streak of the specified length is found, False otherwise.
    """
    streak = 0

    for value in sequence:
        if value == token:
            streak += 1
        else:
            streak = 0

        if streak == length:
            return True

    return False


def check_win(board, row, column, length=4):
    """
    Checks if the player has won the game by getting a streak of the specified length.
    
    Args:
        board (list): The game board.
        row (int): The row where the last token was placed.
        column (int): The column where the last token was placed.
        length (int): The required length of the streak for a win. Default is 4.
    
    Returns:
        bool: True if there is a win, False otherwise.
    """
    token = board[row][column]
    
    horizontal = get_row(board, row)
    vertical = get_column(board, column)
    left_diagonal = get_left_diagonal(board, row, column)
    right_diagonal = get_right_diagonal(board, row, column)

    horizontal_win = has_streak(horizontal, token, length)
    vertical_win = has_streak(vertical, token, length)
    left_diagonal_win = has_streak(left_diagonal, token, length)
    right_diagonal_win = has_streak(right_diagonal, token, length)

    return horizontal_win or vertical_win or left_diagonal_win or right_diagonal_win


def board_full(board):
    """
    Checks if the board is full (no empty spaces left).
    
    Args:
        board (list): The game board.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    # Could just check the top row, but checking all locations might be useful for other games
    for row in board:
        for value in row:
            if value == 0:
                return False

    return True

