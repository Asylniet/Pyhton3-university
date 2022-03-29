import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True

music_playing = True
current = 0
music = ['music/first.mp3', 'music/second.mp3', 'music/third.mp3']
print(len(music))
pygame.mixer.music.load(music[current])
pygame.mixer.music.play()

def next_song() :
    global current
    if current == len(music) - 1 :
        current = 0
        pygame.mixer.music.load(music[current])
        pygame.mixer.music.play()
    elif current < len(music) :
        current += 1
        pygame.mixer.music.load(music[current])
        pygame.mixer.music.play()
    
def previous_song() :
    global current
    if current == 0 :
        current = len(music) - 1
        pygame.mixer.music.load(music[current])
        pygame.mixer.music.play()
    else :
        current -= 1
        pygame.mixer.music.load(music[current])
        pygame.mixer.music.play()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60
color = BLUE

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing == True :
                    pygame.mixer.music.stop()
                    music_playing = False
                else :
                    pygame.mixer.music.play()
                    music_playing = True
            if event.key == pygame.K_RIGHT :
                next_song()
            if event.key == pygame.K_LEFT :
                previous_song()
            
        if event.type == SONG_END:
            next_song()
        
    # Refresh the screen
    screen.fill(WHITE)

    

    # Screen updating
    pygame.display.flip()

    clock.tick(FPS)