# Functions for a Connect 4 game

#EMPTY = 0
EMPTY = None


def make_board(num_rows=6, num_columns=7):
    board = []

    for _ in range(num_rows):
        row = [EMPTY] * num_columns
        board.append(row)

    return board


def location_is_valid(board, row, column):
    return 0 <= row < len(board) and 0 <= column < len(board[0])


def location_empty(board, row, column):
    return board[row][column] == EMPTY


def place_disc(board, row, column, disc):
    if location_is_valid(board, row, column):
        board[row][column] = disc


def column_available(board, column):
    return location_empty(board, 0, column)

   
def drop_disc(board, column, disc):
    if not column_available(board, column):
        return -1
    
    row = len(board) - 1
    
    while not location_empty(board, row, column):
        row -= 1

    place_disc(board, row, column, disc)

    return row


def has_streak(sequence, value, length):
    streak = [value] * length

    for i in range(len(sequence)):
        chunk = sequence[i: i + length]
        if chunk == streak and EMPTY not in chunk:
            return True
            
    return False


def get_row(board, row):
    return board[row]


def get_column(board, column):
    return [row[column] for row in board]


def get_left_diagonal(board, row, column):
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


def check_win(board, row, column, streak_length=4):
    disc = board[row][column]

    if disc == EMPTY:
        return False

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
