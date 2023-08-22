import sys
import pygame
from settings import Settings
from ship import Ship
from shot import Bullet
from alien_1 import Alien
import random
from time import sleep


class Invasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("Invasion")
        self.f1 = pygame.font.Font('font/slkscre.ttf', 150)
        self.f2 = pygame.font.Font('font/slkscre.ttf', 56)
        self.screen_rect = self.screen.get_rect()
        self.score = '0'
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.game_active = False
        self.fleet()
        pygame.mouse.set_visible(False)
        with open('record.txt', 'r') as f:
                    self.rec = int(f.read())
                    

                    
    
    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.bul_upd()
            self.alien_upd()
            self.upd_screen()
            

            
    def upd_screen(self):
        self.text_score = self.f2.render(f"Score:{self.score_1()}", False, (230,0,0))
        self.text_record = self.f2.render(f"Record:{self.rec}", False, (230,0,0))
        self.text_game_over = self.f1.render("GAME OVER", False, (230,0,0))
        self.text_new_record = self.f1.render("New record!", False, (230,0,0))
        self.screen.blit(self.settings.background_color, (0,0))
        self.screen.blit(self.text_score, (0,960))
        self.screen.blit(self.text_record, (0,1020))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bul()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    
        

    def check_events(self):
        for event in pygame.event.get():
            self.exit(event)
            self.key_down(event)
            self.key_up(event)
            


    
            
    

    def exit(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
        
    


    def key_down(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.ship.moving_right = True
            elif event.key == pygame.K_a:
                self.ship.moving_left = True
            elif event.key == pygame.K_w:
                self.ship.moving_up = True
            elif event.key == pygame.K_s:
                self.ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                    self.fire()
                
                    
    def key_up(self,event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.ship.moving_right = False
            elif event.key == pygame.K_a:
                self.ship.moving_left = False
            elif event.key == pygame.K_w:
                self.ship.moving_up = False
            elif event.key == pygame.K_s:
                self.ship.moving_down = False

                

    def fire(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(ai)
            self.bullets.add(new_bullet)
    

    def bul_upd(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self.colis()

    def fleet(self):
        x = random.randint(200, 500)
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        self.random_alien()
        ship_height = self.ship.rect.height
        space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        rows = space_y // alien_height
        for row_num in range(rows):             
            for num in range(self.random_alien()):
                self.alien1(num,row_num)
                

    def alien1(self, num, row_num):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 1.7 * alien_width * num
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_num - 1400
        self.aliens.add(alien)

    def alien_upd(self):
        self.check_fleet()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens) or self.check_Earth_over():
            self.aliens.empty()
            self.bullets.empty()
            self.last_game = self.score_1()
            self.last_game = int(self.last_game)
            if self.last_game > self.rec:       
                with open('record.txt', 'w') as f:
                    self.records()
                    self.screen.blit(self.text_game_over, (410,410))
            else:
                self.screen.blit(self.text_game_over, (410,410))

            self.new_rec = self.last_game
            if self.new_rec > self.rec:
                self.rec = self.new_rec
                self.text_record = self.f2.render(f"Record:{self.rec}", False, (230,0,0))
            pygame.display.update()
            sleep(3)
            self.score = '0'
            self.ship.new_ship()
            

    def records(self):      
            self.screen.blit(self.text_record, (0,1020))
            with open('record.txt', 'w') as f:
                self.line = f.write(str(self.last_game))
                self.screen.blit(self.text_new_record, (330,600)) 
            


    def check_fleet(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_dir()
                break
            if alien.check_over():
                return True
            
    def check_Earth_over(self):
        for alien in self.aliens.sprites():
            if alien.check_over():
                return True
        


    def change_fleet_dir(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop
        self.settings.fleet_dir *= -1
        


    def random_alien(self):
        space_x = self.settings.screen_width
        x = random.randint(200,400)
        num_aliens = space_x // x
        return num_aliens
    

    def colis(self):
        self.colisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
            



        if not self.aliens:
            self.bullets.empty()
            self.fleet()


    def score_1(self):
        if self.colisions:
            self.score = int(self.score)
            self.score += 10
            self.score = str(self.score)
        return self.score
       





ai = Invasion()
ai.run_game()
        