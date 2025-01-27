import pygame, sys
SCREEN_WIDTH = 800
SCREEN_HIGH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
pygame.display.set_caption('Platformer')

player_x,player_y = 100,100
player = pygame.image.load('./assets/MainCharacters/MaskDude/idle.png')
background = pygame.image.load('./assets/Background/Gray.png') #! поміняти зображення фону
pygame.init()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    pygame.display.update()

    pygame.time.Clock().tick(60)






pygame.quit()
