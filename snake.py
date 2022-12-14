import pygame
from settings import *

class Snake ():
    
    def draw_snake (snake_size, snake_pixels):
        i = 0
        for pixel in snake_pixels:
            if i==len(snake_pixels)-1:
                pygame.draw.rect(game_display, red, [pixel[0], pixel[1], snake_size, snake_size])
            else:
                pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])
            i+=1
    