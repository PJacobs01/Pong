"""
pong module
"""
__version__="0.1.0"
import pygame, sys
from settings import width, height
import ball as b
import player as p
import random
random.seed()

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Select Difficulty")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
difficulties = ["Easy", "Medium", "Hard"]
difficulty_rects = []

#^Screen set up, title and game clock added
#------------------------------------------------------

def draw_menu():
    screen.fill('black')
    y_offset = 150
    for index, difficulty in enumerate(difficulties):
        text = font.render(difficulty,True, 'white')
        rect = text.get_rect(center=(width//2, y_offset))
        difficulty_rects.append((rect, difficulty))
        screen.blit(text,rect)
        y_offset +=100

    pygame.display.update()

def menu_selection():
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for rect, difficulty in difficulty_rects:
                    if rect.collidepoint(mouse_pos):
                        return difficulty

def start_game(difficulty):
    if difficulty == "Easy":
        cpu_speed = 3.75
        if b.ball.centery < p.cpu.centery - 15:
            p.cpu.y -= cpu_speed
        elif b.ball.centery > p.cpu.centery + 15:
            p.cpu.y += cpu_speed
    elif difficulty == "Medium":
        cpu_speed = 4.5
        if b.ball.centery < p.cpu.centery :
            p.cpu.y -= cpu_speed
        elif b.ball.centery > p.cpu.centery :
            p.cpu.y += cpu_speed
        """if random.random() < 0.1:
            p.cpu.centery += random.choice ([-cpu_speed, cpu_speed])"""
    elif difficulty == "Hard":
        cpu_speed = 5
        if b.ball.centery < p.cpu.centery:
            p.cpu.y -= cpu_speed
        elif b.ball.centery > p.cpu.centery:
            p.cpu.y += cpu_speed
        """p.cpu.centery = b.ball.centery + b.ball_speed_x * 2
        if p.cpu.top < 0:
            p.cpu.top = 0
        if p.cpu.bottom > height:
            p.cpu.bottom = height"""

def ball_movement():
    b.ball.x += b.ball_speed_x
    b.ball.y += b.ball_speed_y
    # Ball movemennt
    if b.ball.bottom >= height or b.ball.top <= 0:
        b.ball_speed_y *= -1
    if b.ball.right >= width:
        point_won("player")
    if b.ball.left <= 0:
        point_won("cpu")

    if b.ball.colliderect(p.player) or b.ball.colliderect(p.cpu):
        b.ball_speed_x *= -1.1
"""
def speed_up():
    delta = int(p.cpu_points + p.player_points) //5
    if b.ball_speed_x > 0:
        b.ball_speed_x += delta
    #else:
     #   b.ball_speed_x -= delta
    if b.ball_speed_y > 0:
        b.ball_speed_y += delta
   # else:
     #   b.ball_speed_y -= delta
"""

def reset_ball():
    b.ball.x = width / 2 - 10
    b.ball.y = random.randint(10,100)
    b.ball_speed_x *= random.choice([6,-6])

def player_movement():
    p.player.y += p.player_speed
    if p.player.top <= 0:
        p.player.top = 0
    if p.player.bottom >= height:
        p.player.bottom = height
"""
def cpu_movement():
    p.cpu.y += p.cpu_speed
    if b.ball.centery <= p.cpu.centery:
        p.cpu_speed = -4.5
    if b.ball.centery >= p.cpu.centery:
        p.cpu_speed = 4.5
    if p.cpu.top <= 0:
        p.cpu.top = 0
    if p.cpu.bottom >= height:
        p.cpu.bottom = height
"""

def display_winner(screen, winner):
    if winner == "cpu":
        winner_text = score_font.render("CPU Wins! YOU LOSE", True, "white")
    else:
        winner_text = score_font.render("Player Wins!", True, "red")

    text_rect = winner_text.get_rect(center=(width/2, height/2))
    screen.blit(winner_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def point_won(winner):
    if winner == "cpu":
        p.cpu_points += 1
    if winner == "player":
        p.player_points += 1
    reset_ball()
    if p.cpu_points >= p.score_limit:
        display_winner(screen, "cpu")
        reset_game()
    elif p.player_points >= p.score_limit:
        display_winner(screen,"player")
        reset_game()

def reset_game():
    p.cpu_points = 0
    p.player_points = 0
    reset_ball()

difficulty = menu_selection()
cpu_speed = start_game(difficulty)
pygame.display.set_caption("Pong")

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
    start_game(difficulty)
    ball_movement()
    player_movement()
    #cpu_movement()
    #speed_up()
    score_font = pygame.font.Font(None, 100)

    # Drawing objects
    screen.fill('black')
    cpu_score_surface = score_font.render(str(p.cpu_points), True, "white")
    player_score_surface = score_font.render(str(p.player_points), True, "white")
    screen.blit(player_score_surface,(width/4,0))
    screen.blit(cpu_score_surface,(3*width/4,0))
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
