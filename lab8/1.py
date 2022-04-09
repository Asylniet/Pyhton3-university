import pygame
import random
import os
import math
import sys
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("Courier New", 40)
font_small = pygame.font.SysFont("Courier New", 20)
game_over = font.render("Game Over", True, WHITE)

main_bg = pygame.image.load('images/main-bg.png')
background = pygame.image.load("images/bg.png")
bg_height = background.get_height()
tiles = math.ceil(SCREEN_HEIGHT / bg_height) + 1
bg_rect = background.get_rect()
scroll = 0

coin_sound = pygame.mixer.Sound('sound/coin.mp3')
game_over_theme_sound = pygame.mixer.Sound('sound/game_over_theme.mp3')
pygame.mixer.music.load('sound/super_mario.mp3')
pygame.mixer.music.play(-1)
 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Racer")
coin_image = pygame.image.load('images/coin.png')
cars_path = os.path.join(os.getcwd(), 'images/cars')
cars = os.listdir(cars_path)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f'images/cars/{cars[random.randint(0, len(cars) - 1)]}')
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (70 ,140))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(95, SCREEN_WIDTH - 95), 0) 
 
      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.image = pygame.image.load(f'images/cars/{cars[random.randint(0, len(cars) - 1)]}')
            self.image = pygame.transform.rotate(self.image, 180)
            self.image = pygame.transform.scale(self.image, (70 ,140))
            self.rect = self.image.get_rect()
            self.rect.top = 0
            self.rect.center = (random.randint(95, SCREEN_WIDTH - 95), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (30 ,30))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(75, SCREEN_WIDTH - 75), 0) 
 
      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(75, SCREEN_WIDTH - 75), 0)
 
      def collide(self) :
          self.rect.top = 0
          self.rect.center = (random.randint(75, SCREEN_WIDTH - 75), 0)

      def draw(self, surface):
        surface.blit(self.image, self.rect)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/cars/car_red.png")
        self.image = pygame.transform.scale(self.image, (70 ,140))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(10, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     

class Button() :
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self) :
        screen.blit(self.image, self.rect.topleft)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) :
            return True

P1 = Player()
E1 = Enemy()
C1 = Coin()

quit_button_image = pygame.image.load('images/quit.jpg')
restart_button_image = pygame.image.load('images/restart.jpg')
quit_button = Button(quit_button_image, (SCREEN_WIDTH - quit_button_image.get_width()) / 2, SCREEN_HEIGHT - 140)
restart_button = Button(restart_button_image, (SCREEN_WIDTH - restart_button_image.get_width()) / 2, SCREEN_HEIGHT - 240)

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

state = 'play'
while True:     
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED and state == 'play':
            if SPEED <= 10 :
                SPEED += 0.5

        if event.type == pygame.MOUSEBUTTONDOWN and quit_button.draw() :
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and restart_button.draw() :
            SPEED = 5
            SCORE = COINS = 0
            state = 'play'

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE and state == 'game_over' :
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_r and state == 'game_over' :
                SPEED = 5
                SCORE = COINS = 0
                state = 'play'

    if state == 'play' :
        pygame.mixer.music.unpause()
        SCORE += 0.05
        scroll += SPEED - 2
        for i in range(0, tiles) :
            screen.blit(background, (0, (i * bg_height) - bg_height + scroll))

        if abs(scroll > bg_height) :
            scroll = 0

        scores = font_small.render(str(int(SCORE)), True, BLACK)
        coins_text = font_small.render(str(COINS), True, BLACK)
        coin_image = pygame.transform.scale(coin_image, (20, 20))
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - scores.get_width() - 30, 10, scores.get_width() + 20, 30), 0, 5)
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - coin_image.get_width() - coins_text.get_width() - 25, 45, coins_text.get_width() + coin_image.get_width() + 20, 30), 0, 5)
        screen.blit(scores, (SCREEN_WIDTH - scores.get_width() - 20, 15))    
        screen.blit(coin_image, (SCREEN_WIDTH - coin_image.get_width() - 10, 50))    
        screen.blit(coins_text, (SCREEN_WIDTH - coins_text.get_width() - 30, 50))    
    
        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()

    elif state == 'game_over' :
        screen.blit(main_bg, (0, 0))
        screen.blit(game_over, ((SCREEN_WIDTH - game_over.get_width()) / 2, 50))
        your_score = font.render(f'Your score : {int(SCORE)}', True, WHITE)
        screen.blit(your_score, ((SCREEN_WIDTH - your_score.get_width()) / 2, 250))
        quit_button.draw()
        restart_button.draw()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        E1.rect.top = SCREEN_HEIGHT + 1
        state = 'game_over' 
        pygame.mixer.music.pause()
        game_over_theme_sound.play()

    if pygame.sprite.spritecollideany(P1, coins):
        coin_sound.play()
        C1.collide()
        COINS += 1   

    if pygame.sprite.spritecollideany(E1, coins):
        C1.collide()
         
    pygame.display.update()
    FramePerSec.tick(FPS)