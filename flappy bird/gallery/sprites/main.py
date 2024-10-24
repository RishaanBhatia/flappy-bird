import pygame 
import os
import time
from pygame import mixer
mixer.init()
pygame.init()

# Colors and other variables
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 240)
grey = (50, 50, 50)
clock = pygame.time.Clock()
 
# Game window 
screen_width = 900
screen_height = 607
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Caption
pygame.display.set_caption("Rishaan is great- DINO GAME")
pygame.display.update()

# Load images
track = pygame.image.load(os.path.join("Images and sounds", "Other", "Track.png"))
cloud1 = pygame.image.load(os.path.join("Images and sounds", "Other", "Cloud.png"))
cloud2 = pygame.image.load(os.path.join("Images and sounds", "Other", "Cloud.png"))
cloud3 = pygame.image.load(os.path.join("Images and sounds", "Other", "Cloud.png"))
reset = pygame.image.load(os.path.join("Images and sounds", "Other", "Reset.png"))
large_cactus1 = pygame.image.load(os.path.join("Images and sounds", "Cactus", "LargeCactus1.png"))
large_cactus2 = pygame.image.load(os.path.join("Images and sounds", "Cactus", "LargeCactus2.png"))
large_cactus3 = pygame.image.load(os.path.join("Images and sounds", "Cactus", "LargeCactus3.png"))
small_cactus1 = pygame.image.load(os.path.join("Images and sounds", "Cactus", "SmallCactus1.png"))
small_cactus2 = pygame.image.load(os.path.join("Images and sounds", "Cactus", "SmallCactus2.png"))
small_cactus3 = pygame.image.load(os.path.join("Images and sounds", "Cactus", "SmallCactus3.png"))
dino_dead = pygame.image.load(os.path.join("Images and sounds", "Dino", "DinoDead.png" ))
dino_run1 = pygame.image.load(os.path.join("Images and sounds", "Dino", "DinoRun1.png" ))
dino_run2 = pygame.image.load(os.path.join("Images and sounds", "Dino", "DinoRun2.png" ))
dino_start = pygame.image.load(os.path.join("Images and sounds", "Dino", "DinoStart.png" ))
final_dino_run1 = pygame.transform.scale(dino_run1, [63, 70])
final_dino_run2 = pygame.transform.scale(dino_run2, [63, 70])
final_dino_start = pygame.transform.scale(dino_start, [63, 70])
dino_dead = pygame.image.load(os.path.join("Images and sounds", "Dino", "DinoDead.png"))
final_dino_dead = pygame.transform.rotate(dino_dead, 90)
game_controls = pygame.image.load(os.path.join("Images and sounds", "Other", "GAME CONTROLS.png"))
dino_sound = pygame.mixer.Sound(os.path.join("Images and sounds", "Other", "dino_sound.mp3"))
hiscore_broken_sound = pygame.mixer.Sound(os.path.join("Images and sounds", "Other", "hiscore_broken_sound.mp3"))

# Display on screen
def text_screen(a, text, color, gameWindow, x, y):
    font = pygame.font.SysFont(None, a)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def control_screen():
    exit_game = False
    game_over = False
    while not exit_game:
        if game_over:
            pass
        else:
            gameWindow.fill(white)
            text_screen(70, "The controls:", grey, gameWindow, 100, 100)
            text_screen(55, "Right shift key: To start moving", grey, gameWindow, 100, 200)
            text_screen(55, "Up arrow key: To jump", grey, gameWindow, 100, 250)
            text_screen(55, "Press P key to play the game", grey, gameWindow, 200, 400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
            pygame.display.update()
    pygame.quit()
    quit()   



# Welcome screen 
def welcome():
    exit_game = False
    game_over = False
    while not exit_game:
        if game_over:
            pass
        else: 
            gameWindow.fill(blue)
            control_button_rect = pygame.draw.rect(gameWindow, red, [50, 60, game_controls.get_width(), game_controls.get_height()])
            gameWindow.blit(game_controls, [50, 60])
            text_screen(55, "RBIG", white, gameWindow, 390, 200)
            text_screen(55, "DINO GAME", white, gameWindow, 320, 300)
            text_screen(55, "Press SPACE BAR to play", red, gameWindow, 230, 400)

            
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

# Game loop 
def gameloop():
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            hiscore = f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    # Game specific variables
    exit_game = False
    game_over = False
    fps = 70

    track_velocity = 0
    track_x, track_y = 0, 500

    cloud_velocity = 0
    cloud1_x, cloud1_y = 50, 25
    cloud2_x, cloud2_y = 300, 30
    cloud3_x, cloud3_y = 700, 35
    large_cactus1_x, large_cactus1_y = 800, 420
    large_cactus2_x, large_cactus2_y = 1700, 420
    large_cactus3_x, large_cactus3_y = 2200, 420
    small_cactus1_x, small_cactus1_y = 2700, 450
    small_cactus2_x, small_cactus2_y = 3050, 450
    small_cactus3_x, small_cactus3_y = 3500, 450
    cactus_velocity = 0 
    dino_list = [final_dino_start, final_dino_run1, final_dino_run1, final_dino_run1, final_dino_run1, final_dino_run1, final_dino_run1, final_dino_run1, final_dino_run2, final_dino_run2, final_dino_run2, final_dino_run2, final_dino_run2, final_dino_run2, final_dino_run2]
    dino_index = 3
    dino_change_vel = 0
    dino_x, dino_y = 200, 445
    jump = False
    mascular_force = 25
    you_died_x = (screen_width//2) - ((dino_dead.get_width()/2) - 80)
    you_died_y = (screen_height//1.4) - (dino_dead.get_height()/2)
    score = 0
    key_pressed = pygame.key.get_pressed()
    the_score = pygame.USEREVENT + 1
    pygame.time.set_timer(the_score, 1000)

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(final_dino_dead, [(screen_width//2) - (dino_dead.get_width()/2), (screen_height//1.4) - (dino_dead.get_height()/2)])
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RSHIFT:
                        track_velocity = -6
                        cloud_velocity = -6
                        cactus_velocity = -6
                        dino_change_vel = 1
                    if event.key == pygame.K_UP:
                        jump = True
                        dino_sound.play(0)
                if event.type == the_score:
                    score += 1  
                    if score > int(hiscore):
                        hiscore = score
                    if score + 1 == int(hiscore):
                        hiscore_broken_sound.play(0)

                        
            dino_index = dino_index + dino_change_vel
            track_x = track_x + track_velocity
            cloud1_x = cloud1_x + cloud_velocity
            cloud2_x = cloud2_x + cloud_velocity
            cloud3_x = cloud3_x + cloud_velocity
            large_cactus1_x = large_cactus1_x + cactus_velocity
            large_cactus2_x = large_cactus2_x + cactus_velocity
            large_cactus3_x = large_cactus3_x + cactus_velocity
            small_cactus1_x = small_cactus1_x + cactus_velocity
            small_cactus2_x = small_cactus2_x + cactus_velocity
            small_cactus3_x = small_cactus3_x + cactus_velocity
            
            if track_x == -600:
                track_x = 0
            
            if cloud1_x + cloud1.get_width() < 0:
                cloud1_x = screen_width + 73.733
            if cloud2_x + cloud2.get_width() < 0:
                cloud2_x = screen_width + 377.737
            if cloud3_x + cloud3.get_width() < 0:
                cloud3_x = screen_width + 843.86677

            if large_cactus1_x + large_cactus1.get_width() < 0:
                large_cactus1_x = 4211
            if large_cactus2_x + large_cactus2.get_width() < 0:
                large_cactus2_x = 5333
            if large_cactus3_x + large_cactus3.get_width() < 0:
                large_cactus3_x = 6071
            if small_cactus1_x + small_cactus1.get_width() < 0:
                small_cactus1_x = 6783
            if small_cactus2_x + small_cactus2.get_width() < 0:
                small_cactus2_x = 7167
            if small_cactus3_x + small_cactus3.get_width() < 0:
                small_cactus3_x = 7800

            if dino_index == 15:
                dino_index = 3
            
            if jump:
                dino_y -= mascular_force 
                mascular_force -= 1 
                if mascular_force < -25:
                    jump = False
                    mascular_force = 25


            # Drawing on the screen  
            gameWindow.fill((white))
            gameWindow.blit(track, [track_x, track_y])
            gameWindow.blit(cloud1, [cloud1_x, cloud1_y])
            gameWindow.blit(cloud2, [cloud2_x, cloud2_y])
            gameWindow.blit(cloud3, [cloud3_x, cloud3_y])
            gameWindow.blit(large_cactus1, [large_cactus1_x, large_cactus1_y])
            gameWindow.blit(large_cactus2, [large_cactus2_x, large_cactus2_y])
            gameWindow.blit(large_cactus3, [large_cactus3_x, large_cactus3_y])
            gameWindow.blit(small_cactus1, [small_cactus1_x, small_cactus1_y])
            gameWindow.blit(small_cactus2, [small_cactus2_x, small_cactus2_y])
            gameWindow.blit(small_cactus3, [small_cactus3_x, small_cactus3_y])
            gameWindow.blit(dino_list[dino_index], [dino_x, dino_y])
            large_cactus1_rect = pygame.Rect(large_cactus1_x, large_cactus1_y, large_cactus1.get_width(), large_cactus1.get_height())
            large_cactus2_rect = pygame.Rect(large_cactus2_x, large_cactus2_y, large_cactus2.get_width(), large_cactus2.get_height())
            large_cactus3_rect = pygame.Rect(large_cactus3_x, large_cactus3_y, large_cactus3.get_width(), large_cactus3.get_height())
            small_cactus1_rect = pygame.Rect(small_cactus1_x, small_cactus1_y, small_cactus1.get_width(), small_cactus1.get_height())
            small_cactus2_rect = pygame.Rect(small_cactus2_x, small_cactus2_y, small_cactus2.get_width(), small_cactus2.get_height())
            small_cactus3_rect = pygame.Rect(small_cactus3_x, small_cactus3_y, small_cactus3.get_width(), small_cactus3.get_height())
            dino_rect = pygame.Rect(dino_x, dino_y, final_dino_run1.get_width(), final_dino_run1.get_height())
        
            # Handling collisions
            if dino_rect.colliderect(large_cactus1_rect):
                game_over = True
            if dino_rect.colliderect(large_cactus2_rect): 
                game_over = True
            if dino_rect.colliderect(large_cactus3_rect): 
                game_over = True
            if dino_rect.colliderect(small_cactus1_rect): 
                game_over = True
            if dino_rect.colliderect(small_cactus2_rect): 
                game_over = True
            if dino_rect.colliderect(small_cactus3_rect): 
                game_over = True

            text_screen(55, "The score: " + str(score), red, gameWindow, 50, 20)
            text_screen(55, "Hiscore: " + str(hiscore), blue, gameWindow, 300, 20)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
gameloop()