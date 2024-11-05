import pygame
from settings import width, height, player_height, player_width
import random

#Ball
ball = pygame.Rect(width/2,height/2,30,30)
ball_speed_x = random.choice([-6,6])
ball_speed_y = random.choice([-6,6])


original_speed = random.choice([-6,6])


