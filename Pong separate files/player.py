import pygame
from settings import width, height, player_height, player_width
#Player Pad
player = pygame.Rect(0,0, player_width, player_height)
player.centery = height/2
player_speed = 0

#CPU Pad
cpu = pygame.Rect(880,0, player_width, player_height)
cpu.centery = height/2
#First 2 values = coordinates, Last 2 values = dimensions in pixels