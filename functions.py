# Functions for a Connect 4 game

def make_board(width=7, height=6):
    board = []

    for _ in range(height):
        row = [0] * width
        board.append(row)

    return board

def place_piece(board, piece, row, column):
    board[row][column] = piece

   
def location_empty(board, row, column):
    return board[row][column] == 0


def column_available(board, column):
    return location_empty(board, 0, column)

   
def drop_piece(board, column, piece):
    row = len(board) - 1
    
    while not location_empty(board, row, column):
        row -= 1

    place_piece(board, piece, row, column)

    return row
        

def has_streak(section, piece, length):
    streak = [piece] * length

    for i in range(len(section)):
        chunk = section[i: i + length]

        if chunk == streak:
            return True

    return False


def get_horizontal_slice(board, row):
    return board[row]


def get_vertical_slice(board, column):
    return[row[column] for row in board]


def get_left_diagonal_slice(board, row, column):
    # adjust row and column to starting location
    while row > 0 and column > 0:
        row -= 1
        column -= 1

    section = []

    while row < len(board) and column < len(board[0]):
        section.append(board[row][column])
        row += 1
        column += 1

    return section


def get_right_diagonal_slice(board, row, column):
    # adjust row and column to starting location
    while row > 0 and column < len(board[0]) - 1:
        row -= 1
        column += 1

    section = []

    while row < len(board) and column >= 0:
        section.append(board[row][column])
        row += 1
        column -= 1

    return section


def check_win(board, row, column, length=4):
    piece = board[row][column]
    
    horizontal = get_horizontal_slice(board, row)
    vertical = get_vertical_slice(board, column)
    left_diagonal = get_left_diagonal_slice(board, row, column)
    right_diagonal = get_right_diagonal_slice(board, row, column)

    horizontal_win = has_streak(horizontal, piece, length)
    vertical_win = has_streak(vertical, piece, length)
    left_diagonal_win = has_streak(left_diagonal, piece, length)
    right_diagonal_win = has_streak(right_diagonal, piece, length)

    return horizontal_win or vertical_win or left_diagonal_win or right_diagonal_win


def board_full(board):
    for row in board:
        for column in row:
            if column == 0:
                return False

    return True
