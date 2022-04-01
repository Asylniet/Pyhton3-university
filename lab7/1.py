import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((500, 500))


def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


seconds = pygame.image.load('images/big.png')
minutes = pygame.image.load('images/small.png')
seconds = pygame.transform.scale(seconds, (50, 100))
minutes = pygame.transform.scale(minutes, (30, 60))

bg = pygame.image.load('images/mickey-clock.jpg')
w, h = seconds.get_size()

done = False
while not done:
    angle = datetime.now().second * 6
    min = datetime.now().minute * 6
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width() / 2, screen.get_height() / 2)
    screen.blit(bg, (0, 0))
    blitRotate(screen, seconds, pos, (w / 2 - 8, h / 2 + 45), angle)
    blitRotate(screen, minutes, pos, (w / 2 - 15, h / 2 + 10), min)

    # pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()
