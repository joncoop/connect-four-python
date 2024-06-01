import functions


# Board size (Up to 99x99)
NUM_ROWS = 6
NUM_COLUMNS = 7

# How many in a row
STREAK_LENGTH = 4

# Disc symbols
DISCS = 'X', 'O'
BLANK = '-'


def show_start_screen():
    print('******************************')
    print('*                            *')
    print('*         CONNECT 4          *')
    print('*                            *')
    print('*    Press ENTER to play.    *')
    print('*                            *')
    print('******************************')
    input()


def show_end_screen():
    print('Thanks for playing!')


def play_again():
    while True:
        answer = input('Would you like to play again? (y/n)? ')
        answer = answer.lower().strip()
        
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False


def display_board(board):
    for row in board:
        for value in row:
            if value in DISCS:
                print(value, end=' ')
            else:
                print(BLANK, end=' ')

        print()

    print('—' * (2 * len(board[0]) - 1))

    display_column_numbers(board)


def display_column_numbers(board):
    width = len(board[0])

    for i in range(1, width + 1):
        if i < 10:
            print(f'{i}', end=' ')
        else:
            print(f'{i // 10}', end=' ')
    print()

    if width > 9:
        for i in range(1, width + 1):
            if i < 10:
                print(f' ', end=' ')
            else:
                print(f'{i % 10}', end=' ')
        print()


def get_drop_column(board, player):
    while True:
        column = input(f'Where to drop, {player}? ')
        column = column.strip()
        
        if column.isdigit():
            column = int(column) - 1

            if functions.column_available(board, column):
                return column
        
        print('Invalid selection.')


def play():
    playing = True
    turn = 0

    board = functions.make_board(NUM_ROWS, NUM_COLUMNS)
    display_board(board)

    while playing:
        current_disc = DISCS[turn]
        column = get_drop_column(board, current_disc)
        row = functions.drop_disc(board, column, current_disc)

        print()
        display_board(board)

        if functions.win_at_location(board, row, column, STREAK_LENGTH):
            result = f'{current_disc} wins!'
            playing = False
        elif functions.board_is_full(board):
            result = "It's a tie."
            playing = False
        else:
            turn = (turn + 1) % 2
    
    print(f'\n{result}')


def main():
    show_start_screen()

    running = True

    while running:
        play()
        print()
        running = play_again()
        print()

    show_end_screen()


if  __name__ == '__main__':
    main()
