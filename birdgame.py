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


# Load character selection assets once
screen2=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/flappy bird wallpaper.jpeg")
character1=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character1.png")
character2=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character2.png")
character3=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character3.png")
character4=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character4.png")
character5=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character5.png")
character6=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character6.png")
character7=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/character7.png")
option_font1 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/flappy_bird/ByteBounce copy.ttf',25)

textoption1 = option_font1.render('RIZZ GAWDD', True, 'black')
textoption2 = option_font1.render('SHAWARMAA', True, 'black')
textoption3 = option_font1.render('MADHAVV', True, 'black')
textoption4= option_font1.render('ROHITH', True, 'black')
textoption5= option_font1.render('SRIDEV', True, 'black')
textoption6= option_font1.render('PATRIC', True, 'black')
textoption7= option_font1.render('ARJOOONN', True, 'black')

#next button
nextbutton=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/next.png")
nextbuttonl=pygame.image.load("/Users/mikmin/Desktop/birdgame/flappy_bird/nextl.png")

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

    screen.blit(option1,(50,280))
    screen.blit(character2,(229,330))
    screen.blit(textoption2,(100,340))   

    screen.blit(option1,(50,350))  
    screen.blit(character3,(229,390))
    screen.blit(textoption3,(100,410))

    screen.blit(option1,(50,430))
    screen.blit(character4,(229,470))
    screen.blit(textoption4,(105,490))
    
    screen.blit(option1,(50,120))
    screen.blit(textoption5,(105,180))
    screen.blit(character5,(229,170))
    #next button
    screen.blit(nextbutton,(300,570))

    # Draw rectangles to show clickable areas
    
   # pygame.draw.rect(screen, (255, 0, 0), option1_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), option2_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), option3_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), option4_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), option5_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), next_rect, 3)
    
    

    draw_text_outline(
        text_font,
        'CHOOSE YOUR CHARACTER',
        SCORE_COLOR,
        (0, 0, 0),
        180,
        100
    )

mouse_pos = (0, 0)
def nextpg():
    screen.fill(SKY_BLUE)
    screen.blit(screen2,(0,0))
    draw_text_outline(
        text_font,
        'CHOOSE YOUR CHARACTER',
        SCORE_COLOR,
        (0, 0, 0),
        180,
        100
    )
    screen.blit(option1,(50,120))
    screen.blit(character6,(229,145))
    screen.blit(textoption6,(100,180))

    screen.blit(option1,(50,200))
    screen.blit(character7,(229,245))
    screen.blit(textoption7,(100,260)) 

    screen.blit(option1,(50,280))  
    #screen.blit(character3,(229,390))
    #screen.blit(textoption3,(100,410))

    screen.blit(option1,(50,350))  
    #screen.blit(character3,(229,390))
    #screen.blit(textoption3,(100,410))

    screen.blit(option1,(50,430))
    #screen.blit(character4,(229,470))
    #screen.blit(textoption4,(105,490))
    
    

    #next button
    #screen.blit(nextbutton,(300,570))
    screen.blit(nextbuttonl,(10,570))

    #pygame.draw.rect(screen, (255, 0, 0), next_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), nextl_rect, 3)
    #pygame.draw.rect(screen, (255, 0, 0), option6_rect, 3)

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
    elif ans == 'd':
        char = pygame.transform.scale(character4,(90,90))
    elif ans == 'e':
        char = pygame.transform.scale(character5,(70,70))
    elif ans == 'f':
        char = pygame.transform.scale(character6,(130,130))

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
option1_rect = pygame.Rect(70, 250, 216, 40)
option2_rect = pygame.Rect(70, 335, 216, 40)
option3_rect = pygame.Rect(70, 400, 216, 40)
option4_rect = pygame.Rect(70, 480, 216, 40)
option5_rect = pygame.Rect(70, 170, 216, 40)
option6_rect = pygame.Rect(70, 170, 216, 40)
next_rect = pygame.Rect(300, 570, nextbutton.get_width(), nextbutton.get_height())
nextl_rect = pygame.Rect(10, 570, nextbuttonl.get_width(), nextbuttonl.get_height())
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
            elif option4_rect.collidepoint(mouse_pos):
                ans, games1 = "d", 4
                print("Option C chosen - rohith")
                current_screen = 'game'
                pygame.event.clear()
            elif option5_rect.collidepoint(mouse_pos):
                ans, games1 = "e", 5
                print("Option C chosen - sridev")
                current_screen = 'game'
                pygame.event.clear()
            elif next_rect.collidepoint(mouse_pos):
                ans, games1 = "e", 4
                print("next character")
                current_screen = 'nextpg'
                pygame.event.clear()
        elif current_screen == 'nextpg':
            if nextl_rect.collidepoint(mouse_pos):
                print("back to character selection")
                current_screen = 'next'
                pygame.event.clear()
            elif option6_rect.collidepoint(mouse_pos):
                ans, games1 = "f", 6
                print("Option F chosen - patrick")
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
        char_map = {1: character1, 2: character2, 3: character3, 4:character4, 5: character5, 6: character6}
        game = Game(screen, clock, bg, char_map[games1])
        game.run()
        pygame.time.delay(500)
        pygame.event.clear()   # ← flush all buffered events
        current_screen = 'over'  # Reset to start after game ends
        #code to go back to the 1st screen after the game ends  
    elif current_screen == 'nextpg':
        nextpg()
        
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