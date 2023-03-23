import pygame

# define some constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        # initialize Pygame
        pygame.init()

        # create the game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")

        # create the screens
        self.main_screen = MainScreen(self)
        self.game_screen = GameScreen(self)
        self.settings_screen = SettingsScreen(self)

        # set the current screen
        self.current_screen = self.main_screen

    def run(self):
        # game loop
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # quit the game
                    pygame.quit()
                    return

                # pass the event to the current screen
                self.current_screen.handle_event(event)

            # update the current screen
            self.current_screen.update()

            # draw the current screen
            self.current_screen.draw()

            # update the display
            pygame.display.update()

    def switch_screen(self, screen):
        self.current_screen = screen

class Screen:
    def __init__(self, game):
        self.game = game

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class MainScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                self.game.switch_screen(self.game.game_screen)
            elif event.key == pygame.K_s:
                self.game.switch_screen(self.game.settings_screen)

    def draw(self):
        self.game.screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render("Main Screen", True, WHITE)
        text_rect = text.get_rect(center=self.game.screen.get_rect().center)
        self.game.screen.blit(text, text_rect)

class GameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.game.switch_screen(self.game.main_screen)
            elif event.key == pygame.K_s:
                self.game.switch_screen(self.game.settings_screen)

    def draw(self):
        self.game.screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Game Screen", True, BLACK)
        text_rect = text.get_rect(center=self.game.screen.get_rect().center)
        self.game.screen.blit(text, text_rect)

class SettingsScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                self.game.switch_screen(self.game.game_screen)
            elif event.key == pygame.K_m:
                self.game.switch_screen(self.game.main_screen)

    def draw(self):
        self.game.screen.fill((255, 255, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Settings Screen", True, BLACK)
        text_rect = text.get_rect(center=self.game.screen.get_rect().center)
        self.game.screen.blit(text, text_rect)

if __name__ == "__main__":
    game = Game()
    game.run()