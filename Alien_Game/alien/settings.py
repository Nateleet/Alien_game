import pygame
class Settings():

    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.background_color = pygame.image.load('images/background.bmp')
        self.ship_speed = 4
        self.alien_speed = 3.5
        self.fleet_drop = 47
        self.fleet_dir = 1
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 50
        self.bullet_width_1 = 6
        self.bullet_height_1 = 55
        self.bullet_color = (230, 0, 0)
        self.bullet_allowed = 1
        self.score = '0'
        
