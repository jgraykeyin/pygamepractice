# Following a tutorial on https://pythonprogramming.net/pygame-python-3-part-1-intro/
# Sticking to a 4-color CGA color palette for kicks

import pygame
import os

pygame.init()

# Let us use assets from current directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
magenta = (255,85,255)
cyan = (85,255,255)

car_width = 190

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racing Game')
clock = pygame.time.Clock()
#crashed = False
car_image = pygame.image.load(os.path.join(__location__, "playercar.png"))

def car(x,y):
    game_display.blit(car_image, (x,y))

def game_loop():
    x = (display_width * 0.38)
    y = (display_height * 0.7)
    x_change = 0
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x+=x_change
        
        game_display.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()