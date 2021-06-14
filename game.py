import pygame


class Game:

    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.GAME_WINDOW_BACKGROUND_COLOR = (255, 255, 255)
        self.CLOCK_TICK = 60
        BACKGROUND_IMAGE = pygame.image.load('assets/background.png')
        self.BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND_IMAGE, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        TREASURE_IMAGE = pygame.image.load('assets/treasure.png')
        self.TREASURE_IMAGE_SCALED = pygame.transform.scale(TREASURE_IMAGE, (50, 50))
        self.game_window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def draw_objects(self):
        self.game_window.fill(self.GAME_WINDOW_BACKGROUND_COLOR)
        self.game_window.blit(self.BACKGROUND_IMAGE_SCALED, (0, 0))
        self.game_window.blit(self.TREASURE_IMAGE_SCALED, (375, 50))
        pygame.display.update()

    def run_game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            self.draw_objects()
            self.clock.tick(self.CLOCK_TICK)
