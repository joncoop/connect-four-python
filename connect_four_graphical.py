# Standard library imports


# Third-party imports
import pygame


# Local imports
import functions


# Game configuration
class Config:

    # Screen settings
    CAPTION = 'Connect 4'
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700
    FPS = 60

    # Board size (Not flexible yet)
    NUM_ROWS = 6
    NUM_COLUMNS = 7

    # How many in a row (Not used yet)
    STREAK_LENGTH = 4

    # Disc names
    DISCS = ['Red', 'Yellow']

    # Board colors
    BG_COLOR = pygame.Color('black')
    DISC1_COLOR = pygame.Color('red')
    DISC2_COLOR = pygame.Color('yellow')
    BOARD_COLOR = pygame.Color('blue')
    EMPTY_COLOR = pygame.Color('white')
    TEXT_COLOR = pygame.Color('white')

    # Fonts
    FONT_FAMILY_SMALL, FONT_SIZE_SMALL = None, 40
    FONT_FAMILY_MEDIUM, FONT_SIZE_MEDIUM = None, 120
    FONT_FAMILY_LARGE, FONT_SIZE_LARGE = None, 200

    # Scenes
    START = 0
    PLAYING = 1
    END = 2


# Main game class 
class Game:

    def __init__(self, rows=Config.NUM_ROWS, columns=Config.NUM_COLUMNS, streak=Config.STREAK_LENGTH):
        pygame.mixer.pre_init()
        pygame.init()

        self.screen = pygame.display.set_mode([Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT])
        pygame.display.set_caption(Config.CAPTION)
        self.clock = pygame.time.Clock()

        self.rows = rows
        self.columns = columns
        self.streak = streak

        self.running = True
        self.scene = Config.START
        self.message = ''

        self.load_assets()
        self.new_game()

    def load_assets(self):
        self.FONT_SM = pygame.font.Font(Config.FONT_FAMILY_SMALL, Config.FONT_SIZE_SMALL)
        self.FONT_MD = pygame.font.Font(Config.FONT_FAMILY_MEDIUM, Config.FONT_SIZE_MEDIUM)
        self.FONT_LG = pygame.font.Font(Config.FONT_FAMILY_LARGE, Config.FONT_SIZE_LARGE)
    
    def new_game(self):
        self.board = functions.make_board(self.rows, self.columns)
        self.turn = 0
        name = Config.DISCS[self.turn]
        self.message = f"Which column, {name}?"

    def show_start_screen(self):
        title_text = self.FONT_MD.render('Connect', True, pygame.Color('white'))
        title_rect = title_text.get_rect()
        title_rect.midbottom = Config.SCREEN_WIDTH // 2 - 32, Config.SCREEN_HEIGHT // 2 - 8

        number_text = self.FONT_LG.render('4', True, pygame.Color('red'))
        number_rect = number_text.get_rect()
        number_rect.midleft = title_rect.midright

        instructions_text = self.FONT_SM.render('Click to play', True, pygame.Color('white'))
        instructions_rect = instructions_text.get_rect()
        instructions_rect.midtop = Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2 + 8
        
        self.screen.fill(pygame.Color('cyan3'))
        self.screen.blit(title_text, title_rect)
        self.screen.blit(number_text, number_rect)
        self.screen.blit(instructions_text, instructions_rect)

    def display_board(self):
        pygame.draw.rect(self.screen, Config.BOARD_COLOR, [0, 0, Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT - 100])

        for y, row in enumerate(self.board):
            for x, value in enumerate(row):
                center = [100 * x + 50, 100 * y + 50]
                radius = 40

                if value == Config.DISCS[0]:
                    color = Config.DISC1_COLOR
                elif value == Config.DISCS[1]:
                    color = Config.DISC2_COLOR
                else:
                    color = Config.EMPTY_COLOR

                pygame.draw.circle(self.screen, color, center, radius)
       
    def display_status(self):
        message_text = self.FONT_SM.render(self.message, True, Config.TEXT_COLOR)
        message_rect = message_text.get_rect()
        message_rect.center = Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT - 50

        self.screen.blit(message_text, message_rect)

    def handle_start_scene(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.scene = Config.PLAYING

    def get_drop_column(self, event):
        x, y = pygame.mouse.get_pos()

        if y < Config.SCREEN_HEIGHT - 100: # out of status area
            column = x // 100 # 100 is column width
        
            if functions.column_available(self.board, column):
                return column
                    
        return -1
    
    def handle_playing_scene(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            column = self.get_drop_column(event)

            if column != -1:
                current_disc = Config.DISCS[self.turn]
                row = functions.drop_disc(self.board, column, current_disc)

                if functions.win_at_location(self.board, row, column, self.streak):
                    self.message = f"{current_disc} wins! Play again? (y/n)"
                    self.scene = Config.END
                elif functions.board_is_full(self.board):
                    self.message = "It's a tie. Play again? (y/n)"
                    self.scene = Config.END
                else:
                    self.turn = (self.turn + 1) % 2
                    name = Config.DISCS[self.turn]
                    self.message = f"Which column, {name}?"
    
    def handle_end_scene(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                self.new_game()
                self.scene = Config.PLAYING
            if event.key == pygame.K_n:
                self.running = False

    def process_input(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif self.scene == Config.START:
                self.handle_start_scene(event)
            elif self.scene == Config.PLAYING:
                self.handle_playing_scene(event)
            elif self.scene == Config.END:
                self.handle_end_scene(event)

    def update(self):
        pass     

    def render(self):
        self.screen.fill(Config.BG_COLOR)

        if self.scene == Config.START:
            self.show_start_screen()
        else:
            self.display_board()
            self.display_status()

    def play(self):
        while self.running:            
            self.process_input()     
            self.update()     
            self.render()

            pygame.display.update()
            self.clock.tick(Config.FPS)

        pygame.quit()


# Entry point for the game
if __name__ == '__main__':
    game = Game()
    game.play()
