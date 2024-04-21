import functions


def print_2d_array(array):
    for row in array:
        print(row)


def do_tests():
    print('Make board')
    board = functions.make_board()
    print_2d_array(board)
    print()

    print('Place_piece')
    functions.place_piece(board, 2, 5, 1)
    print_2d_array(board)
    print()

    functions.place_piece(board, 1, 4, 1)
    functions.place_piece(board, 2, 3, 1)
    functions.place_piece(board, 1, 2, 1)
    functions.place_piece(board, 2, 5, 2)
    functions.place_piece(board, 1, 4, 2)
    functions.place_piece(board, 2, 3, 2)
    functions.place_piece(board, 1, 2, 2)
    functions.place_piece(board, 2, 1, 2)
    functions.place_piece(board, 1, 0, 2)
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

    print('Drop piece')    
    print(functions.drop_piece(board, 0, 2))
    print(functions.drop_piece(board, 1, 1))
    print_2d_array(board)
    print()

    print('Check for streak')
    print(functions.has_streak([1, 1, 1, 1, 0, 0, 0], 1, 4))
    print(functions.has_streak([0, 1, 1, 1, 1, 0, 0], 1, 4))
    print(functions.has_streak([0, 0, 1, 1, 1, 0], 1, 4))
    print(functions.has_streak([0, 0, 0, 1, 1, 1, 1], 1, 4))
    print(functions.has_streak([0, 0, 0, 0, 0, 0, 0], 1, 4))
    print(functions.has_streak([0, 1, 0, 2, 1, 0, 1], 1, 4))
    print()

    print('Get horizontal slice')
    print(functions.get_horizontal_slice(board, 0))
    print(functions.get_horizontal_slice(board, 1))
    print(functions.get_horizontal_slice(board, 5))
    print()
    
    print('Get vertical slice')
    print(functions.get_vertical_slice(board, 0))
    print(functions.get_vertical_slice(board, 1))
    print(functions.get_vertical_slice(board, 5))
    print()

    print('Get left diagonal slice')
    print(functions.get_left_diagonal_slice(board, 0, 0))
    print(functions.get_left_diagonal_slice(board, 0, 1))
    print(functions.get_left_diagonal_slice(board, 0, 2))
    print(functions.get_left_diagonal_slice(board, 0, 3))
    print(functions.get_left_diagonal_slice(board, 0, 4))
    print(functions.get_left_diagonal_slice(board, 0, 5))
    print(functions.get_left_diagonal_slice(board, 0, 6))
    print(functions.get_left_diagonal_slice(board, 1, 0))
    print(functions.get_left_diagonal_slice(board, 3, 5))
    print(functions.get_left_diagonal_slice(board, 5, 6))
    print()

    print('Get right diagonal slice')
    print(functions.get_right_diagonal_slice(board, 5, 2))
    print(functions.get_right_diagonal_slice(board, 1, 1))
    print(functions.get_right_diagonal_slice(board, 0, 6))
    print(functions.get_right_diagonal_slice(board, 2, 3))


if __name__ == '__main__':
    do_tests()
