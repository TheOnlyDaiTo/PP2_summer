import pygame as pg
import time
import random

from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_q, K_p
#Я не использвал эти константы как в во второй игре, но пусть стоят, прикольно)))

snake_block = 10
FPS = 15

WHITE = (255, 255, 255)
BLACK = (5, 5, 5)

GREEN = (0, 255, 0)
BLUE = (5, 5, 255)

WIN_WIDTH = 1000
WIN_HEIGHT = 600

pg.init()

dis = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption('Snake game(btw its not snake its just multipliing rect :))')

clock = pg.time.Clock()



font_style = pg.font.SysFont("Comic sans", 25)
score_font = pg.font.SysFont("Comic sans", 35)


def Your_score(score):
    value = score_font.render(str(score), True, WHITE)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, WHITE, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [WIN_WIDTH / 6, WIN_HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = WIN_WIDTH / 2
    y1 = WIN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIN_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, WIN_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(BLACK)
            message("My program crashed or u lose, I think its the 2nd. Press P-Play Again or Q-Quit", WHITE)
            Your_score(Length_of_snake - 1)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_p:
                        gameLoop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIN_WIDTH or x1 < 0 or y1 >= WIN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        pg.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pg.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIN_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, WIN_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(FPS)

    pg.quit()
    quit()


gameLoop()