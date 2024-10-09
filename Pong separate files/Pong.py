"""
pong module
"""
__version__="0.1.0"
import pygame, sys
from settings import width, height

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
#^Screen set up, title and game clock added
# --------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#^Command lines (while loop) for exiting the game - if select quit then programme closes. Checking for events.

    pygame.display.update()
    clock.tick(60)
#^Updating display frame rate, 60fps

#class Pong:
 #   def __init__(self, screen):
  #      self.screen = screen
   #     self.FPS = pygame.time.Clock()






def f(x):
    return x+2
