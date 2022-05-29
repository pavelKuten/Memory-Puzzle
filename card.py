import pygame


class Card:
    def __init__(self, img_name, pos):
        self.img_name = img_name
        self.back_side_img_name = 'img/white.jpg'
        self.img = pygame.image.load(self.img_name)
        self.back_side_img = pygame.image.load(self.back_side_img_name)
        self.hidden = False
        self.pos = pos

    def draw(self, screen):
        if self.hidden:
            screen.blit(self.img, self.pos)
        else:
            screen.blit(self.back_side_img, self.pos)

