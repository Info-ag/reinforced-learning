from Tkinter import *

class Field(Canvas):
    def __init__(self, root, width, height):
        Canvas.__init__(self, root, width=width, height=height)

    def drawfoods(self, foodlist):
        for i in foodlist:
            size = i.size
            x0 = i.posX - .5*size
            y0 = i.posY - .5*size
            x1 = x0 + size
            y1 = y0 + size
            self.create_oval(x0, y0, x1, y1, fill="green")

    def drawenemies(self, enemylist):
        for i in enemylist:
            size = i.size
            x0 = i.posX - .5*size
            y0 = i.posY - .5*size
            x1 = x0 + size
            y1 = y0 + size
            self.create_oval(x0, y0, x1, y1, fill="red")
