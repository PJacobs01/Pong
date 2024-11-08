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
class Game:
    def __init__(self):
        self.cpu_speed = 0

    def draw_menu(self):
        screen.fill('black')
        y_offset = 100
        for index, difficulty in enumerate(difficulties):
            text = font.render(difficulty,True, 'white')
            rect = text.get_rect(center=(width//2, y_offset))
            difficulty_rects.append((rect, difficulty))
            screen.blit(text,rect)
            y_offset +=100
        pygame.display.update()

    def menu_selection(self):
        while True:
            self.draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for rect, difficulty in difficulty_rects:
                        if rect.collidepoint(mouse_pos):
                            difficulty_rects.clear()
                            return difficulty

    def start_game(self, difficulty):
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
        elif difficulty == "Hard":
            cpu_speed = 5
            if b.ball.centery < p.cpu.centery:
                p.cpu.y -= cpu_speed
            elif b.ball.centery > p.cpu.centery:
                p.cpu.y += cpu_speed
        self.reset_ball()
        p.player.centery = height // 2
        p.cpu.centery = height //2

    def ball_movement(self):
        b.ball.x += b.ball_speed_x
        b.ball.y += b.ball_speed_y
        if b.ball.bottom >= height or b.ball.top <= 0:
            b.ball_speed_y *= -1
        if b.ball.right >= width:
            self.point_won("player")
        if b.ball.left <= 0:
            self.point_won("cpu")
        if b.ball.colliderect(p.player) or b.ball.colliderect(p.cpu):
            b.ball_speed_x *= -1.1

    def reset_ball(self):
        b.ball.x = width / 2 - 10
        b.ball.y = random.randint(10,400)
        b.ball_speed_x = b.original_speed
        b.ball_speed_y = b.original_speed * random.choice ((1, -1))

    def player_movement(self):
        p.player.y += p.player_speed
        if p.player.top <= 0:
            p.player.top = 0
        if p.player.bottom >= height:
            p.player.bottom = height

    def display_winner(self, screen, winner):
        if winner == "cpu":
            winner_text = score_font.render("CPU Wins! YOU LOSE", True, "white")
        else:
            winner_text = score_font.render("Player Wins!", True, "red")
        text_rect = winner_text.get_rect(center=(width/2, height/2))
        screen.blit(winner_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def point_won(self, winner):
        if winner == "cpu":
            p.cpu_points += 1
        if winner == "player":
            p.player_points += 1
        self.reset_ball()
        if p.cpu_points >= p.score_limit:
            self.display_winner(screen, "cpu")
            self.reset_game()
        elif p.player_points >= p.score_limit:
            self.display_winner(screen,"player")
            self.reset_game()

    def reset_game(self):
        p.cpu_points = 0
        p.player_points = 0
        self.reset_ball()
        difficulty = menu_selection()
        self.start_game(difficulty)
        pygame.display.set_caption("Pong")

    def run_game(self):
        difficulty = self.menu_selection()
        self.start_game(difficulty)
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

        self.ball_movement()
        self.player_movement()
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
    pygame.draw.rect(screen, 'white', p.player)
    pygame.draw.rect(screen, 'white', p.cpu)
    pygame.display.update()
    clock.tick(60)

game = Game()
game.run_game()