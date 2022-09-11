import pygame as pg
from random import randint

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GRID_W = 80
GRID_H = 50

window = pg.display.set_mode((800, 500))
clock = pg.time.Clock()
running = True

class Square:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def draw(self, window, color):
        pg.draw.rect(window, color, (self.c*10, self.r*10, 10, 10))


class Snake:
    def __init__(self):
        self.pieces = [Square(25, 40), Square(25, 41)]

    def update(self, dir, apple: Square):
        # Grow
        if self.pieces[-1].r == apple.r and self.pieces[-1].c == apple.c:
            self.pieces.append(Square(apple.r, apple.c))
            apple.r = randint(0, 49)
            apple.c = randint(0, 79)
        # Move
        for i in range(len(self.pieces)-1):
            self.pieces[i].r = self.pieces[i+1].r
            self.pieces[i].c = self.pieces[i+1].c
        self.pieces[-1].r += dir[0]
        self.pieces[-1].c += dir[1]
        # Wrap
        if self.pieces[-1].r < 0:
            self.pieces[-1].r = 49
        if self.pieces[-1].c < 0:
            self.pieces[-1].c = 79
        if self.pieces[-1].c >= 80:
            self.pieces[-1].c = 0
        if self.pieces[-1].r >= 50:
            self.pieces[-1].r = 0
        # Lose if overlap
        for i in range(len(self.pieces) -1):
            if self.pieces[i].r == self.pieces[-1].r and self.pieces[i].c == self.pieces[-1].c:
                global running
                running = False
 
    def draw(self, window):
        for piece in self.pieces:
            piece.draw(window, BLACK)

dir = (0, 1)
apple = Square(randint(0, 49), randint(0, 79))
snake = Snake()

while running:
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_UP:
                dir = (-1, 0)
            if event.key == pg.K_DOWN:
                dir = (1, 0)
            if event.key == pg.K_LEFT:
                dir = (0, -1)
            if event.key == pg.K_RIGHT:
                dir = (0, 1)
    # Update
    snake.update(dir, apple)
    # Draw
    window.fill(WHITE)
    snake.draw(window)
    apple.draw(window, RED)
    pg.display.update()
    # Framerate
    clock.tick(5)

pg.quit()

