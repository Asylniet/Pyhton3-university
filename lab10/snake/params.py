import pygame
import classes as cs
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Snake")

BLUE = (56, 159, 217)
GREEN = (34, 173, 48)
RED = (255, 0, 0)
#Food type depending on randomly chosen color
colors = (RED, GREEN, BLUE, GREEN, GREEN)

#Sprites for walls
all_sprites = pygame.sprite.Group()

ghost = True

TIMER = pygame.USEREVENT + 1 