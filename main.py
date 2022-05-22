import pygame
import sys
from card import Card


class Interface:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        bg_color = (0, 0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys, exit()

        screen.fill(bg_color)
        pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.card.draw(self.screen)
        pygame.display.update()


intersace = Interface()
