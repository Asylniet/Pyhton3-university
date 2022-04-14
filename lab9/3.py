import math
import pygame

pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

#setting up fonts
font = pygame.font.SysFont("Courier New", 20)

#Initial colors for surfaces
WHITE = (255, 255, 255)
GRAY = (244, 244, 244)


#Colors to choose
colors = (
    (0, 0, 0),
    (153, 153, 153),
    (255, 255, 255),
    (255, 0, 120),
    (255, 153, 0),
    (121, 65, 0),
    (233, 0, 0),
    (83, 255, 234),
    (255, 255, 0),
    (5, 255, 0),
    (0, 178, 255),
    (143, 0, 255)
)

#Tool buttons
buttons = list()
tools = ('brush', 'eraser', 'rectangle', 'romb', 'circle', 'triangle')

for tool in tools :
    buttons.append(pygame.image.load(f'images/paint/{tool}.png'))

bucket = pygame.image.load('images/paint/bucket_black.png')

#Making brush and color of shapes seperately
color = brushcolor = colors[0]
width = brushWidth = 1

#Blue chosen indicator rectangles
colorChooseRect = pygame.Rect(1017, 522, 68, 68)
buttonChooseRect = pygame.Rect(1016, 16, 95, 95)
circleChooseRect = pygame.Rect(1130, 303, 40, 40)


#When mouse is pressed
isMouseDown = False
#When cursor on painting area
paint = True
#Prev position of cursor
prev = None

#Positions of mouse when drawing shapes
prevX = prevY = currentX = currentY = -1

#BaseLayer for drawing
baseLayer = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
#ToolsLayer for displaying tools
toolsLayer = pygame.Surface((400, WINDOW_HEIGHT))
toolsLayerRect = toolsLayer.get_rect()
toolsLayerRect.left = 1000

screen.fill(WHITE)
baseLayer.fill(WHITE)
toolsLayer.fill(GRAY)

#Starting tool is brush
state = 'brush'

#Functions for shapes
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateSquare(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))

def calculateCircle(x1, y1, x2, y2) :
    return ( (min(x1, x2), min(y1, y2)), abs(abs(x1 - x2) - abs(y1 - y2)) )

def calculateRomb(x1, y1, x2, y2) :
    top = (x1 + abs(x1 - x2) / 2, y1)
    bottom = (x1 + abs(x1 - x2) / 2, y2)
    right = (x2, y1 + abs(y1 - y2) / 2)
    left = (x1, y1 + abs(y1 - y2) / 2)
    return (top, right, bottom, left)

def calculateRightRomb(x1, y1, x2, y2) :
    top = (x1 + abs(x1 - x2) / 2, y1)
    bottom = (top[0], y1 + abs(x1 - x2))
    left = (x1, y1 + abs(x1 - x2) / 2)
    right = (x2, left[1])
    return (top, right, bottom, left)

def calculateTriangle(x1, y1, x2, y2) :
    top = (x1 + abs(x1 - x2) / 2, y1)
    left = (x1, y2)
    right = (x2, y2)
    return (top, left, right)

def calculateEqualTriangle(x1, y1, x2, y2) :
    distance = abs(x1 - x2)
    height = math.sqrt( distance ** 2 - (distance / 2) ** 2 )
    top = (x1 + distance / 2, y1)
    left = (x1, y1 + height)
    right = (x2, y1 + height)
    return (top, left, right)

def calculateRightTriangle(x1, y1, x2, y2) :
    top = (x1, y1)
    bottom = (x1, y2)
    right = (x2, y2)
    return (top, bottom, right)

def drawChooseColors(colorRect, top, left) :
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(left, top, 50, 50)
    pygame.draw.rect(screen, colorRect, rect)
    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
        global color, colorChooseRect, brushcolor
        color = brushcolor = colorRect
        colorChooseRect.center = rect.center

def drawChooseButtons(image, tool, left, top) :
    global state, buttonChooseRect
    mouse = pygame.mouse.get_pos()
    rect = image.get_rect()
    rect.topleft = (left, top)
    screen.blit(image, (left, top))
    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        state = tool
        buttonChooseRect.center = rect.center

def drawBucket() :
    global bucket, width
    mouse = pygame.mouse.get_pos()
    rect = bucket.get_rect()
    rect.topleft = (1026, 290)
    screen.blit(bucket, (1026, 290))
    if rect.collidepoint(mouse) :
        return True

def drawChooseWidthCircles(left, top, local_width) :
    global circleChooseRect, width, brushWidth
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(0, 0, 40, 40)
    rect.center = (left, top)
    pygame.draw.rect(screen, (0, 0, 0), rect, local_width, 20)
    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] :
        if width != 0 :
            circleChooseRect.center = rect.center
            width = brushWidth = local_width

shift = False
alt = False

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


    #Checking if shift or alt pressed
    if event.type == pygame.KEYUP :
        if event.key == pygame.K_LSHIFT :
            shift = False
        if event.key == pygame.K_LALT :
            alt = False

    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_ESCAPE :
            running = False
        #Checking if shift or alt pressed
        if event.key == pygame.K_LSHIFT :
            shift = True
        if event.key == pygame.K_LALT :
            alt = True
        #Changing tools with keyboard
        if event.key == pygame.K_r :
            state = 'rectangle'
            buttonChooseRect.center = (1026 + 35, 170 + 35)
        if event.key == pygame.K_b :
            state = 'brush'
            buttonChooseRect.center = (1026 + 35, 30 + 35)
        if event.key == pygame.K_e and shift == False :
            state = 'eraser'
            buttonChooseRect.center = (1026 + 1 * 89 + 39, 30 + 35)
        if event.key == pygame.K_c :
            state = 'circle'
            buttonChooseRect.center = (1026 + 2 * 89 + 35, 170 + 35)
        if event.key == pygame.K_t :
            state = 'triangle'
            buttonChooseRect.center = (1026 + 3 * 89 + 35, 170 + 35)
        if event.key == pygame.K_v :
            state = 'romb'
            buttonChooseRect.center = (1026 + 1 * 89 + 35, 170 + 35)
        #Shift + e clear everything
        if event.key == pygame.K_e and shift :
            screen.blit(baseLayer, (0, 0))
            screen.fill(WHITE)
            baseLayer.blit(screen, (0, 0))
        #Shift + f fill with selected color
        if event.key == pygame.K_f and shift :
            screen.blit(baseLayer, (0, 0))
            screen.fill(color)
            baseLayer.blit(screen, (0, 0))

    #position of mouse
    mouse = pygame.mouse.get_pos()
    #Changing mouse accroding to position of mouse
    if toolsLayerRect.collidepoint(mouse) :
        paint = False
        pygame.mouse.set_cursor(pygame.cursors.arrow)
    else :
        paint = True
        pygame.mouse.set_cursor(pygame.cursors.broken_x)

    #Brush and eraser color handling
    if state == 'brush':
        brushcolor = color
    elif state == 'eraser':
        brushcolor = WHITE

    #Brush and eraser tool handling
    if state == 'brush' or state == 'eraser':
        if pygame.mouse.get_pressed()[0] and paint:
            screen.blit(baseLayer, (0, 0))
            currentX, currentY = pygame.mouse.get_pos()
            if prev is not None :
                prevX, prevY = prev
                for x in range(brushWidth) :
                    for y in range(brushWidth) :
                        pygame.draw.line(baseLayer, brushcolor, 
                        (prevX + x - brushWidth, prevY + y - brushWidth), 
                        (currentX + x - brushWidth, currentY + y - brushWidth))
            prev = (currentX, currentY)
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
            screen.blit(baseLayer, (0, 0))
    #Shape tools handling
    else:
        #Getting starting and ending positions of mouse press
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

        #Shape tools drawing
        if state == 'rectangle' and paint:  
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                #Draw rectangle, if shift is pressed draw square
                r = calculateRect(prevX, prevY, currentX, currentY) if shift == False else calculateSquare(prevX, prevY, currentX, currentY)
                pygame.draw.rect(screen, color, pygame.Rect(r), width)
        elif state == 'circle' and paint:
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                #Draw circle
                circle = calculateCircle(prevX, prevY, currentX, currentY)
                pygame.draw.circle(screen, color, circle[0], circle[1], width)
        elif state == 'romb' and paint:
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                #Draw rhombus, if shift is pressed draw right rhombus
                romb = calculateRomb(prevX, prevY, currentX, currentY) if shift == False else calculateRightRomb(prevX, prevY, currentX, currentY)
                pygame.draw.polygon(screen, color, romb, width)
        elif state == 'triangle' and paint:
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                #Draw just triangle
                if shift == False:
                    triangle = calculateTriangle(prevX, prevY, currentX, currentY)
                #Draw just equaterial triangle if shift is pressed
                elif shift == True and alt == False :
                    triangle = calculateEqualTriangle(prevX, prevY, currentX, currentY)
                #Draw just right triangle if shift and alt is pressed
                elif shift == True and alt == True :
                    triangle = calculateRightTriangle(prevX, prevY, currentX, currentY)
                pygame.draw.polygon(screen, color, triangle, width)

  #Bucket icon, fill or border
  if drawBucket() and event.type == pygame.MOUSEBUTTONDOWN :
        #Fill
        if width == 0 :
            width = 1
            bucket = pygame.image.load('images/paint/bucket_black.png')
            screen.blit(bucket, (1026, 290))
        #Border
        else :
            width = 0
            bucket = pygame.image.load('images/paint/bucket_blue.png')
            screen.blit(bucket, (1026, 290))
            circleChooseRect.center = (1420, 1020)

  #Blitting tools layer
  screen.blit(toolsLayer, ((WINDOW_WIDTH - 400), 0))
  #Tools choose blue rectangle
  pygame.draw.rect(screen, (173, 206, 255), buttonChooseRect)
  #drawing tools
  for i in range(2) :
      for j in range(4) :
        if i == 0 and j <= 1 :
            drawChooseButtons(buttons[j], tools[j], 1026 + j * 89, 30)
        elif i == 0 and j > 1 :
            pass
        else :
            drawChooseButtons(buttons[2 + j], tools[2 + j], 1026 + j * 89, 170)

  #Color choose blue rectangle
  pygame.draw.rect(screen, (173, 206, 255), colorChooseRect)
  #drawing colors
  for i in range(2) :
      for j in range(6) :
          choose_color = colors[j] if i == 0 else colors[6 + j]
          drawChooseColors(choose_color, 530 + i * 60, 1026 + j * 60)

  #bucket icon
  drawBucket()
  #width choose circles
  for i in range(4) :
      drawChooseWidthCircles(1150 + (i * 50), 323, i * 4 + 1)

  #width choose circles blue circle
  pygame.draw.rect(screen, (0, 102, 255), circleChooseRect, width, 20)
  pygame.display.flip()


  clock.tick(60)

pygame.quit()