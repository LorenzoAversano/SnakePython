import pygame, time, random

white = (255, 255, 255)
black = (0,0,0)
red = (255, 0,0)
width, height = 600, 400
size = (width,height)
screen = pygame.display.set_mode(size)
bg_image = pygame.image.load("img/snake.jpeg")

game_display = pygame.display.set_mode ((width, height))
pygame.display.set_caption("Snake by Lorenzo")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

