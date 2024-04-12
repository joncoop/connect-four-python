NUM_ROWS = 6
NUM_COLS = 7
EMPTY = 0
RED = 1
BLACK = 2


def make_board():
    board = []

    for _ in range(NUM_ROWS):
        row = [EMPTY] * NUM_COLS
        board.append(row)

    return board


def display_board(board):
    for row in board:
        for value in row:
            print(value, end=' ')
        print()
    print()


def place_piece(board, piece, row, column):
    board[row][column] = piece

   
def location_empty(board, row, column):
    return board[row][column] == EMPTY


def column_available(board, column):
    return location_empty(board, 0, column)

   
def drop_piece(board, column, piece):
    row = NUM_ROWS - 1
    
    while not location_empty(board, row, column):
        row -= 1

    place_piece(board, piece, row, column)

    return row
        

def check_for_streak(slice, piece):
    streak = [piece] * 4

    for i in range(len(slice) - 3):
        chunk = slice[i: i + 4]

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

    slice = []

    while row < NUM_ROWS and column < NUM_COLS:
        slice.append(board[row][column])
        row += 1
        column += 1

    return slice


def get_right_diagonal_slice(board, row, column):
    # adjust row and column to starting location
    while row > 0 and column < NUM_COLS - 1:
        row -= 1
        column += 1

    slice = []

    while row < NUM_ROWS and column >= 0:
        slice.append(board[row][column])
        row += 1
        column -= 1

    return slice


def check_win(board, row, column):
    horizontal = get_horizontal_slice(board, row)
    vertical = get_vertical_slice(board, column)
    left_diagonal = get_left_diagonal_slice(board, row, column)
    right_diagonal = get_right_diagonal_slice(board, row, column)

    horizontal_win = check_for_streak(board, horizontal)
    vertical_win = check_for_streak(board, vertical)
    left_diagonal_win = check_for_streak(board, left_diagonal)
    right_diagonal_win = check_for_streak(board, right_diagonal)

    return horizontal_win or vertical_win or left_diagonal_win or right_diagonal_win


def board_full(board):
    for row in board:
        for column in row:
            if row[column] == EMPTY:
                return False

    return True


def do_tests():
    board = make_board()
    print(board)
    display_board(board)

    place_piece(board, RED, 5, 1)
    display_board(board)

    print(location_empty(board, 0, 0))
    print(location_empty(board, 3, 1))

    place_piece(board, BLACK, 4, 1)
    place_piece(board, RED, 3, 1)
    place_piece(board, BLACK, 2, 1)
    display_board(board)

    place_piece(board, RED, 5, 2)
    place_piece(board, BLACK, 4, 2)
    place_piece(board, RED, 3, 2)
    place_piece(board, BLACK, 2, 2)
    place_piece(board, RED, 1, 2)
    place_piece(board, BLACK, 0, 2)
    display_board(board)

    print(column_available(board, 0))
    print(column_available(board, 1))
    print(column_available(board, 2))

    print(drop_piece(board, 0, RED))
    print(drop_piece(board, 1, BLACK))
    display_board(board)

    print(check_for_streak([RED, RED, RED, RED, EMPTY, EMPTY, EMPTY], RED))
    print(check_for_streak([EMPTY, RED, RED, RED, RED, EMPTY, EMPTY], RED))
    print(check_for_streak([EMPTY, EMPTY, RED, RED, RED, RED, EMPTY], RED))
    print(check_for_streak([EMPTY, EMPTY, EMPTY, RED, RED, RED, RED], RED))

    print(check_for_streak([EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], RED))
    print(check_for_streak([EMPTY, RED, BLACK, RED, RED, EMPTY, EMPTY], RED))

    print(get_horizontal_slice(board, 0))
    print(get_horizontal_slice(board, 1))
    print(get_horizontal_slice(board, 5))

    print(get_vertical_slice(board, 0))
    print(get_vertical_slice(board, 1))
    print(get_vertical_slice(board, 5))

    print(get_left_diagonal_slice(board, 0, 0))
    print(get_left_diagonal_slice(board, 0, 1))
    print(get_left_diagonal_slice(board, 0, 2))
    print(get_left_diagonal_slice(board, 0, 3))
    print(get_left_diagonal_slice(board, 0, 4))
    print(get_left_diagonal_slice(board, 0, 5))
    print(get_left_diagonal_slice(board, 0, 6))
    print(get_left_diagonal_slice(board, 1, 0))
    print(get_left_diagonal_slice(board, 3, 5))
    print(get_left_diagonal_slice(board, 5, 6))

    print(get_right_diagonal_slice(board, 5, 2))
    print(get_right_diagonal_slice(board, 1, 1))
    print(get_right_diagonal_slice(board, 0, 6))
    print(get_right_diagonal_slice(board, 2, 3))


if __name__ == '__main__':
    do_tests()
