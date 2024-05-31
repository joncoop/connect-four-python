import functions


def print_2d_array(array):
    for row in array:
        print(row)


def do_tests():
    print('Make board')
    board = functions.make_board()
    print_2d_array(board)
    print()

    print('Place disc')
    functions.place_disc(board, 5, 2, 1)
    print_2d_array(board)
    print()

    functions.place_disc(board, 5, 1, 1)
    functions.place_disc(board, 5, 3, 1)
    functions.place_disc(board, 5, 4, 1)
    functions.place_disc(board, 5, 6, 2)
    functions.place_disc(board, 4, 6, 2)
    functions.place_disc(board, 3, 6, 2)
    functions.place_disc(board, 2, 6, 2)
    functions.place_disc(board, 5, 0, 2)
    functions.place_disc(board, 4, 1, 2)
    functions.place_disc(board, 4, 2, 1)
    functions.place_disc(board, 3, 2, 2)
    functions.place_disc(board, 4, 3, 1)
    functions.place_disc(board, 3, 3, 1)
    functions.place_disc(board, 2, 3, 2)
    functions.place_disc(board, 4, 4, 1)
    functions.place_disc(board, 2, 2, 1)
    functions.place_disc(board, 3, 1, 1)
    functions.place_disc(board, 2, 1, 2)
    functions.place_disc(board, 1, 1, 1)
    functions.place_disc(board, 0, 1, 2)

    print_2d_array(board)
    print()
    
    print('Location empty')
    print(functions.location_empty(board, 0, 0))
    print(functions.location_empty(board, 3, 1))
    print()
    
    print('Column available')    
    print(functions.column_available(board, 0))
    print(functions.column_available(board, 1))
    print(functions.column_available(board, 2))
    print()
    

    print('Drop disc')    
    print(functions.drop_disc(board, 0, 2))
    print(functions.drop_disc(board, 5, 2))
    print(functions.drop_disc(board, 1, 1))
    print_2d_array(board)
    print()
    
    print('Check for streak')
    print(functions.has_streak([1, 1, 1, 1, 0, 0, 0], 1, 4))
    print(functions.has_streak([0, 1, 1, 1, 1, 0, 0], 1, 4))
    print(functions.has_streak([0, 0, 1, 1, 1, 1, 0], 1, 4))
    print(functions.has_streak([0, 0, 0, 1, 1, 1, 1], 1, 4))
    print(functions.has_streak([0, 0, 0, 0, 0, 0, 0], 1, 4))
    print(functions.has_streak([0, 1, 0, 2, 1, 0, 1], 1, 4))
    print()
    
    print('Get row')
    print(functions.get_row(board, 0))
    print(functions.get_row(board, 1))
    print(functions.get_row(board, 5))
    print()
    
    print('Get column')
    print(functions.get_column(board, 0))
    print(functions.get_column(board, 1))
    print(functions.get_column(board, 5))
    print()
    
    print('Get left diagonal')
    print(functions.get_left_diagonal(board, 0, 0))
    print(functions.get_left_diagonal(board, 0, 1))
    print(functions.get_left_diagonal(board, 0, 2))
    print(functions.get_left_diagonal(board, 0, 3))
    print(functions.get_left_diagonal(board, 0, 4))
    print(functions.get_left_diagonal(board, 0, 5))
    print(functions.get_left_diagonal(board, 0, 6))
    print(functions.get_left_diagonal(board, 1, 0))
    print(functions.get_left_diagonal(board, 3, 5))
    print(functions.get_left_diagonal(board, 5, 6))
    print()

    print('Get right diagonal')
    print(functions.get_right_diagonal(board, 5, 2))
    print(functions.get_right_diagonal(board, 1, 1))
    print(functions.get_right_diagonal(board, 0, 6))
    print(functions.get_right_diagonal(board, 2, 3))
    print()

    print('Check win')
    print(functions.check_win(board, 5, 2))
    print(functions.check_win(board, 4, 6))
    print(functions.check_win(board, 3, 3))
    print(functions.check_win(board, 3, 2))
    print(functions.check_win(board, 3, 1))
    print(functions.check_win(board, 4, 5)) # weird, but easy to fix
    print()
    
    print('Check board full')
    full = [[1, 1, 2], [1, 1, 2], [2, 1, 2]]
    not_full = [[1, functions.EMPTY, functions.EMPTY], [1, 1, 2], [2, 1, 2]]
    print(functions.board_full(full))
    print(functions.board_full(not_full))


if __name__ == '__main__':
    do_tests()
