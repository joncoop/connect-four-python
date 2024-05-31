# Standard library imports


# Third-party imports
import pygame


# Local imports


# Game configuration
class Config:

    # Screen settings
    CAPTION = 'Name of Game'
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60


# Main game class 
class Game:

    def __init__(self):
        pygame.mixer.pre_init()
        pygame.init()

        self.screen = pygame.display.set_mode([Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT])
        pygame.display.set_caption(Config.CAPTION)
        self.clock = pygame.time.Clock()

        self.running = True
        self.new_game()

    def new_game(self):
        pass

    def process_input(self):
        pressed = pygame.key.get_pressed()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass
    
    def render(self):
        pass

    def play(self):
        while self.running:            
            self.process_input()     
            self.update()     
            self.render()

            self.clock.tick(Config.FPS)

        pygame.display.update()
        pygame.quit()


# Entry point for the game
if __name__ == '__main__':
    game = Game()
    game.play()
