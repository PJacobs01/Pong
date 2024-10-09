"""
pong module
"""
__version__="0.1.0"
import pygame, sys
from settings import width, height
import ball
import random

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
#^Screen set up, title and game clock added
#------------------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#^Command lines (while loop) for exiting the game - if select quit then programme closes. Checking for events.

    #screen.fill('black')
    # Drawing objects
    pygame.draw.aaline(screen, 'white', (width / 2, 0), (width / 2, height))
    pygame.draw.ellipse(screen, 'white', ball.ball)
    # ^1st, where to draw object, 2nd is colour, 3rd define of rect (pulled from ball .py) .ellipse = circle
    pygame.draw.rect(screen, 'red', ball.player)
    # Player paddle + position
    pygame.draw.rect(screen, 'white', ball.cpu)
    # CPU paddle + position
    ball.x += ball.ball_speed_x
    ball.y += ball.ball_speed_y
    #ATTEMPT TO MAKE THE BALL MOVE

    pygame.display.update()
    clock.tick(60)
#^Updating display frame rate, 60fps

#class Pong:
 #   def __init__(self, screen):
  #      self.screen = screen
   #     self.FPS = pygame.time.Clock()






def f(x):
    return x+2
