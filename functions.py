# Functions for a Connect 4 game

def make_board(width=7, height=6):
    board = []

    for _ in range(height):
        row = [0] * width
        board.append(row)

    return board

def place_token(board, token, row, column):
    board[row][column] = token

   
def location_empty(board, row, column):
    return board[row][column] == 0


def column_available(board, column):
    return location_empty(board, 0, column)

   
def drop_token(board, column, token):
    row = len(board) - 1
    
    while not location_empty(board, row, column):
        row -= 1

    place_token(board, token, row, column)

    return row
        

def has_streak(section, token, length):
    streak = [token] * length

    for i in range(len(section)):
        chunk = section[i: i + length]

        if chunk == streak:
            return True

    return False


def get_row(board, row):
    return board[row]


def get_column(board, column):
    return[row[column] for row in board]


def get_left_diagonal(board, row, column):
    # adjust row and column to starting location
    distance_to_edge = min(row, column)
    row -= distance_to_edge
    column -= distance_to_edge

    diagonal = []

    while row < len(board) and column < len(board[0]):
        diagonal.append(board[row][column])
        row += 1
        column += 1

    return diagonal


def get_right_diagonal(board, row, column):
    # adjust row and column to starting location
    distance_to_edge = min(row, len(board[0]) - column - 1)
    row -= distance_to_edge
    column += distance_to_edge

    diagonal = []

    while row < len(board) and column >= 0:
        diagonal.append(board[row][column])
        row += 1
        column -= 1

    return diagonal


def check_win(board, row, column, length=4):
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
    num_columns = len(board[0])

    for column in range(num_columns):
        if column_available(board, column):
            return False

    return True
