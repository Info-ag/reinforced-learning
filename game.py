from elements import Food
from elements import Enemy
from elements import Player
from field import Field
import random, math

from Tkinter import *

widthPixel = 720
heightPixel = 720

nFoods = 10
nEnemies = 10
foods = []
enemies = []

for i in xrange(nFoods):
    while True:
        flag = False
        # size = random.randint(0, 0.1)
        size = 1.0 * Food.sizeF
        x = random.uniform(size / 2.0, 1 - size / 2.0)
        y = random.uniform(size / 2.0, 1 - size / 2.0)
        for n in foods:
            sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
            if sdump < n.size * Food.sizeF / 2.0 + size / 2.0:
                flag = True
        if not (flag):
            break

    foods.extend([Food(x, y, size / Food.sizeF)])

for i in xrange(nEnemies):
    while True:
        flag = False
        # size = random.randint(0, 0.1)
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
        if not (flag):
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
    if not (flag):
        break

player = Player(x, y, size / Player.sizeF)


def update():
    deltax, deltay = player.moveplayer(0.2)  # Zahlen von 0 bis 2 da Bogenmass als Winkelangabe
    player.posX = deltax
    player.posY = deltay
    #print player.posX * canvas.width - (.5 * size * player.sizeF * canvas.width)
    canvas.delete(canvas.drawnplayer)
    canvas.drawplayer(player)
    root.after(10, update)


root = Tk()
root.title("1337 H4X0R5")
root.resizable(width=0, height=0)
canvas = Field(root, widthPixel, heightPixel)
canvas.pack()
canvas.drawfoods(foods)
canvas.drawenemies(enemies)
canvas.drawplayer(player)
root.after(0, update)
root.mainloop()
