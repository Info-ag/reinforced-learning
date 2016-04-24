from Tkinter import *


class Field(Canvas):
    height = 0
    width = 0

    def __init__(self, root, width, height):
        self.height = height
        self.width = width
        Canvas.__init__(self, root, width=width, height=height)

    def drawfoods(self, foodlist):
        for i in foodlist:
            size = i.size
            sizeF = i.sizeF
            x0 = i.posX * self.width - (.5 * size * sizeF * self.width)
            y0 = i.posY * self.height - (.5 * size * sizeF * self.height)
            x1 = x0 + size * sizeF * self.width
            y1 = y0 + size * sizeF * self.height
            # print size
            # print sizeF
            # print self.height
            self.create_oval(int(x0 + 0.5), int(y0 + 0.5), int(x1 + 0.5), int(y1 + 0.5), fill=i.color)

    def drawenemies(self, enemylist):
        for i in enemylist:
            size = i.size
            sizeF = i.sizeF
            x0 = i.posX * self.width - (.5 * size * sizeF * self.width)
            y0 = i.posY * self.height - (.5 * size * sizeF * self.height)
            x1 = x0 + (size * sizeF * self.width)
            y1 = y0 + (size * sizeF * self.height)
            self.create_oval(int(x0 + 0.5), int(y0 + 0.5), int(x1 + 0.5), int(y1 + 0.5), fill=i.color)

    def drawplayer(self, player):
        size = player.size
        sizeF = player.sizeF
        x0 = player.posX * self.width - (.5 * size * sizeF * self.width)
        y0 = player.posY * self.height - (.5 * size * sizeF * self.height)
        #print player.posX, player.posY
        x1 = x0 + (size * sizeF * self.width)
        y1 = y0 + (size * sizeF * self.height)
        self.drawnplayer = self.create_oval(int(x0 + 0.5), int(y0 + 0.5), int(x1 + 0.5), int(y1 + 0.5), fill=player.color)
