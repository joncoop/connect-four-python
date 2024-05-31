# Functions for a Connect 4 game

#EMPTY = 0
EMPTY = None


def make_board(num_columns=7, num_rows=6):
    board = []

    for _ in range(num_rows):
        row = [EMPTY] * num_columns
        board.append(row)

    return board


def place_disc(board, row, column, disc):
    board[row][column] = disc

   
def location_empty(board, row, column):
    return board[row][column] == EMPTY


def column_available(board, column):
    return location_empty(board, 0, column)

   
def drop_disc(board, column, disc):
    row = len(board) - 1
    
    while not location_empty(board, row, column):
        row -= 1

    if row >= 0:
        place_disc(board, row, column, disc)

    return row
        

def has_streak(sequence, value, length):
    streak = [value] * length

    for i in range(len(sequence)):
        chunk = sequence[i: i + length]
        if chunk == streak:
            return True
            
    return False


def get_row(board, row):
    return board[row]


def get_column(board, column):
    return [row[column] for row in board]


def get_left_diagonal(board, row, column):
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
    distance_to_edge = min(row, len(board[0]) - column - 1)
    row -= distance_to_edge
    column += distance_to_edge

    diagonal = []

    while row < len(board) and column >= 0:
        diagonal.append(board[row][column])
        row += 1
        column -= 1

    return diagonal


def check_win(board, row, column, streak_length=4):
    disc = board[row][column]
    
    horizontal = get_row(board, row)
    vertical = get_column(board, column)
    left_diagonal = get_left_diagonal(board, row, column)
    right_diagonal = get_right_diagonal(board, row, column)

    horizontal_win = has_streak(horizontal, disc, streak_length)
    vertical_win = has_streak(vertical, disc, streak_length)
    left_diagonal_win = has_streak(left_diagonal, disc, streak_length)
    right_diagonal_win = has_streak(right_diagonal, disc, streak_length)

    return horizontal_win or vertical_win or left_diagonal_win or right_diagonal_win


def board_full(board):
    num_columns = len(board[0])

    for column in range(num_columns):
        if column_available(board, column):
            return False

    return True
