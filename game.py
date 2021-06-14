import pygame
from gameObject import GameObject
from player import Player


class Game:

    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.GAME_WINDOW_BACKGROUND_COLOR = (255, 255, 255)
        self.CLOCK_TICK = 60
        self.background = GameObject(0, 0, 800, 800, 'assets/background.png')
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')
        self.game_window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)
        self.clock = pygame.time.Clock()

    def draw_objects(self):
        self.game_window.fill(self.GAME_WINDOW_BACKGROUND_COLOR)
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        pygame.display.update()

    def run_game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            self.draw_objects()
            self.clock.tick(self.CLOCK_TICK)
