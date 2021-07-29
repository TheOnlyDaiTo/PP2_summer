import pygame as pg
import sys, random

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
FPS = 120
TARGET_FPS = 120
WIN_WIDTH = 1000
WIN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (5, 5, 5)

RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE = (5, 5, 255)



pg.init()
pg.font.init()

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('Hungry lion(but its not lion, its rect :))')

font = pg.font.SysFont('Comic sans', 50)
player_x = WIN_WIDTH / 2
player_y = 400
player_speed = 3
red_block_list = []
green_block_list = []
cnt = 0
score = 0
is_touched = False


for _ in range(50):
    red_block_x = random.randint(0, WIN_WIDTH)
    red_block_y = random.randint(-WIN_HEIGHT / 2, WIN_HEIGHT / 2)
    red_block_rect = pg.Rect((red_block_x, red_block_y, 20, 15))
    red_block_list.append((screen, RED, red_block_rect))

for _ in range(10):
    green_block_x = random.randint(0, WIN_WIDTH)
    green_block_y = random.randint(0, WIN_HEIGHT / 2)
    green_block_rect = pg.Rect((green_block_x, green_block_y, 20, 15))
    green_block_list.append((screen, GREEN, green_block_rect))

while True:
    player_rect = pg.Rect(player_x, player_y, 15, 15)
    keys_pressed = pg.key.get_pressed()
    screen.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if keys_pressed[pg.K_UP] and player_y>5:
        player_y -= player_speed
    if keys_pressed[pg.K_DOWN] and player_y<595:
        player_y += player_speed
    if keys_pressed[pg.K_LEFT] and player_x>5:
        player_x -= player_speed
    if keys_pressed[pg.K_RIGHT] and player_x<995:
        player_x += player_speed

    for i in red_block_list:
        pg.draw.rect(i[0], i[1], i[2])
        i[2][1] += 1
        if i[2][1] > WIN_HEIGHT:
            i[2][1] = -20
        if player_rect.colliderect(i[2]):
            i[2][1] = 10000
            i[2][0] = 10000
            score -= 1

    for i in green_block_list:
        pg.draw.rect(i[0], i[1], i[2])
        if player_rect.colliderect(i[2]):
            cnt += 1
            score += 1
            i[2][1] = 10000
            i[2][0] = 10000
        else:
            i[2][1] += random.randint(-2, 2)
            i[2][0] += random.randint(-2, 2)

    if not (0 <= player_y <= WIN_HEIGHT or 0 <= player_x <= WIN_WIDTH):
        player_speed = -player_speed
    score_text = f'{score}'
    score_surface = font.render(score_text, True, WHITE)
    score_rect = score_surface.get_rect(center = (50, 20))
    screen.blit(score_surface, score_rect)
    pg.draw.rect(screen, BLUE, player_rect)
    pg.display.update()
    clock.tick(FPS)