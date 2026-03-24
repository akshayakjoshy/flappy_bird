import pygame
from pygame.locals import *
import cflap
from cflap import Bird, Pipe, Game


pygame.init()
screen_width=360
screen_height=640
ans="k"
games1=0
 # code....  changed ....x
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("flappy Bird 2")
clock=pygame.time.Clock()
SCORE_COLOR = (255, 255, 255)   # White score text
GAME_OVER_RED = (200, 0, 0)     # Game over text
PIPE_GREEN = (0, 200, 0)        # Pipes
SKY_BLUE = (135, 206, 235)      # Background sky
GAME_OVER_COLOR = (235, 162, 89)

test_font2=pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/BotsmaticRegularDemo.ttf',40)
text_font=pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/FlappyBirdRegular-9Pq0.ttf',40)
start_button=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/start2.png")
current_screen='start' 

# Load option buttons globally
option1=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/option button copy.png")
option2=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/option button copy.png")
option3=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/option button copy.png")

# Load character selection assets once
screen2=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/flappy bird wallpaper.jpeg")
character1=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character1.png")
character2=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character2.png")
character3=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character3.png")

option_font1 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/ByteBounce copy.ttf',25)
option_font2 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/ByteBounce copy.ttf',25)
option_font3 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/ByteBounce copy.ttf',25)
textoption1 = option_font1.render('RIZZ GAWDD', True, 'black')
textoption2 = option_font2.render('SHAWARMAA', True, 'black')
textoption3 = option_font3.render('MADHAVV', True, 'black')


#load images
bg=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/flappy bird wallpaper.jpeg")
#charca


def draw_text_outline(font, text, text_color, outline_color, center_x, center_y):
    text_surface = font.render(text, True, text_color)
    outline_surface = font.render(text, True, outline_color)

    x = center_x - text_surface.get_width() // 2
    y = center_y - text_surface.get_height() // 2

    # draw outline
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        screen.blit(outline_surface, (x + dx, y + dy))

    # draw main text
    screen.blit(text_surface, (x, y))

def draw():
    screen.blit(bg,(0,0))
    screen.blit(start_button,(105,290))
    draw_text_outline(
        test_font2,
        'FLAPPY BIRD ',
        PIPE_GREEN,
        (0, 0, 0),
        180,
        180
    )

def gamestart():
    
    game_font=pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/FlappyBirdRegular-9Pq0.ttf',40)
    screen3=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/flappy bird wallpaper.jpeg")
    screen.blit(screen3,(0,0))
   
    
# Screen 2: choose character
def chose_character():
    screen.blit(screen2,(0,0))
    

    screen.blit(option1,(50,200))
    screen.blit(character1,(229,237))
    screen.blit(textoption1,(100,260))

    screen.blit(option2,(50,260))
    screen.blit(character2,(229,305))
    screen.blit(textoption2,(100,320))   

    screen.blit(option3,(50,320))  
    screen.blit(character3,(229,360))
    screen.blit(textoption3,(100,380))

    draw_text_outline(
        text_font,
        'CHOOSE YOUR CHARACTER',
        SCORE_COLOR,
        (0, 0, 0),
        180,
        180
    )

mouse_pos = (0, 0)

def score():
    screen.fill(SKY_BLUE)

    bg_img = pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/flappy bird wallpaper.jpeg")
    screen.blit(bg_img,(0,0))
    #-----for transpenrent layer-----
    dark_layer = pygame.Surface((360,640))  # same size as screen
    dark_layer.set_alpha(120)               # transparency (0–255)
    dark_layer.fill((0,0,0))                # black color

    screen.blit(dark_layer,(0,0))

    score_font = pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/Ithaca-LVB75.ttf', 30)
    game_over_font = pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/FlappyBirdRegular-9Pq0.ttf', 60)

    # GAME OVER title
    draw_text_outline(
        game_over_font,
        'GAME OVER',
        GAME_OVER_COLOR,
        (0,0,0),
        180,
        120
    )

    # character
    if ans == 'a':
        char = pygame.transform.scale(character1,(90,90))
    elif ans == 'b':
        char = pygame.transform.scale(character2,(90,90))
    elif ans == 'c':
        char = pygame.transform.scale(character3,(90,90))

    char_rect = char.get_rect(center=(180,210))
    screen.blit(char,char_rect)

    # score text
    score_text = score_font.render(f'Score: {game.score}', True, 'white')
    score_rect = score_text.get_rect(center=(180,320))
    screen.blit(score_text,score_rect)

    highscore_text = score_font.render(f'High Score: ', True, 'white')
    high_rect = highscore_text.get_rect(center=(180,360))
    screen.blit(highscore_text,high_rect)
    playagain_image = pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/playagain.png")
    screen.blit(playagain_image,(95,400))
    
        
# shrink the clickable area a little
option1_rect = pygame.Rect(60, 250, 230, 40)
option2_rect = pygame.Rect(60, 319, 230, 40)
option3_rect = pygame.Rect(60, 376, 230, 40)
playagain_rect = pygame.Rect(95, 400, 170, 50)
while True :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

        if current_screen == 'start':
            if 105 <= mouse_pos[0] <= 255 and 290 <= mouse_pos[1] <= 340:
                print('Start button clicked')
                current_screen = 'next'

        elif current_screen == 'next':
            if option1_rect.collidepoint(mouse_pos):
                ans, games1 = "a", 1
                print("Option A chosen - RIZZ GAWDD")
                current_screen = 'game'
                pygame.event.clear() 

            elif option2_rect.collidepoint(mouse_pos):
                ans, games1 = "b", 2
                print("Option B chosen - SHAWARMAA")
                current_screen = 'game'
                pygame.event.clear() 

            elif option3_rect.collidepoint(mouse_pos):
                ans, games1 = "c", 3
                print("Option C chosen - madhav")
                current_screen = 'game'
                pygame.event.clear()

        elif current_screen == 'over':
            if playagain_rect.collidepoint(mouse_pos):
                print('Play Again button clicked')
                current_screen = 'start'

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN: 
            if current_screen == 'start':
                current_screen = 'next'
                print('Enter key - moving to character selection')
        
        
    # Draw our elements based on current screen
    if current_screen == 'start':
        draw()            
    elif current_screen == 'next':
        chose_character()
    elif current_screen == 'game':
        char_map = {1: character1, 2: character2, 3: character3}
        game = Game(screen, clock, bg, char_map[games1])
        game.run()
        pygame.time.delay(500)
        pygame.event.clear()   # ← flush all buffered events
        current_screen = 'over'  # Reset to start after game ends
        #code to go back to the 1st screen after the game ends  
    elif current_screen == 'over':
        score()
    elif current_screen == 'playagain':
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 95 <= mouse_pos[0] <= 265 and 400 <= mouse_pos[1] <= 450:
                print('Play Again button clicked')
                draw()  # Go back to start screen
        
    pygame.display.update()
    clock.tick(60)
