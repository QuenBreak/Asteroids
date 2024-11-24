import pygame
from constants import *


class Text_Box():
    def __init__(self, font, font_size, text, text_color):
        self.font = pygame.font.Font(font, font_size)
        self.text = pygame.font.Font.render(self.font, text, True, text_color)
        self.text_background = self.text.get_rect()
        self.text_background.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def show_text (self, screen, color):
        screen.fill(color)
        screen.blit(self.text, self.text_background)