import pygame as pg
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

empty = set()
for r in range(len(board)):
    for c in range(len(board[r])):
        empty.add((r, c))

window = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
winner = ' '

def checkWinner():
    for row in board:
        if row.count('o') == 3:
            return 'o'
        if row.count('x') == 3:
            return 'x'
    for col in zip(*board):
        if col.count('o') == 3:
            return 'o'
        if col.count('x') == 3:
            return 'x'
    diag1 = (board[0][0], board[1][1], board[2][2])
    diag2 = (board[0][2], board[1][1], board[2][0])
    if diag1.count('o') == 3:
        return 'o'
    if diag1.count('x') == 3:
        return 'x'
    if diag2.count('o') == 3:
        return 'o'
    if diag2.count('x') == 3:
        return 'x'
    if isBoardFull():
        return 'n'
    return ' '

def isBoardFull():
    for row in board:
        if ' ' in row:
            return False
    return True

while running:
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            r, c = (y) // 200, (x) // 200
            if (r, c) in empty:
                # Player move
                if winner == ' ':
                    board[r][c] = 'o'
                    empty.remove((r, c))

                # Check for winners
                winner = checkWinner()

                # Cpu move
                if winner == ' ':
                    r, c = random.choice(tuple(empty))
                    board[r][c] = 'x'
                    empty.remove((r, c))

                # Check for winners
                winner = checkWinner()

                # Stop if somebody won or is a tie
                if winner != ' ':
                    print(f'The winner is {winner}')
                    running = False


    # Update

    # Draw
    window.fill(WHITE)
    pg.draw.line(window, BLACK, (0, 200), (600, 200), 5)
    pg.draw.line(window, BLACK, (0, 400), (600, 400), 5)
    pg.draw.line(window, BLACK, (200, 0), (200, 600), 5)
    pg.draw.line(window, BLACK, (400, 0), (400, 600), 5)
    for r, row in enumerate(board):
        for c, el in enumerate(row):
            x, y = c*200, r*200
            if el == 'o':
                pg.draw.circle(window, BLACK, (x+100, y+100), 50)
                pg.draw.circle(window, WHITE, (x+100, y+100), 40)
            if el == 'x':
                off = 55
                w = 20
                pg.draw.line(window, RED, (x+off, y+off), (x+200-off, y+200-off), w)
                pg.draw.line(window, RED, (x+200-off, y+off), (x+off, y+200-off), w)
    pg.display.update()

pg.quit()
