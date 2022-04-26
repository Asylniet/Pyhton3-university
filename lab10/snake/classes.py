import time
import random
import math
import pygame
import params
import connection as cn


coin_sound = pygame.mixer.Sound('sound/coin.mp3')

class Wall(pygame.sprite.Sprite) :
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
        
    def draw(self) :
        pygame.draw.rect(params.screen, (98, 50, 50), self.rect)

def updateLevel() :
    sql = f'''
        select *
        from user_score
        where level = {cn.user_data[3]}
    '''
    cn.cursor.execute(sql)
    global level_data
    level_data = cn.cursor.fetchone()

def createWall() :
    for i in range(len(level_data[1])) :
        values = level_data[1][i]
        for j in range(len(values)) :
            values[j] = int(values[j])
        globals()[f'wall{i + 1}'] = Wall(pygame.Rect(values))
        params.all_sprites.add(globals()[f'wall{i + 1}'])
    # params.pygame.display.update()

cn.updateUserLevel()
updateLevel()
createWall()

#FPS
SPEED = level_data[2]

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


class Snake:
    def __init__(self, x, y):
        self.size = 0
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.is_add = False
        #Level counter to display on screen
        self.level = cn.user_data[3]
        self.count = 0

    def draw(self):
        for i in range(self.size + 1):
            if params.ghost == False :
                pygame.draw.circle(params.screen, (255, 0, 0), self.elements[i], self.radius)
            else :
                pygame.draw.circle(params.screen, (238, 238, 238), self.elements[i], self.radius)

    #Adding to snake
    def add_to_snake(self, food_color):
        #If food is usual
        if food_color == params.GREEN :
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
            coin_sound.play()
            params.ghost = True
            pygame.time.set_timer(params.TIMER, 0)
            pygame.time.set_timer(params.TIMER, 2000)
            self.level += 1
            sql = f'''
                update users
                set level = {self.level}
                where name = \'{cn.user}\'
            '''
            cn.cursor.execute(sql)
            cn.conn.commit()
            cn.updateUserLevel()
            updateLevel()
            global SPEED
            SPEED = level_data[2]
            createWall()

    def move(self):
        for i in range(self.size, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        #If head heats other parts of snake's body
        for i in range(self.size - 1, 1, -1) :
            if self.elements[0] == self.elements[i] :
                return True

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
        self.color = random.choice(params.colors)
        self.x = random.randint(0, params.screen_width - 20)
        self.y = random.randint(0, params.screen_height - 20)
        #If color is not green, make food bigger
        self.w = 20 if self.color == params.GREEN else 30

    def gen(self):
        self.color = random.choice(params.colors)
        #If color is not green, make food bigger
        self.w = 20 if self.color == params.GREEN else 30
        self.x = random.randint(0, params.screen_width - self.w)
        self.y = random.randint(0, params.screen_height - self.w)

    def draw(self):
        if self.color == params.RED :
            #If color is red make circle
            pygame.draw.rect(params.screen, self.color, (self.x, self.y, self.w, self.w), 0, int(self.w / 2))
        else :
            #Else, rectangle
            pygame.draw.rect(params.screen, self.color, (self.x, self.y, self.w, self.w))

class Button() :
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self) :
        params.screen.blit(self.image, self.rect.topleft)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) :
            return True