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

#Setting up Images
main_bg = pygame.image.load('images/racer/main-bg.png') #BG on game over
background = pygame.image.load("images/racer/bg.png") #BG on playing

#Bg on scroll setup
bg_height = background.get_height()
tiles = math.ceil(SCREEN_HEIGHT / bg_height) + 1 #How many pictures are needed of to cover screen
bg_rect = background.get_rect()
scroll = 0

#Loading all the colors of enemy cars
cars_path = os.path.join(os.getcwd(), 'images/racer/cars')
cars = list()
for image in os.listdir(cars_path) :
    cars.append(pygame.image.load(f'{cars_path}/{image}'))

#Randomly choosing coin image
coin_images = [pygame.image.load('images/racer/coin.png'), pygame.image.load('images/racer/super_coin.png')]
coin_image = coin_images[0]
for i in range(3) :
    coin_images.append(pygame.image.load('images/racer/coin.png'))


#Setting up Sounds
coin_sound = pygame.mixer.Sound('sound/coin.mp3')
game_over_theme_sound = pygame.mixer.Sound('sound/game_over_theme.mp3')
pygame.mixer.music.load('sound/super_mario.mp3')
pygame.mixer.music.play(-1)
 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        #Random car image
        self.image = random.choice(cars)
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (70 ,140))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(95, SCREEN_WIDTH - 95), 0) 
 
      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.image = random.choice(cars)
            self.image = pygame.transform.rotate(self.image, 180)
            self.image = pygame.transform.scale(self.image, (70 ,140))
            self.rect = self.image.get_rect()
            self.rect.top = 0
            self.rect.bottomleft = (random.randint(95, SCREEN_WIDTH - 95), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.random = random.randint(0, len(coin_images) - 1)
        self.image = coin_images[self.random]
        self.image = pygame.transform.scale(self.image, (30 ,30))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(75, SCREEN_WIDTH - 75), 0)

      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.random = random.randint(0, len(coin_images) - 1)
            self.image = coin_images[self.random]
            self.image = pygame.transform.scale(self.image, (30 ,30))
            self.rect.top = 0
            self.rect.center = (random.randint(75, SCREEN_WIDTH - 75), 0)
 
      #When colliding with others(player or enemy)
      def collide(self) :
        self.random = random.randint(0, len(coin_images) - 1)
        self.image = coin_images[self.random]
        self.image = pygame.transform.scale(self.image, (30 ,30))
        self.rect.top = 0
        self.rect.center = (random.randint(75, SCREEN_WIDTH - 75), 0)

      def draw(self, surface):
        surface.blit(self.image, self.rect)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('images/racer/cars/car_blue.png')
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


#Loading for game_over screen
quit_button_image = pygame.image.load('images/racer/quit.jpg')
restart_button_image = pygame.image.load('images/racer/restart.jpg')
quit_button = Button(quit_button_image, (SCREEN_WIDTH - quit_button_image.get_width()) / 2, SCREEN_HEIGHT - 140)
restart_button = Button(restart_button_image, (SCREEN_WIDTH - restart_button_image.get_width()) / 2, SCREEN_HEIGHT - 240)

#Creating Sprite Groups
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
    for event in pygame.event.get():
        if event.type == INC_SPEED and state == 'play':
            if SPEED <= 10 :
                SPEED += 0.5

        if event.type == pygame.MOUSEBUTTONDOWN and quit_button.draw() :
            pygame.quit()
            sys.exit()

        #Reseting progress for restart
        if event.type == pygame.MOUSEBUTTONDOWN and restart_button.draw() :
            SPEED = 5
            SCORE = COINS = 0
            state = 'play'

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Options by keyboard
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE and state == 'game_over' :
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_r and state == 'game_over' :
                SPEED = 5
                SCORE = COINS = 0
                

    if state == 'play' :
        pygame.mixer.music.unpause()
        SCORE += 0.05
        scroll += SPEED - 2
        #BG infinite scroll
        for i in range(0, tiles) :
            screen.blit(background, (0, (i * bg_height) - bg_height + scroll))

        if abs(scroll > bg_height) :
            scroll = 0

        #Score and coins counter
        scores = font_small.render(str(int(SCORE)), True, BLACK)
        coins_text = font_small.render(str(COINS), True, BLACK)
        coin_image = pygame.transform.scale(coin_image, (20, 20))
        #Rectangles under
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - scores.get_width() - 30, 10, scores.get_width() + 20, 30), 0, 5)
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - coin_image.get_width() - coins_text.get_width() - 25, 45, coins_text.get_width() + coin_image.get_width() + 20, 30), 0, 5)
        #Blitting score and coin counter on screen
        screen.blit(scores, (SCREEN_WIDTH - scores.get_width() - 20, 15))    
        screen.blit(coin_image, (SCREEN_WIDTH - coin_image.get_width() - 10, 50))    
        screen.blit(coins_text, (SCREEN_WIDTH - coins_text.get_width() - 30, 50))    
    
        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()

    elif state == 'game_over' :
        #Game over screen
        screen.blit(main_bg, (0, 0))
        screen.blit(game_over, ((SCREEN_WIDTH - game_over.get_width()) / 2, 50))
        your_score = font.render(f'Your score : {int(SCORE)}', True, WHITE)
        screen.blit(your_score, ((SCREEN_WIDTH - your_score.get_width()) / 2, 250))
        quit_button.draw()
        restart_button.draw()

    # Collision between enemy and player
    if pygame.sprite.spritecollideany(P1, enemies):
        E1.rect.top = SCREEN_HEIGHT + 1
        state = 'game_over' 
        pygame.mixer.music.pause()
        game_over_theme_sound.play()

    #Collecting coins
    if pygame.sprite.spritecollideany(P1, coins):
        coin_sound.play()
        #If coin image is usual
        if C1.random != 1 :
            COINS += 1
        #Else, then coin image is super coin
        else :
            COINS += 5
        C1.collide()

    #If coin appeares on top of enemy
    if pygame.sprite.spritecollideany(E1, coins):
        C1.collide()
         
    pygame.display.update()
    FramePerSec.tick(FPS)