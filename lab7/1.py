import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True

center = screen.get_rect().center

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60

def clock_loader(path, angle) :
    image = pygame.image.load(path)
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    print(box)
    box_rotate = [p.rotate(angle) for p in box]
    print(box_rotate)

    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    origin = (center[0] + min_box[0], center[1] - max_box[1])

    rotated_image = pygame.transform.rotate(image, angle)
    screen.blit(rotated_image, origin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(WHITE)

    angle_minutes = datetime.now().minute * 6 + 180
    angle_seconds = datetime.now().second * 6 + 180
    clock_loader('images/minutes.png', -angle_minutes)
    clock_loader('images/seconds.png', -angle_seconds)

    clock_frame = pygame.image.load('images/clock.png')
    cw, ch = clock_frame.get_size()
    screen.blit(clock_frame, (center[0] - cw / 2, center[1] - ch / 2))

    # Screen updating
    pygame.display.flip()

    clock.tick(FPS)