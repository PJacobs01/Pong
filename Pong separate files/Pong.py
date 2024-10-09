"""
pong module
"""
__version__="0.1.0"
import pygame, sys
from settings import width, height
import ball as b
import player as p
import random

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

#^Screen set up, title and game clock added
#------------------------------------------------------
def ball_movement():
    b.ball.x += b.ball_speed_x
    b.ball.y += b.ball_speed_y
    # Ball movemennt
    if b.ball.bottom >= height or b.ball.top <= 0:
        b.ball_speed_y *= -1
    if b.ball.right >= width:
        point_won("cpu")
    if b.ball.left <= 0:
        point_won("player")

    if b.ball.colliderect(p.player) or b.ball.colliderect(p.cpu):
        b.ball_speed_x *=-1

def reset_ball():
    b.ball.x = width / 2 - 10
    b.ball.y = random.randint(10,100)
    b.ball_speed_x *= random.choice([-1,1])
    b.ball_speed_y *= random.choice([-1,1])

def player_movement():
    p.player.y += p.player_speed
    if p.player.top <= 0:
        p.player.top = 0
    if p.player.bottom >= height:
        p.player.bottom = height

def cpu_movement():
    p.cpu.y += p.cpu_speed
    if b.ball.centery <= p.cpu.centery:
        p.cpu_speed = - 3.75
    if b.ball.centery >= p.cpu.centery:
        p.cpu_speed = 3.75

    if p.cpu.top <= 0:
        p.cpu.top = 0
    if p.cpu.bottom >= height:
        p.cpu.bottom = height

def point_won(winner):
    p.cpu_points, p.player_points
    if winner == "cpu":
        p.cpu_points += 1
    if winner == "player":
        p.player_points += 1
    reset_ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # ^Command lines (while loop) for exiting the game - if select quit then programme closes. Checking for events.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p.player_speed = -6
            if event.key == pygame.K_DOWN:
                p.player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p.player_speed = 0
            if event.key == pygame.K_DOWN:
                p.player_speed = 0

#^Command lines (while loop) for exiting the game - if select quit then programme closes. Checking for events.
    ball_movement()
    player_movement()
    cpu_movement()
    score_font = pygame.font.Font(None, 100)

    # Drawing objects
    screen.fill('black')
    cpu_score_surface = score_font.render(str(p.cpu_points), True, "white")
    player_score_surface = score_font.render(str(p.player_points), True, "white")
    screen.blit(cpu_score_surface,(width/4,0))
    screen.blit(player_score_surface,(3*width/4,0))
    #Scores display

    pygame.draw.aaline(screen, 'white', (width / 2, 0), (width / 2, height))
    pygame.draw.ellipse(screen, 'white', b.ball)
    # ^1st, where to draw object, 2nd is colour, 3rd define of rect (pulled from ball .py) .ellipse = circle
    pygame.draw.rect(screen, 'red', p.player)
    # Player paddle + position
    pygame.draw.rect(screen, 'white', p.cpu)
    # CPU paddle + position

    pygame.display.update()
    clock.tick(60)
#^Updating display frame rate, 60fps






#def f(x):
 #   return x+2
