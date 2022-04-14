import pygame
import random
import math
import time
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Snake")
#FPS
SPEED = 30

BLUE = (56, 159, 217)
GREEN = (34, 173, 48)
RED = (255, 0, 0)
#Food type depending on randomly chosen color
colors = (RED, GREEN, BLUE, GREEN, GREEN)

#Settin gup font
font = pygame.font.SysFont("Courier New", 20)

#Setting up Sounds
food_sound = pygame.mixer.Sound('sound/eat.mp3')
game_over_theme_sound = pygame.mixer.Sound('sound/game_over_theme.mp3')
pygame.mixer.music.load('sound/super_mario.mp3')
pygame.mixer.music.play(-1)

running = True
state = 'main menu'

#Detecting collision between circle and rectangle (snake and food)
def collision(rleft, rtop, width, height,
              center_x, center_y, radius):
    rright, rbottom = rleft + width/2, rtop + height/2
    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False
    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True
    return False

#Game over function
def game_over() :
    game_over_theme_sound.play()
    global SPEED
    SPEED = 0
    time.sleep(2)
    global state
    state = 'game over'

class Snake:
    def __init__(self, x, y):
        self.size = 0
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.is_add = False
        #Level counter to display on screen
        self.level = 1
        #Counts how many food have been eaten, so that every 4th eaten food adds enw level
        self.count = 0

    def draw(self):
        #Dynamically changing color
        for i in range(self.size + 1):
            if 255 - i - 20 >= 0 :
                #Dynamically changing color depending on its position
                #From red to black gradient
                pygame.draw.circle(screen, (255 - i - 20, 0, 0), self.elements[i], self.radius)
            else :
                pygame.draw.circle(screen, (0, 0, 0), self.elements[i], self.radius)

    #Adding to snake
    def add_to_snake(self, food_color):
        #If food is usual
        if food_color == GREEN :
            self.size += 1
        #Else, food is red or blue
        else :
            self.size += 3
        self.count += 1
        #Add circles depending on size
        for i in range(self.size) :
            self.elements.append([0, 0])

        #If 4 foods are eaten increase level
        if self.count % 4 == 0 :
            time.sleep(0.2)
            global SPEED
            SPEED += 10
            self.level += 1
            #Create new wall
            globals()[f'wall{self.level}'] = Wall(self.level)
            all_sprites.add(globals()[f'wall{self.level}'])

    def move(self):
        for i in range(self.size, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        #If head heats other parts of snake's body
        for i in range(self.size - 1, 1, -1) :
            if self.elements[0] == self.elements[i] :
                game_over()

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, foodx, foody, foodw):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx - 10 <= x <= foodx + foodw + 10 and foody - 10 <= y <= foody + foodw + 10:
            return True
        return False

    #Not to appear food on top of snake
    def food(self, foodx, foody, foodw) :
        for i in range(self.size) :
            x = self.elements[i][0]
            y = self.elements[i][1]
            if collision(foodx, foody, foodw, foodw, x, y, self.radius) :
                return True

    #Wall collision
    def wall(self, wallx, wally, wallw, wallh) :
        x = self.elements[0][0]
        y = self.elements[0][1]
        if wallx <= x <= wallx + wallw and wally <= y <= wally + wallh:
            return True
        return False

class Food:
    def __init__(self):
        #Choose color randomly (green, blue, red)
        self.color = random.choice(colors)
        self.x = random.randint(0, screen_width - 20)
        self.y = random.randint(0, screen_height - 20)
        #If color is not green, make food bigger
        self.w = 20 if self.color == GREEN else 30

    def gen(self):
        self.color = random.choice(colors)
        #If color is not green, make food bigger
        self.w = 20 if self.color == GREEN else 30
        self.x = random.randint(0, screen_width - self.w)
        self.y = random.randint(0, screen_height - self.w)

    def draw(self):
        if self.color == RED :
            #If color is red make circle
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.w), 0, int(self.w / 2))
        else :
            #Else, rectangle
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.w))


class Wall(pygame.sprite.Sprite) :
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.dimensions = (20, random.randint(100, 200))
        self.choose = random.randint(0, 1)
        self.width = self.dimensions[self.choose]
        self.height = self.dimensions[0] if self.choose == 1 else self.dimensions[1]
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def gen(self) :
        self.width = self.dimensions[self.choose]
        self.height = self.dimensions[0] if self.choose == 1 else self.dimensions[1]
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    #If wall appears on top of another
    def wallCheck(self, object) :
        if self.rect is not object.rect and self.rect.colliderect(object.rect) :
            object.gen()

    def draw(self) :
        pygame.draw.rect(screen, (98, 50, 50), self.rect)

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

#Sprites for walls
all_sprites = pygame.sprite.Group()

snake = Snake(0, 0)
food = Food()

d = 5

#Loading images for buttons
main_menu_bg_load = pygame.image.load('images/snake/main_menu_snake.jpg')
main_menu_bg = Button(main_menu_bg_load, 0, 0)
main_menu_play_load = pygame.image.load('images/snake/play_button_snake.png')
main_menu_play = Button(main_menu_play_load, (screen_width - main_menu_play_load.get_width()) / 2, 300)
main_menu_quit_load = pygame.image.load('images/snake/quit_button_snake.png')
main_menu_quit = Button(main_menu_quit_load, (screen_width - main_menu_quit_load.get_width()) / 2, 400)
main_menu_restart_load = pygame.image.load('images/snake/restart_button_snake.png')
main_menu_restart = Button(main_menu_restart_load, (screen_width - main_menu_restart_load.get_width()) / 2, 300)

clock = pygame.time.Clock()

while running:
    #FPS depending on speed
    clock.tick(SPEED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d

        if event.type == pygame.MOUSEBUTTONDOWN and main_menu_play.draw() :
            state = 'play'
        if event.type == pygame.MOUSEBUTTONDOWN and main_menu_quit.draw() :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and main_menu_restart.draw() :
            #Reseting all the progress
            screen.fill((0, 0, 0))
            state = 'play'
            #FPS back to 30
            SPEED = 30
            #Snake reset
            snake.size = 0
            snake.level = 1
            snake.elements.clear()
            snake.elements.append([0, 0])
            snake.dx = d
            snake.dy = 0
            #Removing all walls
            for object in all_sprites :
                object.kill()

    if state == 'main menu' :
        #Buttons for starter main menu
        main_menu_bg.draw()
        main_menu_play.draw()
        main_menu_quit.draw()
    elif state == 'play' :
        screen.fill((255, 255, 255))
        #Reaching the borders
        if snake.elements[0][0] > screen_width :
            snake.elements[0][0] = 0
        if snake.elements[0][0] < 0 :
            snake.elements[0][0] = screen_width
        if snake.elements[0][1] > screen_height :
            snake.elements[0][1] = 0
        if snake.elements[0][1] < 0 :
            snake.elements[0][1] = screen_height

        #Eating food
        if snake.eat(food.x, food.y, food.w):
            food_sound.play()
            snake.add_to_snake(food.color)
            food.gen()

        #If food appears on top of snake, it generates new food
        if snake.food(food.x, food.y, food.w) :
            food.gen()

        #Drawing walls
        for object in all_sprites :
            object.draw()
            #Checking if wall appears on top of another
            for objects in all_sprites :
                object.wallCheck(objects)
            
            #Check if snake collides with walls
            if snake.wall(object.x, object.y, object.width, object.height) :
                game_over()

            #Checking if food appears on top of walls
            if object.rect.colliderect((food.x, food.y, food.w, food.w)):
                food.gen()


        snake.move()
        food.draw()
        #Timer for red food
        if food.color == RED :
            if food.w >= 0:
                food.w -= 0.1
            if food.w < 0 :
                food.gen()

        snake.draw()
        #Score and level text
        score = font.render(str(snake.size), True, (0, 0, 0))
        lvl = font.render(f"lvl: {str(snake.level)}", True, (0, 0, 0))
        screen.blit(score, (screen_width - score.get_width() - 10, 10))
        screen.blit(lvl, (screen_width - lvl.get_width() - 10, 30))

    elif state == 'game over' :
        #game over menu
        main_menu_bg.draw()
        main_menu_restart.draw()
        main_menu_quit.draw()

    pygame.display.flip()

pygame.quit()