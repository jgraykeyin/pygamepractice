# Following a tutorial on https://pythonprogramming.net/pygame-python-3-part-1-intro/
# Using a 16-color CGA palette for kicks!
# Music from https://newretrowave.bandcamp.com/album/the-80s-dream-compilation-tape

import pygame
import os
import time
import random

pygame.init()
pygame.mixer.init()

# Let us use assets from current directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
pygame.mixer.music.load(os.path.join(__location__, "bgmusic1.mp3"))
pygame.mixer.music.play(-1,0.0)

display_width = 800
display_height = 600

black = (0,0,0)
grey = (85,85,85)
white = (255,255,255)
magenta = (255,85,255)
cyan = (85,255,255)
yellow = (255,255,85)
green = (85,255,85)
dark_green = (0,170,0)
blue = (85,85,255)

car_width = 190

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racing Game')
clock = pygame.time.Clock()

car_image = pygame.image.load(os.path.join(__location__, "playercar.png"))
cpu_image = pygame.image.load(os.path.join(__location__, "cpucar.png"))

def road_side(x,y,w,h,color):
    pygame.draw.rect(game_display,color,[x,y,w,h])

def road_lines(linex, liney, linew, lineh, color):
    pygame.draw.rect(game_display,color,[linex,liney,linew,lineh])

def things(thingx,thingy):
    #pygame.draw.rect(game_display,color, [thingx,thingy,thingw,thingh])
    game_display.blit(cpu_image, (thingx,thingy))

def car(x,y):
    game_display.blit(car_image, (x,y))

def text_objects(text,font):
    text_surface = font.render(text, True, yellow)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font(os.path.join(__location__,'PressStart2P-Regular.ttf'),32)
    TextSurf, TextRect = text_objects(text,large_text)
    TextRect.center = ((display_width / 2), (display_height /2))
    game_display.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display("GAME OVER")
    

def game_loop():
    x = (display_width * 0.38)
    y = (display_height * 0.7)
    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7

    road_line_startx = (display_width / 2)
    road_line_starty = -100
    road_line_speed = 12
    road_line_width = 10
    road_line_height = 100
    #thing_width = 100
    #thing_height = 100

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #game_exit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x+=x_change
        game_display.fill(grey)

        road_lines(road_line_startx, road_line_starty, road_line_width, road_line_height, yellow)
        road_line_starty += road_line_speed

        # Draw the CPU cars
        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        
        # Draw the player car
        car(x,y)

        road_side(0,0,100,display_height,dark_green)
        road_side(700,0,100,display_height,dark_green)

        if x < 100:
            x = 100
        elif x > 580:
            x = 580

        if thing_starty > display_height:
            thing_starty = 0 - 150
            thing_startx = random.randrange(0,display_width)

        if road_line_starty > display_height:
            road_line_starty = 0 - 100
            road_line_startx = (display_width / 2)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()