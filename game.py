from elements import Food
from elements import Enemy
from elements import Player
from field import Field
import random
import math
import tkMessageBox

from Tkinter import *

class game:

    nFoods = 10
    nEnemies = 10
    foods = []
    enemies = []
    size, x, y = 0, 0, 0

    def __init__(self, _root, _slider, _canvas, _label):
        self.root = _root
        self.slider = _slider
        self.canvas = _canvas
        self.label = _label
        self.btn_reset = Button(root, text="Reset game", command=self.resetgame, state=DISABLED)
        self.btn_reset.pack()

    def init_objects(self):
        for i in xrange(self.nFoods):
            while True:
                flag = False
                size = 1.0 * Food.sizeF
                self.x = random.uniform(size / 2.0, 1 - size / 2.0)
                self.y = random.uniform(size / 2.0, 1 - size / 2.0)
                for n in self.foods:
                    sdump = math.sqrt((self.x - n.posX) ** 2 + (self.y - n.posY) ** 2)
                    if sdump < n.size * Food.sizeF / 2.0 + size / 2.0:
                        flag = True
                if not flag:
                    break

            self.foods.extend([Food(self.x, self.y, self.size / Food.sizeF)])

        for j in xrange(self.nEnemies):
            while True:
                flag = False
                size = 1 * Enemy.sizeF
                self.x = random.uniform(size / 2.0, 1 - size / 2.0)
                self.y = random.uniform(size / 2.0, 1 - size / 2.0)

                for n in self.enemies:
                    sdump = math.sqrt((self.x - n.posX) ** 2 + (self.y - n.posY) ** 2)
                    if sdump < n.size * Enemy.sizeF / 2.0 + size / 2.0:
                        flag = True
                for n in self.foods:
                    sdump = math.sqrt((self.x - n.posX) ** 2 + (self.y - n.posY) ** 2)
                    if sdump < n.size * Food.sizeF / 2.0 + size / 2.0:
                        flag = True
                if not flag:
                    break

            self.enemies.extend([Enemy(self.x, self.y, self.size / Enemy.sizeF)])

        while True:
            flag = False
            # size = random.randint(0, 0.1)
            size = 1 * Player.sizeF
            self.x = random.uniform(size / 2.0, 1 - size / 2.0)
            self.y = random.uniform(size / 2.0, 1 - size / 2.0)
            for i in self.foods:
                sdump = math.sqrt((self.x - i.posX) ** 2 + (self.y - i.posY) ** 2)
                if sdump < i.size * Player.sizeF / 2.0 + size / 2.0:
                    flag = True
            for i in self.enemies:
                sdump = math.sqrt((self.x - i.posX) ** 2 + (self.y - i.posY) ** 2)
                if sdump < i.size * Player.sizeF / 2.0 + size / 2.0:
                    flag = True
            if not flag:
                break

        self.player = Player(self.x, self.y, self.size / Player.sizeF)

    def update(self):
        angle = self.slider.get()
        collisions = self.player.checkcollision(angle)
        deltax, deltay = self.player.moveplayer(angle, collisions)
        self.foods = self.player.checkeatingfood(self.foods, self.canvas)
        self.enemies = self.player.checkeatingenemy(self.enemies, self.canvas)
        finished = self.player.checkeatenallfood(self.foods)
        self.label.set("Score: " + str(self.player.score))
        if finished:
            tkMessageBox.showinfo("Game completed", "Game completed with score " + str(self.player.score))
            self.btn_reset.configure(state=NORMAL)
            self.root.mainloop()
        self.player.posX = deltax
        self.player.posY = deltay
        self.canvas.delete(self.canvas.drawnplayer)
        self.canvas.drawplayer(self.player)
        self.root.after(1, self.update)

    def startgame(self):
        self.canvas.drawfoods(self.foods)
        self.canvas.drawenemies(self.enemies)
        self.canvas.drawplayer(self.player)
        self.root.after(0, self.update)
        self.root.mainloop()

    def resetgame(self):
        self.btn_reset.configure(state=DISABLED)
        self.x, self.y, self.size = 0, 0, 0
        z = 0
        for enemie in self.enemies:
            canvas.delete(canvas.drawnenemy[z])
            del canvas.drawnenemy[z]
        self.enemies = []
        z = 0
        for food in self.foods:
            canvas.delete(canvas.drawnfood[z])
            del canvas.drawnfood[z]
        self.foods = []
        canvas.delete(canvas.drawnplayer)
        self.init_objects()
        self.startgame()

widthPixel = 720
heightPixel = 720

root = Tk()
root.configure(bg='white')
root.title("1337 H4X0R5")
root.resizable(width=0, height=0)
slider = Scale(root, from_=0, to=2, orient=HORIZONTAL, resolution=0.01)
slider.configure(bg='white', highlightthickness=0)
slider.pack()
label = StringVar()
Label(root, textvariable=label, bg='white').pack()
canvas = Field(root, widthPixel, heightPixel)
canvas.configure(bg='grey')
canvas.pack()


game = game(root, slider, canvas, label)

game.init_objects()
game.startgame()

