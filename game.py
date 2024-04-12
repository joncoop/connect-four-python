from functions import *


def get_drop_column(board, player):
    while True:
        column = input(f"Where to drop, {player}? ")
        column = int(column) - 1

        if column_available(board, column):
            return column
        else:
            print("That column is full.")


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
        display_board(board)

        if check_win(board, row, column):
            print(f"{current_player} wins!")
            playing = False
        elif board_full(board):
            print("It's a tie.")
            playing = False
        else:
            turn = (turn + 1) % 2
    

def main():
    play()

if  __name__ == '__main__':
    main()