import time
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
        self.selected_card = None
        self.place_cards()
        self.point = 0

    def place_cards(self):
        img_names = ['img/blue.jpg', 'img/blue.jpg', 'img/green.jpg', 'img/green.jpg', 'img/orange.jpg'
            , 'img/orange.jpg', 'img/purple.jpg', 'img/purple.jpg', 'img/red.jpg', 'img/red.jpg'
            , 'img/yellow.jpg', 'img/yellow.jpg']
        for x in range(4):
            for y in range(3):
                card_name = img_names.pop(random.randint(0, len(img_names) - 1))
                self.cards.append(
                    Card(card_name, (x * 250 + 110, y * 250 + 50), img_names.count(card_name)))

    def start(self):

        while True:
            self.draw()
            if self.point == 12:
                self.screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 150)
                text = font.render("You are winner!", True, [255, 255, 255])
                textpos = (250, 300)
                self.screen.blit(text, textpos)
                pygame.display.update()
                time.sleep(1)
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    for card in self.cards:
                        if card.pos[0] < pos[0] < card.pos[0] + 200 and \
                                card.pos[1] < pos[1] < card.pos[1] + 200:
                            if card.hidden:
                                card.hidden = False
                                if self.selected:
                                    if self.selected_card.img_name == card.img_name and self.selected_card.index != card.index:
                                        self.draw()
                                        time.sleep(0.4)
                                        self.mark_deleted(card.img_name)
                                        self.point += 2
                                    else:
                                        self.draw()
                                        time.sleep(0.4)
                                        self.mark_hidden(card.img_name)
                                        self.mark_hidden(self.selected_card.img_name)
                                        self.selected_card = None
                                        self.selected = False
                                else:
                                    self.selected = True
                                    self.selected_card = card
                            else:
                                card.hidden = True
                                self.selected = False



    def draw(self):
        self.screen.fill((0, 0, 0))
        for card in self.cards:
            card.draw(self.screen)
        pygame.display.update()


    def mark_deleted(self, card_name):
        for card in self.cards:
            if card.img_name == card_name:
                card.deleted = True

    def mark_hidden(self, card_name):
        for card in self.cards:
            if card.img_name == card_name:
                card.hidden = True




interface = Interface()
interface.start()