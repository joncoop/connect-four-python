import functions


# Board size (Up to 99x99)
NUM_ROWS = 6
NUM_COLS = 7

# Win condition
STREAK_LENGTH = 4

# Token symbols
TOKENS = {
    0: "-",  # Empty
    1: "X",  # Player 1
    2: "O"   # Player 2
}


def show_start_screen():
    """
    Displays the start screen and prompts the user to press Enter to begin the game.
    """
    print("******************************")
    print("*                            *")
    print(f"*         CONNECT {STREAK_LENGTH}          *")
    print("*                            *")
    print("*    Press ENTER to play.    *")
    print("*                            *")
    print("******************************")
    input()


def show_end_screen():
    """
    Displays an end screen.
    """
    print("Thanks for playing!")


def play_again():
    """
    Asks the player if they would like to play another game.
    
    Returns:
        bool: True if the player chooses to play again, False otherwise.
    """
    while True:
        answer = input("Would you like to play again? (y/n) ")
        answer = answer.lower().strip()
        
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False


def display_board(board):
    """
    Displays the current state of the game board.
    
    Args:
        board (list): The game board represented as a 2D list.
    """
    column_gap = " "
    num_cols = len(board[0])

    for row in board:
        print(column_gap.join(TOKENS[value] for value in row))

    board_width = num_cols + (num_cols - 1) * len(column_gap)
    print('—' * board_width)

    # Write 1st digit of column number below each column
    for i in range(1, num_cols + 1):
        first_digit = i if i < 10 else i // 10
        print(first_digit, end=column_gap)
    print()

    # Write 2nd digit of column number on next line (only if 2-digit column numbers exist)
    if num_cols > 9:
        for i in range(1, num_cols + 1):
            second_digit = " " if i < 10 else i % 10
            print(second_digit, end=column_gap)
        print()


def get_drop_column(board, player):
    """
    Prompts the player to select a column to drop their token.
    
    Args:
        board (list): The game board represented as a 2D list.
        player (int): The player number (1 or 2).
    
    Returns:
        int: The column selected by the player.
    """
    while True:
        column = input(f"{TOKENS[player]}, choose a column? ").strip()
        
        if not column.isdigit():
            print("Enter a numeric value.")
            continue
        
        column = int(column) - 1  # Board uses zero-based index

        if not functions.column_is_valid(board, column):
            print("Invalid column number.")
            continue
        
        if not functions.column_available(board, column):
            print("Column not available.")
            continue

        return column


def get_result(board, row, column, current_player):
    """
    Determines if the game has been won or ended in a tie.

    Args:
        board (list): The game board represented as a 2D list.
        row (int): The row index of the last token placed.
        column (int): The column index of the last token placed.
        current_player (int): The player who made the last move.

    Returns:
        str | None: A message describing the game result, or None if play should continue.
    """
    result = None

    if functions.check_win(board, row, column, ):
        result = f"{TOKENS[current_player]} wins!"
    elif functions.board_full(board):
        result = "It's a tie."

    return result


def play():
    """
    Manages the gameplay loop for Connect 4. Alternates players, accepts moves, 
    checks for wins, and displays the game board. Ends when a player wins 
    or the board is full (tie).
    """
    result = None
    current_player = 1

    board = functions.make_board(NUM_ROWS, NUM_COLS)
    display_board(board)

    while result is None:
        column = get_drop_column(board, current_player)
        row = functions.drop_token(board, column, current_player)

        print()
        display_board(board)
        result = get_result(board, row, column, current_player)
        
        if result is None:
            current_player = 1 if current_player == 2 else 2
    
    print(f"\n{result}\n")


def main():
    """
    Manages the game loop, calling the necessary functions to start and play the game,
    and asking the player if they want to play again after the game ends.
    """
    show_start_screen()

    running = True

    while running:
        play()
        running = play_again()

        if running:
            print("\nNew game...")
        print()

    show_end_screen()


if __name__ == "__main__":
    main()
