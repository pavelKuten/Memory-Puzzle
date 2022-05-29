import pygame
import sys
import random
from card import Card


class Interface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (0, 0, 0)
        self.cards = []
        self.selected = False
        self.place_cards()

    def place_cards(self):
        img_names = ['img/blue.jpg', 'img/blue.jpg', 'img/green.jpg', 'img/green.jpg', 'img/orange.jpg'
            , 'img/orange.jpg', 'img/purple.jpg', 'img/purple.jpg', 'img/red.jpg', 'img/red.jpg'
            , 'img/yellow.jpg', 'img/yellow.jpg']
        for x in range(4):
            for y in range(3):
                self.cards.append(
                    Card(img_names.pop(random.randint(0, len(img_names) - 1)), (x * 250 + 110, y * 250 + 50)))

    def start(self):

        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    for card in self.cards:
                        if card.pos[0] < pos[0] < card.pos[0] + 200 and \
                                card.pos[1] < pos[1] < card.pos[1] + 200:
                            if card.hidden:
                                card.hidden = False
                                if self.selected:
                                    ...
                                else:
                                    self.selected = True
                            else:
                                card.hidden = True
                                self.selected = False


    def draw(self):
        self.screen.fill((0, 0, 0))
        for card in self.cards:
            card.draw(self.screen)
        pygame.display.update()


interface = Interface()
interface.start()
