import pygame
import random
import math
import time


pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_width, screen_height = screen.get_size()

font = pygame.font.SysFont("Courier New", 20)

#Setting up Sounds
food_sound = pygame.mixer.Sound('sound/eat.mp3')
game_over_theme_sound = pygame.mixer.Sound('sound/game_over_theme.mp3')
pygame.mixer.music.load('sound/super_mario.mp3')
pygame.mixer.music.play(-1)

running = True
state = 'main menu'

#Detecting collision between circle and rectangle
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

#When losing
def game_over() :
    game_over_theme_sound.play()
    snake.speed = 0
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
        self.speed = 1
        self.level = 1

    def draw(self):
        #Dynamically changing color
        for i in range(self.size + 1):
            if 255 - i - 20 >= 0 :
                pygame.draw.circle(screen, (255 - i - 20, 0, 0), self.elements[i], self.radius)
            else :
                pygame.draw.circle(screen, (0, 0, 0), self.elements[i], self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 4 == 0 :
            self.speed += 0.1
            self.level += 1

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        for i in range(self.size - 1, 1, -1) :
            if self.elements[0] == self.elements[i] :
                game_over()

        self.elements[0][0] += self.speed * self.dx
        self.elements[0][1] += self.speed * self.dy

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx - 10 <= x <= foodx + 40 and foody - 10 <= y <= foody + 40:
            return True
        return False

    def food(self, foodx, foody) :
        for i in range(self.size) :
            x = self.elements[i][0]
            y = self.elements[i][1]
            if collision(foodx, foody, 20, 20, x, y, self.radius) :
                return True

    def wall(self, wallx, wally, wallw, wallh) :
        x = self.elements[0][0]
        y = self.elements[0][1]
        if wallx <= x <= wallx + wallw and wally <= y <= wally + wallh:
            return True
        return False

class Food:
    def __init__(self):
        self.x = random.randint(0, screen_width - 20)
        self.y = random.randint(0, screen_height - 20)

    def gen(self):
        self.x = random.randint(0, screen_width - 20)
        self.y = random.randint(0, screen_height - 20)

    def draw(self):
        pygame.draw.rect(screen, (34, 173, 48), (self.x, self.y, 20, 20))


class Wall(pygame.sprite.Sprite) :
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.dimensions = (20, random.randint(100, 200))
        self.choose = random.randint(0, 1)
        self.width = self.dimensions[self.choose]
        self.height = self.dimensions[0] if self.choose == 1 else self.dimensions[1]
        #Making walls appear on different parts of screen
        if self.index == 1 :
            self.x = random.randint(0, screen_width / 2 - self.width)
            self.y = random.randint(0, screen_height / 2 - self.height)
        elif self.index == 2 :
            self.x = random.randint(screen_width / 2, screen_width - self.width)
            self.y = random.randint(0, screen_height / 2  - self.height)
        elif self.index == 3 :
            self.x = random.randint(0, screen_width / 2 - self.width)
            self.y = random.randint(screen_height / 2, screen_height - self.height)
        elif self.index == 4 :
            self.x = random.randint(screen_width / 2, screen_width - self.width)
            self.y = random.randint(screen_height / 2, screen_height - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def gen(self) :
        self.width = self.dimensions[self.choose]
        self.height = self.dimensions[0] if self.choose == 1 else self.dimensions[1]
        if self.index == 1 :
            self.x = random.randint(0, screen_width / 2 - self.width)
            self.y = random.randint(0, screen_height / 2 - self.height)
        elif self.index == 2 :
            self.x = random.randint(screen_width / 2, screen_width - self.width)
            self.y = random.randint(0, screen_height / 2  - self.height)
        elif self.index == 3 :
            self.x = random.randint(0, screen_width / 2 - self.width)
            self.y = random.randint(screen_height / 2, screen_height - self.height)
        elif self.index == 4 :
            self.x = random.randint(screen_width / 2, screen_width - self.width)
            self.y = random.randint(screen_height / 2, screen_height - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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

all_sprites = pygame.sprite.Group()

snake = Snake(0, 0)
food = Food()
wall = Wall(1)
wall1 = Wall(2)
wall2 = Wall(3)
wall3 = Wall(4)

all_sprites.add(wall)

#Checking if walls appear on top of each-other
if wall.rect.colliderect(wall1.rect) :
    wall1.gen()
else :
    all_sprites.add(wall1)

if wall1.rect.colliderect(wall2.rect) :
    wall2.gen()
else :  
    all_sprites.add(wall2)

if wall2.rect.colliderect(wall3.rect) :
    wall3.gen()
else :  
    all_sprites.add(wall3)

FPS = 60
d = 5

#Loading images for buttons
main_menu_bg_load = pygame.image.load('images/main_menu_snake.jpg')
main_menu_bg = Button(main_menu_bg_load, 0, 0)
main_menu_play_load = pygame.image.load('images/play_button_snake.png')
main_menu_play = Button(main_menu_play_load, (screen_width - main_menu_play_load.get_width()) / 2, 300)
main_menu_quit_load = pygame.image.load('images/quit_button_snake.png')
main_menu_quit = Button(main_menu_quit_load, (screen_width - main_menu_quit_load.get_width()) / 2, 400)
main_menu_restart_load = pygame.image.load('images/restart_button_snake.png')
main_menu_restart = Button(main_menu_restart_load, (screen_width - main_menu_restart_load.get_width()) / 2, 300)

clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
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
            snake.size = 0
            snake.speed = 1
            snake.level = 1
            snake.elements.clear()
            snake.elements.append([0, 0])
            snake.dx = d
            snake.dy = 0
            for object in all_sprites :
                object.gen()

    if state == 'main menu' :
        main_menu_bg.draw()
        main_menu_play.draw()
        main_menu_quit.draw()
    elif state == 'play' :
        screen.fill((255, 255, 255))
        if snake.elements[0][0] > screen_width :
            snake.elements[0][0] = 0
        if snake.elements[0][0] < 0 :
            snake.elements[0][0] = screen_width
        if snake.elements[0][1] > screen_height :
            snake.elements[0][1] = 0
        if snake.elements[0][1] < 0 :
            snake.elements[0][1] = screen_height

        if snake.eat(food.x, food.y):
            food_sound.play()
            snake.is_add = True
            food.gen()

        if snake.food(food.x, food.y) :
            food.gen()

        for object in all_sprites :
            if snake.wall(object.x, object.y, object.width, object.height) :
                game_over()

            if object.rect.colliderect((food.x, food.y, 20, 20)):
                food.gen()

        food.draw()
        snake.draw()
        snake.move()
        wall.draw()
        wall1.draw()
        wall2.draw()
        wall3.draw()
        #Score and level text
        score = font.render(str(snake.size), True, (0, 0, 0))
        lvl = font.render(f"lvl: {str(snake.level)}", True, (0, 0, 0))
        screen.blit(score, (screen_width - score.get_width() - 10, 10))
        screen.blit(lvl, (screen_width - lvl.get_width() - 10, 30))

    elif state == 'game over' :
        main_menu_bg.draw()
        main_menu_restart.draw()
        main_menu_quit.draw()

    pygame.display.flip()

pygame.quit()