import pygame
import random
import math
import time


pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_width, screen_height = screen.get_size()

font = pygame.font.SysFont("Courier New", 20)

running = True

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

def game_over() :
    snake.speed = 0
    time.sleep(2)
    global running
    running = False

class Snake:
    def __init__(self, x, y):
        self.size = 0
        self.elements = [[x, y]]
        for i in range(self.size - 1) :
            self.elements.append([0, 0])
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 1

    def draw(self):
        for i in range(len(self.elements)):
            if 255 - i - 20 >= 0 :
                pygame.draw.circle(screen, (255 - i - 20, 0, 0), self.elements[i], self.radius)
            else :
                pygame.draw.circle(screen, (0, 0, 0), self.elements[i], self.radius)


    def add_to_snake(self):
        self.size += 1
        for i in range(self.size - 1) :
            self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
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
        self.x = random.randint(0, screen_width / 4 * self.index - self.width - 20)
        self.y = random.randint(0, screen_height - self.height - 20)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self) :
        pygame.draw.rect(screen, (98, 50, 50), self.rect)

all_sprites = pygame.sprite.Group()

snake = Snake(0, 0)
food = Food()
wall = Wall(1)
wall1 = Wall(2)
wall2 = Wall(3)
wall3 = Wall(4)

all_sprites.add(wall)
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

    screen.fill((255, 255, 255))
    score = font.render(str(snake.size), True, (0, 0, 0))
    screen.blit(score, (screen_width - score.get_width() - 10, 10))

    if snake.elements[0][0] > screen_width :
        snake.elements[0][0] = 0
    if snake.elements[0][0] < 0 :
        snake.elements[0][0] = screen_width
    if snake.elements[0][1] > screen_height :
        snake.elements[0][1] = 0
    if snake.elements[0][1] < 0 :
        snake.elements[0][1] = screen_height

    if snake.eat(food.x, food.y):
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
    snake.move()
    snake.draw()
    wall.draw()
    wall1.draw()
    wall2.draw()
    wall3.draw()
    pygame.display.flip()

pygame.quit()