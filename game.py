from functions import *


def show_start_screen():
    print("******************************")
    print("*                            *")
    print("*        CONNECT FOUR        *")
    print("*                            *")
    print("*    Press ENTER to play.    *")
    print("*                            *")
    print("******************************")
    input()


def show_end_screen():
    print("Good bye. Thanks for playing.")


def play_again():
    while True:
        answer = input("Would you like to play again? (y/n)? ")
        answer = answer.lower().strip()
        
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
            
        
def get_drop_column(board, player):
    while True:
        column = input(f"Where to drop, {player}? ")
        column = column.strip()
        
        if column.isdigit():
            column = int(column) - 1

            if 0 <= column < NUM_COLS:
                return int(column)
        
        print("Invalid selection.")


def play():
    playing = True
    players = [RED, BLACK]
    turn = 0

    board = make_board()
    display_board(board)

    while playing:
        current_player = players[turn]
        column = get_drop_column(board, current_player)
        row = drop_piece(board, column, current_player)

        print()
        display_board(board)

        if check_win(board, row, column):
            print(f"\n{current_player} wins!")
            playing = False
        elif board_full(board):
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

    show_end_screen()


if  __name__ == '__main__':
    main()
