import pygame


class Card:
    def __init__(self, img_name, pos, index):
        self.img_name = img_name
        self.back_side_img_name = 'img/white.jpg'
        self.img = pygame.image.load(self.img_name)
        self.back_side_img = pygame.image.load(self.back_side_img_name)
        self.hidden = True
        self.deleted = False
        self.pos = pos
        self.index = index

    def draw(self, screen):
        if not self.hidden and not self.deleted:
            screen.blit(self.img, self.pos)
        elif not self.deleted:
            screen.blit(self.back_side_img, self.pos)