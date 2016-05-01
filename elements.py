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
    score = 0
    speedF = 0.001

    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "blue")

    def checkcollision(self):
        collisions = [0, 0, 0, 0]
        if not self.posY + self.sizeF / 2 > 0:
            collisions[0] = 1
        if not self.posX + self.sizeF / 2 < 1:
            collisions[1] = 1
        if not self.posY + self.sizeF / 2 < 1:
            collisions[2] = 1
        if not self.posX + self.sizeF / 2 > 0:
            collisions[3] = 1
        return collisions

    def moveplayer(self, angle, field, collisions):
        deltax = self.posX
        deltay = self.posY

        z = 0
        #print self.posX, self.posY, angle, field.width, field.height
        self.velocity = [math.cos(angle * math.pi), math.sin(angle * math.pi)]
        for i in collisions:
            if i == 1:
                z += 1
        if z == 0:
            deltax = self.posX + self.velocity[1] * self.speedF
            deltay = self.posY + self.velocity[0] * self.speedF
        if collisions[0] == 1:
            deltax = self.posX + self.velocity[1] * self.speedF
        if collisions[1] == 1:
            deltay = self.posY + self.velocity[0] * self.speedF
        if collisions[2] == 1:
            deltax = self.posX + self.velocity[1] * self.speedF
        if collisions[3] == 1:
            deltay = self.posY + self.velocity[0] * self.speedF
        if z > 1:
            deltax = self.posX
            deltay = self.posY

        return deltax, deltay

    def checkeatingfood(self, foodlist, canvas):
        z = 0
        for food in foodlist:
            if self.posX + self.sizeF / 2 >= food.posX + food.sizeF / 2 and self.posY + self.sizeF / 2 >= food.posY + food.sizeF / 2 and self.posX - self.sizeF / 2 <= food.posX - food.sizeF / 2 and self.posY - self.sizeF / 2 <= food.posY - food.sizeF / 2:
                canvas.delete(canvas.drawnfood[z])
                food.posX = -1
                food.posY = -1
                self.score += 1
                print self.score
            z += 1

    def checkeatingenemy(self, enemylist, canvas):
        z = 0
        for enemy in enemylist:
            if self.posX + self.sizeF / 2 >= enemy.posX + enemy.sizeF / 2 and self.posY + self.sizeF / 2 >= enemy.posY + enemy.sizeF / 2 and self.posX - self.sizeF / 2 <= enemy.posX - enemy.sizeF / 2 and self.posY - self.sizeF / 2 <= enemy.posY - enemy.sizeF / 2:
                enemy.posX = -1
                enemy.posY = -1
                canvas.delete(canvas.drawnenemy[z])
                self.score -= 1
                print self.score
            z += 1
