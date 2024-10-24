import pygame
pygame.init()
from pygame import mixer
mixer.init()
import os

game_controls = pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\GAME CONTROLS.png")

def baseBlit(gameWindow, base, base_x, base_y):
    gameWindow.blit(base, [base_x, base_y])
    gameWindow.blit(base, [base_x + 900, base_y])

def control_screen():
    exit_game = False  
    game_over = False
    while not exit_game:
        if game_over:
            pass
        else:
            gameWindow.fill(white)
            text_screen(70, "The controls:", red, gameWindow, 100, 100)
            text_screen(55, "Space bar: To start moving", red, gameWindow, 100, 200)
            text_screen(55, "Up arrow key: To move up", red, gameWindow, 100, 250)
            text_screen(55, "Press P key to play the game", red, gameWindow, 200, 400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
            pygame.display.update()
    pygame.quit()
    quit()

# Variables
clock = pygame.time.Clock()
red = (255, 0, 0)
white = (255, 255, 255)

# Game window
screen_width, screen_height = 900, 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background, base and pipes
background = pygame.transform.scale(pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\background-day.png"), [screen_width, screen_height])
base = pygame.transform.scale(pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\base.png"), [screen_width, 50])
pipe_not_final = pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\pipe-green.png")
pipe = pygame.transform.scale(pipe_not_final, [pipe_not_final.get_width(), pipe_not_final.get_height() - 65])
pipe_red_not_final = pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\pipe-red.png")
pipe_red = pygame.transform.scale(pipe_red_not_final, [pipe_not_final.get_width(), pipe_not_final.get_height() - 75])


# Red bird upflap
red_bird_upflap_not_final = pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\redbird-upflap.png")
bird_width, bird_height = red_bird_upflap_not_final.get_width() + 25, red_bird_upflap_not_final.get_height() + 25
red_bird_upflap = pygame.transform.scale(red_bird_upflap_not_final, [bird_width, bird_height])

# Red bird midflap
red_bird_midflap_not_final = pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\redbird-midflap.png")
red_bird_midflap = pygame.transform.scale(red_bird_midflap_not_final, [bird_width, bird_height])
 

# Red bird downflap
red_bird_downflap_not_final = pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\redbird-downflap.png")
red_bird_downflap = pygame.transform.scale(red_bird_downflap_not_final, [bird_width, bird_height])

# Sound-
hiscore_broken_sound = pygame.mixer.Sound(r"D:\PYTHON\Pygame\flappy bird\audio\point.ogg")
hit_sound = pygame.mixer.Sound(r"D:\PYTHON\Pygame\flappy bird\audio\hit.wav")
wing_sound = pygame.mixer.Sound(r"D:\PYTHON\Pygame\flappy bird\audio\wing.wav")
point_sound = pygame.mixer.Sound(r"D:\PYTHON\Pygame\flappy bird\gallery\audio\point.wav")
night_back = pygame.transform.scale(pygame.image.load(r"D:\PYTHON\Pygame\flappy bird\sprites\background-night.png"), [screen_width, screen_height])

# Welcome screen 
def welcome():
    exit_game = False
    game_over = False
    while not exit_game:
        if game_over:
            pass
        else: 
            gameWindow.blit(background, [0, 0])
            red_bird_in_wel =  pygame.transform.scale(red_bird_upflap_not_final, [red_bird_upflap.get_width() + 50, red_bird_upflap.get_height() + 50])
            gameWindow.blit(red_bird_in_wel, [400, 350])

            control_button_rect = pygame.draw.rect(gameWindow, red, [50, 60, game_controls.get_width(), game_controls.get_height()])
            gameWindow.blit(game_controls, [50, 60])
            text_screen(55, "RBIG", red, gameWindow, screen_width//2 - 50, 80)
            text_screen(55, "FLAPPY BIRD GAME", red, gameWindow, 270, 200)
            text_screen(55, "Press SPACE BAR to play", red, gameWindow, 230, 270)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if control_button_rect.collidepoint(pos):
                        control_screen()

        pygame.display.update()
    pygame.quit()
    quit()

def text_screen(a, text, color, gameWindow, x, y):
    font = pygame.font.SysFont(None, a)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# game loop
def gameloop():
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            hiscore = f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    # Game specific variables
    exit_game = False
    game_over = False
    fps = 60
    pipe_vel = 0
    init_vel = 7
    pipe1_x, pipe1_y = 800, 0
    pipe2_x, pipe2_y = 1000, screen_height - pipe.get_height()
    pipe3_x, pipe3_y = 1278, 0
    pipe4_x, pipe4_y = 1568, screen_height - pipe.get_height()
    pipe5_x, pipe5_y = 1900, screen_height - pipe.get_height()
    bird_x, bird_y = 50, 300
    bird_vel = 0
    base_vel = 0
    base_init_vel = 7
    base_x, base_y = 0, screen_height - base.get_height()
    gravity = 0
    bird_movement = 0
    red_bird_list = [red_bird_upflap, red_bird_upflap, red_bird_upflap, red_bird_upflap, red_bird_upflap, red_bird_midflap, red_bird_midflap, red_bird_midflap, red_bird_midflap , red_bird_midflap, red_bird_downflap, red_bird_downflap, red_bird_downflap, red_bird_downflap, red_bird_downflap]
    red_bird_list_index = 0
    red_bird_index_change = 0
    game_over = False
    you_died_x, you_died_y = 350, 400
    name = input("Enter your name: ")
    the_score = pygame.USEREVENT + 1
    pygame.time.set_timer(the_score, 1000)
    score = 0
    back_index = 0
    back_list = [background, night_back]
    pipe_list = [pipe, pipe_red]
    pipe_index = 0

    # Caption
    pygame.display.set_caption(f"{name}'s flappy bird game")
    print(f"Hi {name}! All the best!!")
    pygame.display.update()


    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
        if game_over:
            gameWindow.blit(background, [0, 0])
            text_screen(55, "GAME OVER! PRESS ENTER TO PLAY AGAIN", red, gameWindow, 50, 200)
            text_screen(55, "YOU LOST", red, gameWindow, you_died_x, you_died_y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == the_score:
                    score += 1  
                    point_sound.play(0)
                    
                    if score > int(hiscore):
                        hiscore = score
                    if score + 1 == int(hiscore):
                        hiscore_broken_sound.play(0)
                    if score >= 10:
                        back_index = 1
                        pipe_index = 1
                    if score >= 60:
                        back_index = 0
                        pipe_index = 0
                    if score >= 100:
                        back_index = 1
                        pipe_index = 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pipe_vel = -init_vel
                        base_vel = -base_init_vel
                        gravity = 0.25
                        red_bird_index_change = 1
                        
                    if event.key == pygame.K_UP:
                        gravity = 0.25
                        bird_movement = 0
                        bird_movement -= 8
                        wing_sound.play(0)  
                                       
            red_bird_list_index = red_bird_list_index + red_bird_index_change
            bird_movement += gravity 
            bird_y = bird_y + bird_movement
            base_x = base_x + base_vel
            pipe1_x = pipe1_x  + pipe_vel
            pipe2_x = pipe2_x + pipe_vel
            pipe3_x = pipe3_x + pipe_vel
            pipe4_x = pipe4_x + pipe_vel
            pipe5_x = pipe5_x + pipe_vel

            if pipe1_x + pipe.get_width() < 0:
                pipe1_x = 2100
            if pipe2_x + pipe.get_width() < 0:
                pipe2_x = 2200
            if pipe3_x + pipe.get_width() < 0:
                pipe3_x = 2600
            if pipe4_x + pipe.get_width() < 0:
                pipe4_x = 2900
            if pipe5_x + pipe.get_width() < 0:
                pipe5_x = 3100

            if base_x <= -900:
                base_x = 0
            if red_bird_list_index >= 15:
                red_bird_list_index = 0
            if score >= 15 and score < 30:
                pipe_vel = -14
                base_vel = -14
                


            pipe1_rect = pygame.Rect(pipe1_x, pipe1_y, pipe.get_width(), pipe.get_height())
            pipe2_rect = pygame.Rect(pipe2_x, pipe2_y, pipe.get_width(), pipe.get_height())
            pipe3_rect = pygame.Rect(pipe3_x, pipe3_y, pipe.get_width(), pipe.get_height())
            pipe4_rect = pygame.Rect(pipe4_x, pipe4_y, pipe.get_width(), pipe.get_height())
            pipe5_rect = pygame.Rect(pipe5_x, pipe5_y, pipe.get_width(), pipe.get_height())
            bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
                    

            if name == "Riggi" or name == "riggi" or (score >= 15 and score < 30):
                if bird_y >= base_y:
                    game_over = False
                    
                if bird_y <= 0:
                    game_over = False
                    
                if bird_rect.colliderect(pipe1_rect):
                    game_over = False
                    
                if bird_rect.colliderect(pipe2_rect): 
                    game_over = False
                    
                if bird_rect.colliderect(pipe3_rect): 
                    game_over = False
                    
                if bird_rect.colliderect(pipe4_rect): 
                    game_over = False
                    
                if bird_rect.colliderect(pipe5_rect): 
                    game_over = False
        
                    
            else:
                if bird_y >= base_y:
                    hit_sound.play(0)
                    game_over = True 
                if bird_y <= 0:
                    hit_sound.play(0)
                    game_over = True 
                if bird_rect.colliderect(pipe1_rect):
                    hit_sound.play(0)
                    game_over = True
                if bird_rect.colliderect(pipe2_rect): 
                    hit_sound.play(0)
                    game_over = True
                if bird_rect.colliderect(pipe3_rect): 
                    hit_sound.play(0)
                    game_over = True
                if bird_rect.colliderect(pipe4_rect): 
                    hit_sound.play(0)
                    game_over = True
                if bird_rect.colliderect(pipe5_rect): 
                    hit_sound.play(0)
                    game_over = True
                if name == "YBIG" or name == "YB":
                    print("Invald name!!!\nThere is only one great person on Earth i.e @Rishaan Bhatia(RBIG)\nDo not copy him...")
                    game_over = True
        
            gameWindow.blit(back_list[back_index], [0, 0])
            gameWindow.blit(pipe_list[pipe_index], [pipe1_x, pipe1_y])
            gameWindow.blit(pipe_list[pipe_index], [pipe2_x, pipe2_y])
            gameWindow.blit(pipe_list[pipe_index], [pipe3_x, pipe3_y])
            gameWindow.blit(pipe_list[pipe_index], [pipe4_x, pipe4_y])
            gameWindow.blit(pipe_list[pipe_index], [pipe5_x, pipe5_y])
            gameWindow.blit(red_bird_list[red_bird_list_index], [bird_x, bird_y]) 
            baseBlit(gameWindow, base, base_x, base_y)

            text_screen(55, "The score: " + str(score), red, gameWindow, 50, 20)
            text_screen(55, "Hiscore: " + str(hiscore), white, gameWindow, 400, 20)

            if score >= 15 and score < 25:
                text_screen(40, "POWER BOOST!!!", red, gameWindow, 350, 70)

            if name == "Riggi" or name == "riggi":
                text_screen(55, "Nobody can defeat my father!!: ", red, gameWindow, 200, 120)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
gameloop()