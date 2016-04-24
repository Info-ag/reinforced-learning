import math


class Element(object):
    posX = 0
    posY = 0
    size = 1
    sizeF = 0.03
    color = "green"

    def __init__(self, posX, posY, size, color):
        self.posX = posX
        self.posY = posY
        self.size = size if size else self.size
        self.color = color


class Food(Element):
    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "green")


class Enemy(Element):
    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "red")


class Player(Element):
    velocity = [math.cos(0), math.sin(0)]
    speed = math.sqrt(velocity[0] ** 2 + velocity[1] ** 2)
    sizeF = 0.05

    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "blue")


    def moveplayer(self, angle):
        self.velocity = [math.cos(angle * math.pi), math.sin(angle * math.pi)]
        deltax = self.posX + self.velocity[1] *0.001
        deltay = self.posY + self.velocity[0] *0.001
        #print "Debug"
        #print self.posX, self.posY
        return deltax, deltay
