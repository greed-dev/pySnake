import random
import pygame

from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_c,
    QUIT
)

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

GRID_HEIGHT = SCREEN_HEIGHT/20
GRID_WIDTH = SCREEN_WIDTH/20

X_STEP = GRID_HEIGHT
Y_STEP = GRID_WIDTH

x_pos = SCREEN_WIDTH/2 - GRID_WIDTH
y_pos = SCREEN_HEIGHT/2 - GRID_HEIGHT

x_change = 0
y_change = 1

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

def message(screen,msg,font, color, pos_x, pos_y):
    msg = font.render(msg, True, color)
    screen.blit(msg, [pos_x, pos_y])
    pygame.display.update()

def generateFoodPos():
    rand_x = random.randrange(0,SCREEN_WIDTH)
    rand_y = random.randrange(0,SCREEN_HEIGHT)
    food_x = round((rand_x - (rand_x % 25)))
    food_y = round((rand_y - (rand_y % 25)))

    return food_x, food_y

def draw_snake(screen, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, blue, [block[0], block[1], GRID_WIDTH, GRID_HEIGHT])

def main():
    running = True
    game_over = False

    global x_pos
    global y_pos

    global x_change
    global y_change

    length = 1
    snake = []

    pygame.init()
    pygame.display.set_caption('pySnake by Greed')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    food_x, food_y = generateFoodPos()

    while running:
        while game_over:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        x_pos = SCREEN_WIDTH/2 - GRID_WIDTH
                        y_pos = SCREEN_HEIGHT/2 - GRID_HEIGHT
                        x_change = 0
                        y_change = 1
                        main()
                        game_over = False
                    elif event.key == K_ESCAPE:
                        running = False
                        game_over = False
                elif event.type == QUIT:
                    running = False
                    game_over = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    y_change = -1
                    x_change = 0
                if event.key == K_DOWN:
                    y_change = 1
                    x_change = 0
                if event.key == K_RIGHT:
                    y_change = 0
                    x_change = 1
                if event.key == K_LEFT:
                    y_change = 0
                    x_change = -1
            elif event.type == QUIT:
                running = False

        x_pos += x_change * X_STEP
        y_pos += y_change * Y_STEP

        snake_head = []
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snake.append(snake_head)

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, GRID_WIDTH, GRID_HEIGHT])

        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                message(screen, 'Game Over - C to Play Again!', pygame.font.SysFont(None, 30), red, 112, 225)
                game_over = True

        if x_pos == food_x and y_pos == food_y:
            food_x, food_y = generateFoodPos()
            length += 1

        if x_pos >= SCREEN_WIDTH or x_pos < 0 or y_pos >= SCREEN_HEIGHT or y_pos < 0:
            message(screen, 'Game Over - C to Play Again!', pygame.font.SysFont(None, 30), red, 112, 225)
            game_over = True

        message(screen, "Your Score: "+str(length-1), pygame.font.SysFont(None, 30), white, 15, 15)
        draw_snake(screen, snake)
        pygame.display.update()
        clock.tick(6)
main()