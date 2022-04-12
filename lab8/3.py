import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Making brush and color of shapes seperately
color = brushcolor = RED

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

#setting up fonts
font= pygame.font.SysFont("Courier New", 20)

isMouseDown = False

#Positions of mouse when drawing shapes
prevX = -1
prevY = -1
currentX = -1
currentY = -1

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
baseLayer = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True

prev = None

screen.fill(WHITE)
baseLayer.fill(WHITE)
#Starting tool is brush
state = 'brush'
#Changing mouse
pygame.mouse.set_cursor(pygame.cursors.diamond)

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateCircleCenter(x1, y1, x2, y2) :
    return (min(x1, x2), min(y1, y2))

def calculateCircleRadius(x1, y1, x2, y2) :
    return abs(abs(x1 - x2) - abs(y1 - y2))

while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_ESCAPE :
            running = False
        if event.key == pygame.K_r :
            state = 'rect'
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
        if event.key == pygame.K_b :
            state = 'brush'
            brushcolor = color
            pygame.mouse.set_cursor(pygame.cursors.diamond)
        if event.key == pygame.K_e :
            #Eraser
            state = 'brush'
            brushcolor = WHITE
            pygame.mouse.set_cursor(pygame.cursors.tri_left)
        if event.key == pygame.K_k :
            color = brushcolor = RED
        if event.key == pygame.K_g :
            color = brushcolor = GREEN
        if event.key == pygame.K_s :
            color = brushcolor = BLUE
        if event.key == pygame.K_c :
            state = 'circle'
            pygame.mouse.set_cursor(pygame.cursors.ball)

    if state == 'brush':
        if pygame.mouse.get_pressed()[0]:
            screen.blit(baseLayer, (0, 0))
            currentX, currentY = pygame.mouse.get_pos()
            if prev is not None :
                prevX, prevY = prev
                for x in range(20) :
                    for y in range(20) :
                        pygame.draw.line(baseLayer, brushcolor, 
                        (prevX + x - 10, prevY + y - 20), 
                        (currentX + x - 10, currentY + y - 20))
            prev = (currentX, currentY)
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
            screen.blit(baseLayer, (0, 0))
    elif state == 'rect' or state == 'circle':
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            baseLayer.blit(screen, (0, 0))


        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                currentX =  event.pos[0]
                currentY =  event.pos[1]

        if state == 'rect':  
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX, prevY, currentX, currentY)
                pygame.draw.rect(screen, color, pygame.Rect(r), 1)
        elif state == 'circle':
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                center = calculateCircleCenter(prevX, prevY, currentX, currentY)
                radius = calculateCircleRadius(prevX, prevY, currentX, currentY)
                pygame.draw.circle(screen, color, center, radius, 1)

  pygame.display.flip()


  clock.tick(60)


pygame.quit()