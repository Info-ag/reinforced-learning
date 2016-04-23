class Element(object):
    posX = 0
    posY = 0
    size = 20
    color = "green"

    def __init__(self, posX, posY, size, color):
        self.posX = posX
        self.posY = posY
        self.size = size if size else self.size


class Food(Element):
    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "green")


class Enemy(Element):
    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "red")
