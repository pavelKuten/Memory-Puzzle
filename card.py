import pygame

class Card:

    def __init__(self):
        self.img = pygame.image.load('img/Boss.png')
        self.pos = (100, 200)


    def draw(self, screen):
        screen.blit(self.img, self.pos)
