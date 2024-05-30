# Imports
import pygame
import functions

# Screen settings
CAPTION = 'Connect 4'
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FPS = 60

# Initialize pygame and make window
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# Board size (Not flexible yet)
WIDTH = 7
HEIGHT = 6

# How many in a row (Not used yet)
STREAK_LENGTH = 4

# Player info
PLAYER_NAMES = ['Red', 'Yellow']
P1_COLOR = pygame.Color('red')
P2_COLOR = pygame.Color('yellow')

# Colors
BOARD_COLOR = pygame.Color('blue')
EMPTY_COLOR = pygame.Color('white')

# Fonts
FONT_LG = pygame.font.Font(None, 208)
FONT_MD = pygame.font.Font(None, 128)
FONT_SM = pygame.font.Font(None, 42)

# Scenes
START = 0
PLAYING = 1
END = 2


def show_start_screen():
    title_text = FONT_MD.render('Connect', True, pygame.Color('white'))
    title_rect = title_text.get_rect()
    title_rect.midbottom = SCREEN_WIDTH // 2 - 32, SCREEN_HEIGHT // 2 - 8

    number_text = FONT_LG.render('4', True, pygame.Color('red'))
    number_rect = number_text.get_rect()
    number_rect.midleft = title_rect.midright

    message_text = FONT_SM.render('Click to play', True, pygame.Color('white'))
    message_rect = message_text.get_rect()
    message_rect.midtop = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 8
    
    screen.fill(pygame.Color('cyan3'))
    screen.blit(title_text, title_rect)
    screen.blit(number_text, number_rect)
    screen.blit(message_text, message_rect)


def display_board(board):
    pygame.draw.rect(screen, BOARD_COLOR, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - 100])

    for y, row in enumerate(board):
        for x, value in enumerate(row):
            center = [100 * x + 50, 100 * y + 50]
            radius = 40

            if value == 0:
                color = P1_COLOR
            elif value == 1:
                color = P2_COLOR
            else:
                color = EMPTY_COLOR

            pygame.draw.circle(screen, color, center, radius)


def display_status(message):
    message_text = FONT_SM.render(message, True, pygame.Color('white'))
    message_rect = message_text.get_rect()
    message_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50

    screen.blit(message_text, message_rect)


def get_drop_column(board, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if y < SCREEN_HEIGHT - 100: # out of status area
            column = x // 100

        if 0 <= column < len(board[0]) and functions.column_available(board, column):
            return column
        
    return None
    
            
def new_game():
    board = functions.make_board(WIDTH, HEIGHT)
    turn = 0

    return board, turn


def play_again(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
            return True
        elif event.key == pygame.K_n:
            return False
    
    return None

 
def run():
    scene = START
    running = True
    message = ''
    board, turn = new_game()

    while running:
        # Input
        column = None
        again = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if scene == START and event.type == pygame.MOUSEBUTTONDOWN:
                scene = PLAYING
            elif scene == PLAYING:
                column = get_drop_column(board, event)
            elif scene == END:
                again = play_again(event)
                break # otherwise again gets flipped back to None as other events are processed
                
        #Logic
        if scene == PLAYING:
            name = PLAYER_NAMES[turn]
            message = f"Which column, {name}?"

            if column is not None:
                row = functions.drop_disc(board, column, turn)

                if functions.check_win(board, row, column):
                    message = f"{name} wins! Play again? (y/n)"
                    scene = END
                elif functions.board_full(board):
                    message = "It's a tie. Play again? (y/n)"
                    scene = END
                else:
                    turn = (turn + 1) % 2

        elif scene == END:
            if again == True:
                board, turn = new_game()
                scene = PLAYING
            elif again == False: # Can't use 'else' or say 'not again' because None is falsy
                running = False


        # Drawing
        screen.fill(pygame.Color('black'))

        if scene == START:
            show_start_screen()
        else:
            display_board(board)
            display_status(message)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    run()
