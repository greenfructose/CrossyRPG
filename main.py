import pygame
from game import Game
pygame.init()
pygame.mixer.init()

game = Game()
game.run_game_loop()

pygame.quit()
quit()
