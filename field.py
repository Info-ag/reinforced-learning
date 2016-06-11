from Tkinter import *


class Field(Canvas):
    height = 0
    width = 0
    drawnfood = []
    drawnenemy = []
    drawnplayer = 0

    def __init__(self, root, width, height):
        self.height = height
        self.width = width
        Canvas.__init__(self, root, width=width, height=height)

    def drawfoods(self, foodlist):
        for food in foodlist:
            size = food.size
            sizeF = food.sizeF
            x0 = food.posX * self.width - (.5 * size * sizeF * self.width)
            y0 = food.posY * self.height - (.5 * size * sizeF * self.height)
            x1 = x0 + size * sizeF * self.width
            y1 = y0 + size * sizeF * self.height
            self.drawnfood.append(
                self.create_oval(int(x0 + 0.5), int(y0 + 0.5), int(x1 + 0.5), int(y1 + 0.5), fill=food.color))

    def drawenemies(self, enemylist):
        for enemy in enemylist:
            size = enemy.size
            sizeF = enemy.sizeF
            x0 = enemy.posX * self.width - (.5 * size * sizeF * self.width)
            y0 = enemy.posY * self.height - (.5 * size * sizeF * self.height)
            x1 = x0 + (size * sizeF * self.width)
            y1 = y0 + (size * sizeF * self.height)
            self.drawnenemy.append(
                self.create_oval(int(x0 + 0.5), int(y0 + 0.5), int(x1 + 0.5), int(y1 + 0.5), fill=enemy.color))

    def drawplayer(self, player):
        size = player.size
        sizeF = player.sizeF
        x0 = player.posX * self.width - (.5 * size * sizeF * self.width)
        y0 = player.posY * self.height - (.5 * size * sizeF * self.height)
        x1 = x0 + (size * sizeF * self.width)
        y1 = y0 + (size * sizeF * self.height)
        self.drawnplayer = self.create_oval(int(x0 + 0.5), int(y0 + 0.5), int(x1 + 0.5), int(y1 + 0.5),
                                            fill=player.color)
