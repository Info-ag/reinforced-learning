from elements import Food
from elements import Enemy
from field import Field
import random, math

from Tkinter import *

width = 720
height = 720

nFoods = 10
nEnemies = 10

foods = []
enemies = []

for i in xrange(nFoods):
    while True:
        flag = False
        #size = random.randint(0, 0.1)
        size = 20
        x = random.randint(size / 2, width - size / 2)
        y = random.randint(size / 2, height - size / 2)
        if len(foods) == 0:
            break
        else:
            for n in foods:
                sdump = math.sqrt((x - n.posX)**2 + (y - n.posY)**2)
                if sdump < n.size/2 + size/2:
                    flag = True
            for n in enemies:
                sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
                if sdump < n.size / 2 + size / 2:
                    flag = True
            if not(flag):
                break

    foods.extend([Food(x, y, size)])


for i in xrange(nEnemies):
    while True:
        flag = False
        # size = random.randint(0, 0.1)
        size = 20
        x = random.randint(size / 2, width - size / 2)
        y = random.randint(size / 2, height - size / 2)
        if len(enemies) == 0:
            break
        else:
            for n in enemies:
                sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
                if sdump < n.size / 2 + size / 2:
                    flag = True
            for n in foods:
                sdump = math.sqrt((x - n.posX) ** 2 + (y - n.posY) ** 2)
                if sdump < n.size / 2 + size / 2:
                    flag = True
            if not (flag):
                break

    enemies.extend([Enemy(x, y, size)])


def update():
    root.after(10, update)


root = Tk()
root.resizable(width=0, height=0)
canvas = Field(root, width, height)
canvas.pack()
canvas.drawfoods(foods)
canvas.drawenemies(enemies)

root.after(0, update)
root.mainloop()
