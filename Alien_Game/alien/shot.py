import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, alien_game):
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect1 = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect2 = pygame.Rect(0,0,self.settings.bullet_width_1,self.settings.bullet_height_1)
        self.rect.topleft = alien_game.ship.rect.topleft
        self.rect1.topright = alien_game.ship.rect.topright
        self.rect2.midtop = alien_game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.y = float(self.rect1.y)
        self.y = float(self.rect2.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        self.rect1.y = self.y
        self.rect2.y = self.y

    def draw_bul(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,self.color,self.rect1)
        pygame.draw.rect(self.screen,self.color,self.rect2)

