from traceback import print_tb
import pygame
import random
import math


pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_width, screen_height = screen.get_size()

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

class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        for i in range(self.size - 1) :
            self.elements.append([0, 0])
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 1

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
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
                pass

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
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 20, 20))


class Wall :
    def __init__(self):
        self.dimensions = (20, random.randint(100, 200))
        self.choose = random.randint(0, 1)
        self.width = self.dimensions[self.choose]
        self.height = self.dimensions[0] if self.choose == 1 else self.dimensions[1]
        self.x = random.randint(0, screen_width - self.width - 20)
        self.y = random.randint(0, screen_width - self.height - 20)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self) :
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

snake = Snake(100, 100)
food = Food()
wall = Wall()
wall1 = Wall()
wall2 = Wall()

running = True

FPS = 60
d = 5

clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                food.gen()
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

    if snake.wall(wall.x, wall.y, wall.width, wall.height) :
        print("collide")

    if wall.rect.colliderect((food.x, food.y, 20, 20)) :
        food.gen()

    screen.fill((0, 0, 0))
    food.draw()
    snake.draw()
    snake.move()
    wall.draw()
    wall1.draw()
    wall2.draw()
    pygame.display.flip()

pygame.quit()