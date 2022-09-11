import pygame as pg
from random import randint

pg.init()

class Star:
    def __init__(self):
        self.pos = pg.Vector2()
        self.vel = pg.Vector2()
        self.radius = 2
        self.spawn()

    def spawn(self):
        z = randint(10, 30) / 10
        self.pos = pg.Vector2(randint(0, 800), randint(0, 500))
        self.vel = self.pos - pg.Vector2(400, 250)
        self.vel.normalize_ip()
        self.vel.scale_to_length(z*1.5)
        self.radius = 4/z
    
    def update(self):
        self.pos += self.vel
        if self.pos.x < 0 or self.pos.y < 0 or self.pos.x > 800 or self.pos.y > 500:
            self.spawn()

window = pg.display.set_mode((800, 500))
clock = pg.time.Clock()
running = True

stars = []
for _ in range(200):
    stars.append(Star())

while running:
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # Update
    for star in stars:
        star.update()
    
    # Draw
    window.fill((0, 0, 0))
    for star in stars:
        pg.draw.circle(window, (255, 255, 255), star.pos, star.radius)
    pg.display.update()

    # Frame rate
    clock.tick(60)
    
pg.quit()

