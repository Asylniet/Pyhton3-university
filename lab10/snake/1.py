import pygame
import connection as cn
import classes as cs
import params as ps

#Setting up fonts
font = pygame.font.SysFont("Courier New", 20)
big_font = pygame.font.SysFont("Courier New", 30)

#Setting up Sounds
food_sound = pygame.mixer.Sound('sound/eat.mp3')
pygame.mixer.music.load('sound/super_mario.mp3')
game_over_theme_sound = pygame.mixer.Sound('sound/game_over_theme.mp3')
pygame.mixer.music.play(-1)

running = True
state = 'main menu'

snake = cs.Snake(0, 0)
food = cs.Food()

d = 5

#Loading images for buttons
main_menu_bg_load = pygame.image.load('images/main_menu_snake.jpg')
main_menu_bg = cs.Button(main_menu_bg_load, 0, 0)
main_menu_play_load = pygame.image.load('images/play_button_snake.png')
main_menu_play = cs.Button(main_menu_play_load, (ps.screen_width - main_menu_play_load.get_width()) / 2, 300)
main_menu_quit_load = pygame.image.load('images/quit_button_snake.png')
main_menu_quit = cs.Button(main_menu_quit_load, (ps.screen_width - main_menu_quit_load.get_width()) / 2, 400)
main_menu_restart_load = pygame.image.load('images/restart_button_snake.png')
main_menu_restart = cs.Button(main_menu_restart_load, (ps.screen_width - main_menu_restart_load.get_width()) / 2, 300)

clock = pygame.time.Clock()


#Game over function
def game_over() :
    global state
    state = 'game over'
    game_over_theme_sound.play()
    if snake.size > cn.user_data[2] :
        sql = f'''
            update users
            set score = {snake.size}
            where name = \'{cn.user}\'
        '''
        cn.cursor.execute(sql)
        cn.conn.commit()

while running:
    #FPS depending on speed
    clock.tick(cs.SPEED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ps.TIMER :
            ps.ghost = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state = 'pause' if state == 'play' else 'play'
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

        if event.type == pygame.MOUSEBUTTONDOWN and main_menu_play.draw() and state != 'game over':
            state = 'play'
            pygame.time.set_timer(ps.TIMER, 2000)
        if event.type == pygame.MOUSEBUTTONDOWN and main_menu_quit.draw():
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and main_menu_restart.draw() and state == 'game over':
            ps.ghost = True
            pygame.time.set_timer(ps.TIMER, 0)
            pygame.time.set_timer(ps.TIMER, 2000)
            #Reseting all the progress
            ps.screen.fill((0, 0, 0))
            state = 'play'
            #Snake reset
            snake.size = 0
            snake.count = 0
            snake.elements.clear()
            snake.elements.append([0, 0])
            snake.dx = d
            snake.dy = 0

    if state == 'main menu' :
        welcome = big_font.render(f"Welcome, {cn.user_data[1]}", True, (255, 255, 255))
        best_scoore_text = big_font.render(f"Best score: {cn.user_data[2]}", True, (255, 255, 255))
        #Buttons for starter main menu
        main_menu_bg.draw()
        main_menu_play.draw()
        main_menu_quit.draw()
        ps.screen.blit(welcome, ((ps.screen_width - welcome.get_width()) / 2, 20))
        ps.screen.blit(best_scoore_text, ((ps.screen_width - best_scoore_text.get_width()) / 2, 60))
    elif state == 'play' :
        pygame.mixer.music.unpause()
        ps.screen.fill((255, 255, 255))
        #Reaching the borders
        if snake.elements[0][0] > ps.screen_width :
            snake.elements[0][0] = 0
        if snake.elements[0][0] < 0 :
            snake.elements[0][0] = ps.screen_width
        if snake.elements[0][1] > ps.screen_height :
            snake.elements[0][1] = 0
        if snake.elements[0][1] < 0 :
            snake.elements[0][1] = ps.screen_height

        #Eating food
        if snake.eat(food.x, food.y, food.w):
            food_sound.play()
            snake.add_to_snake(food.color)
            food.gen()

        #If food appears on top of snake, it generates new food
        if snake.food(food.x, food.y, food.w) :
            food.gen()

        snake.move()
        if snake.move() :
            game_over()

        food.draw()
        #Drawing walls
        for object in ps.all_sprites :
            object.draw()
            
            #Check if snake collides with walls
            if snake.wall(object.rect.x, object.rect.y, object.rect.width, object.rect.height) and ps.ghost == False :
                game_over()

            #Checking if food appears on top of walls
            if object.rect.colliderect((food.x, food.y, food.w, food.w)):
                food.gen()


        #Timer for red food
        if food.color == ps.RED :
            if food.w >= 0:
                food.w -= 0.1
            if food.w < 0 :
                food.gen()

        snake.draw()
        #Score and level text
        score = font.render(str(snake.size), True, (0, 0, 0))
        lvl = font.render(f"lvl: {str(snake.level)}", True, (0, 0, 0))
        ps.screen.blit(score, (ps.screen_width - score.get_width() - 10, 10))
        ps.screen.blit(lvl, (ps.screen_width - lvl.get_width() - 10, 30))

    elif state == 'pause' :
        pygame.mixer.music.pause()
        pause_text = big_font.render("Your game on pause", True, (255, 255, 255))
        score_text = big_font.render(f"Your current score: {snake.size}", True, (255, 255, 255))
        main_menu_bg.draw()
        main_menu_play.draw()
        main_menu_quit.draw()
        ps.screen.blit(pause_text, ((ps.screen_width - pause_text.get_width()) / 2, 20))
        ps.screen.blit(score_text, ((ps.screen_width - score_text.get_width()) / 2, 60))
        if snake.size > cn.user_data[2] :
            new_record = big_font.render("New record was saved!", True, (255, 255, 255))
            ps.screen.blit(new_record, ((ps.screen_width - new_record.get_width()) / 2, 100))
            sql = f'''
                update users
                set score = {snake.size}
                where name = \'{cn.user}\'
            '''
            cn.cursor.execute(sql)
            cn.conn.commit()
            cs.updateLevel()
        else :
            best_score_text = big_font.render(f"Your best score: {cn.user_data[2]}", True, (255, 255, 255))
            ps.screen.blit(best_score_text, ((ps.screen_width - best_score_text.get_width()) / 2, 100))
    elif state == 'game over' :
        game_over_text = big_font.render("Game over", True, (255, 255, 255))
        score_text = big_font.render(f"Your score: {snake.size}", True, (255, 255, 255))
        #game over menu
        main_menu_bg.draw()
        main_menu_restart.draw()
        main_menu_quit.draw()
        ps.screen.blit(game_over_text, ((ps.screen_width - game_over_text.get_width()) / 2, 20))
        ps.screen.blit(score_text, ((ps.screen_width - score_text.get_width()) / 2, 60))
        if snake.size > cn.user_data[2] :
            new_record = big_font.render("New record!", True, (255, 255, 255))
            ps.screen.blit(new_record, ((ps.screen_width - new_record.get_width()) / 2, 100))

    pygame.display.flip()

pygame.quit()

cn.cursor.close()
cn.conn.close()