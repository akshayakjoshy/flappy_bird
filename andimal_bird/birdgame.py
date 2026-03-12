import pygame
from pygame.locals import *

pygame.init()
screen_width=360
screen_height=640
ans="k"
games1=0
 # code....  changed ....x
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Andimal Bird")
clock=pygame.time.Clock()
SCORE_COLOR = (255, 255, 255)   # White score text
GAME_OVER_RED = (200, 0, 0)     # Game over text
PIPE_GREEN = (0, 200, 0)        # Pipes
SKY_BLUE = (135, 206, 235)      # Background sky

test_font2=pygame.font.Font('/Users/mikmin/Desktop/birdgame/andimal_bird/BotsmaticRegularDemo.ttf',40)
text_font=pygame.font.Font('/Users/mikmin/Desktop/birdgame/andimal_bird/FlappyBirdRegular-9Pq0.ttf',40)
start_button=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/start2.png")
current_screen='start' 

# Load option buttons globally
option1=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/option button copy.png")
option2=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/option button copy.png")
option3=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/option button copy.png")

# Load character selection assets once
screen2=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/flappy bird wallpaper.jpeg")
character1=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/character1.png")
character2=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/character2.png")
character3=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/character3.png")

option_font1 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/andimal_bird/ByteBounce copy.ttf',25)
option_font2 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/andimal_bird/ByteBounce copy.ttf',25)
option_font3 = pygame.font.Font('/Users/mikmin/Desktop/birdgame/andimal_bird/ByteBounce copy.ttf',25)
textoption1 = option_font1.render('RIZZ GAWDD', True, 'black')
textoption2 = option_font2.render('SHAWARMAA', True, 'black')
textoption3 = option_font3.render('NIDHII', True, 'black')


#load images
bg=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/flappy bird wallpaper.jpeg")
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
        'ANDIMAL BIRD',
        PIPE_GREEN,
        (0, 0, 0),
        180,
        180
    )

def gamestart():
    screen.fill('BLUE')
    game_font=pygame.font.Font('/Users/mikmin/Desktop/birdgame/andimal_bird/FlappyBirdRegular-9Pq0.ttf',40)
    screen3=pygame.image.load("/Users/mikmin/Desktop/birdgame/andimal_bird/flappy bird wallpaper.jpeg")
    screen.blit(screen3,(0,0))
    draw_text_outline(
        game_font,
        'POII PADIKK PILAREE',
        SCORE_COLOR,
        (0, 0, 0),
        180,
        180
    )
    
# Screen 2: choose character
def chose_character():
    screen.blit(screen2,(0,0))
    screen.blit(option1,(50,200))
    screen.blit(character1,(229,237))
    screen.blit(textoption1,(100,260))
    screen.blit(option2,(50,250))
    screen.blit(character2,(229,300))
    screen.blit(textoption2,(100,310))   
    screen.blit(option3,(50,300))  
    screen.blit(textoption3,(100,360))
    screen.blit(character3,(229,350))

    draw_text_outline(
        text_font,
        'CHOOSSE YOUR CHARACTER',
        SCORE_COLOR,
        (0, 0, 0),
        180,
        180
    )

mouse_pos = (0, 0) 
while True :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # START SCREEN: Check start button
            if current_screen == 'start':
                if 105 <= mouse_pos[0] <= 105 + start_button.get_width() and 290 <= mouse_pos[1] <= 290 + start_button.get_height():
                    current_screen = 'next'
                    print('Start button clicked')
            
            # CHARACTER SELECTION SCREEN: Check character buttons
            elif current_screen == 'next':
                if 50 <= mouse_pos[0] <= 50 + option1.get_width() and 200 <= mouse_pos[1] <= 200 + option1.get_height():
                    ans = "a"
                    games1 = 1
                    current_screen = 'game'
                    print("Option A chosen - RIZZ GAWDD")
                    
                    
                elif 50 <= mouse_pos[0] <= 50 + option2.get_width() and 250 <= mouse_pos[1] <= 250 + option2.get_height():
                    ans = "b"
                    games1 = 2
                    print("Option B chosen - SHAWARMAA")
                    current_screen = 'game'
                    
                elif 50 <= mouse_pos[0] <= 50 + option3.get_width() and 300 <= mouse_pos[1] <= 300 + option3.get_height():
                    ans = "c"
                    games1 = 3
                    print("Option C chosen - PULINGOOO")
                    current_screen = 'game'

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
        gamestart()
    
    pygame.display.update()
    clock.tick(60)
