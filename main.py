import pygame as pg 
from random import randint
import time 



BLUE = (153, 204, 155)
win_size = (800, 600)
mw = pg.display.set_mode(win_size)
mw.fill(BLUE)
caption = pg.display.set_caption('Пинг понг')
clock = pg.time.Clock()

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed_x=0, speed_y=0):
      super().__init__()
      self.rect = pg.Rect(x, y, w, h)
      self.image = pg.transform.scale(pg.image.load(filename), (w, h))
      self.speed_x = speed_x
      self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Player(Base_sprite):
    def update(self):
        super().update()

players = pg.sprite.Group()
all_sprites = pg.sprite.Group()

player1 = Player('images/ping_rocket1.png', 40, 225, 30, 150)
player2 = Player('images/ping_rocket2.png', 730, 225, 30, 150)
players.add(player1)
players.add(player2)
all_sprites.add(player1)
all_sprites.add(player2)


play = True
game = True
win = False
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player1.speed_y = -5
            if event.key == pg.K_DOWN:
                player1.speed_y = 5
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player1.speed_y = 0
            if event.key == pg.K_RIGHT:
                player1.speed_y = 0

    if game:
       


        all_sprites.draw(mw)
        all_sprites.update()



    pg.display.update()
    clock.tick(60)