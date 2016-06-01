from elements import Food
from elements import Enemy
from elements import Player
from field import Field
import random
import math

from Tkinter import *

widthPixel = 720
heightPixel = 720

nFoods = 10
nEnemies = 10
foods = []
enemies = []
size, x, y = 0, 0, 0

for i in xrange(nFoods):
    while True:
        flag = False
        size = 1.0 * Food.sizeF
        x = random.uniform(size / 2.0, 1 - size / 2.0)
        y = random.uniform(size / 2.0, 1 - size / 2.0)
        for n in foods:
            sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
            if sdump < n.size * Food.sizeF / 2.0 + size / 2.0:
                flag = True
        if not flag:
            break

    foods.extend([Food(x, y, size / Food.sizeF)])

for j in xrange(nEnemies):
    while True:
        flag = False
        size = 1 * Enemy.sizeF
        x = random.uniform(size / 2.0, 1 - size / 2.0)
        y = random.uniform(size / 2.0, 1 - size / 2.0)

        for n in enemies:
            sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
            if sdump < n.size * Enemy.sizeF / 2.0 + size / 2.0:
                flag = True
        for n in foods:
            sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
            if sdump < n.size * Food.sizeF / 2.0 + size / 2.0:
                flag = True
        if not flag:
            break

    enemies.extend([Enemy(x, y, size / Enemy.sizeF)])

while True:
    flag = False
    # size = random.randint(0, 0.1)
    size = 1 * Player.sizeF
    x = random.uniform(size / 2.0, 1 - size / 2.0)
    y = random.uniform(size / 2.0, 1 - size / 2.0)
    for i in foods:
        sdump = math.sqrt((x - i.posX) ** 2 + (y - i.posY) ** 2)
        if sdump < i.size * Player.sizeF / 2.0 + size / 2.0:
            flag = True
    for i in enemies:
        sdump = math.sqrt((x - i.posX) ** 2 + (y - i.posY) ** 2)
        if sdump < i.size * Player.sizeF / 2.0 + size / 2.0:
            flag = True
    if not flag:
        break

player = Player(x, y, size / Player.sizeF)


# angle = 0.2     # Zahlen von 0 bis 2 da Bogenmass als Winkelangabe


def update():
    angle = slider.get()
    collisions = player.checkcollision(angle)
    deltax, deltay = player.moveplayer(angle, collisions)
    player.checkeatingfood(foods, canvas)
    player.checkeatingenemy(enemies, canvas)
    finished = player.checkeatenallfood(foods)
    if finished:
        root.mainloop()
    player.posX = deltax
    player.posY = deltay
    canvas.delete(canvas.drawnplayer)
    canvas.drawplayer(player)
    root.after(10, update)


root = Tk()
root.title("1337 H4X0R5")
root.resizable(width=0, height=0)
slider = Scale(root, from_=0, to=2, orient=HORIZONTAL, resolution=0.1)
slider.pack()
canvas = Field(root, widthPixel, heightPixel)
canvas.pack()
canvas.drawfoods(foods)
canvas.drawenemies(enemies)
canvas.drawplayer(player)
root.after(0, update)
root.mainloop()
