import pygame

# Initialize all configs
pygame.init()

# Creating main window (Surface)
screen = pygame.display.set_mode((500, 500))  # Surface
running = True

# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
# Frame per second
FPS = 60
color = RED

x = 25
y = 25

# Main loop
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Getting all pressed buttons
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if y > 25 :
            y -= 20
    if pressed[pygame.K_DOWN]:
        if y < 475 :
            y += 20
    if pressed[pygame.K_LEFT]:
        if x > 25 :
            x -= 20
    if pressed[pygame.K_RIGHT]:
        if x < 475 :
            x += 20

    # Refresh the screen
    screen.fill(WHITE)
    pygame.draw.circle(screen, color, (x, y), 25)

    # Screen updating
    pygame.display.flip()

    clock.tick(FPS)