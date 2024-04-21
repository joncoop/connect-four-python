import functions


# Board size (Up to 99x99)
WIDTH = 7
HEIGHT = 6

# How many in a row
STREAK_LENGTH = 4

# Markers
EMPTY = '-'
P1_MARKER = 'X'
P2_MARKER = 'O'


def show_start_screen():
    print("******************************")
    print("*                            *")
    print(f"*         CONNECT 4         *")
    print("*                            *")
    print("*    Press ENTER to play.    *")
    print("*                            *")
    print("******************************")
    input()


def play_again():
    while True:
        answer = input("Would you like to play again? (y/n)? ")
        answer = answer.lower().strip()
        
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False


def display_board(board):
    for i in range(1, WIDTH + 1):
        print(i, end=' ')
    print()

    for row in board:
        for value in row:
            if value == 1:
                marker = P1_MARKER
            elif value == 2:
                marker = P2_MARKER
            else:
                marker = EMPTY

            print(marker, end=' ')
        print()


def get_drop_column(board, player):
    while True:
        column = input(f"Where to drop, {player}? ")
        column = column.strip()
        
        if column.isdigit():
            column = int(column) - 1

            if 0 <= column < len(board[0]) and functions.column_available(board, column):
                return column
        
        print("Invalid selection.")


def play():
    playing = True
    turn = 0

    board = functions.make_board(WIDTH, HEIGHT)
    display_board(board)

    while playing:
        current_player = turn + 1
        column = get_drop_column(board, current_player)
        row = functions.drop_piece(board, column, current_player)

        print()
        display_board(board)

        if functions.check_win(board, row, column, STREAK_LENGTH):
            print(f"\nPlayer {current_player} wins!")
            playing = False
        elif functions.board_full(board):
            print("\nIt's a tie.")
            playing = False
        else:
            turn = (turn + 1) % 2
    

def main():
    show_start_screen()

    running = True

    while running:
        play()
        print()
        running = play_again()
        print()


if  __name__ == '__main__':
    main()
