import pygame, sys
from settings import width, height, player_height, player_width

ball = pygame.Rect(width/2,height/2,30,30)

player = pygame.Rect(880,0, player_width, player_height)
cpu = pygame.Rect(0,0, player_width, player_height)


#First 2 values = coordinates, Last 2 values = dimensions in pixels