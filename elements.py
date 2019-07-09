import math


class Element(object):
    posX = 0
    posY = 0
    size = 1
    sizeF = 0.1
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
        Element.__init__(self, posX, posY, size, "blue")


class Player(Element):
    velocity = [math.cos(0), math.sin(0)]
    speed = math.sqrt(velocity[0] ** 2 + velocity[1] ** 2)
    sizeF = 0.13
    score = 0
    speedF = 0.2

    def __init__(self, posX, posY, size):
        Element.__init__(self, posX, posY, size, "red")

    def checkcollision(self, angle):
        collisions = [0, 0, 0, 0]
        if not self.posY - (self.size * self.sizeF) / 2 > 0:
            if 0.5 < angle < 1.5:
                collisions[0] = 1
                #print("a")
        if not self.posX + int((self.size * self.sizeF) / 2) < self.size and angle:
            if angle < 1:
                collisions[1] = 1
                #print("b")
        if not self.posY + (self.size * self.sizeF) / 2 < self.size:
            if angle < 0.5 or angle > 1.5:
                collisions[2] = 1
                #print("c")
        if not self.posX - (self.size * self.sizeF) / 2 > 0:
            if angle > 1:
                collisions[3] = 1
                #print("d")
        return collisions

    def moveplayer(self, angle, collisions):
        deltax = self.posX
        deltay = self.posY

        z = 0
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

    def checkeatingfood(self, foodlist):
        z = 0
        eaten_food = False
        for food in foodlist:
            if self.posX + (self.size * self.sizeF) / 2 >= food.posX + (food.sizeF * food.sizeF) / 2 \
                    and self.posY + (self.size * self.sizeF) / 2 >= food.posY + (food.sizeF * food.sizeF) / 2 \
                    and self.posX - (self.size * self.sizeF) / 2 <= food.posX - (food.sizeF * food.sizeF) / 2 \
                    and self.posY - (self.size * self.sizeF) / 2 <= food.posY - (food.sizeF * food.sizeF) / 2:
                foodlist.remove(food)
                self.score += 1
                eaten_food = True
            z += 1
        return [foodlist, eaten_food]

    def checkeatingenemy(self, enemylist):
        z = 0
        eaten_enemy = False
        for enemy in enemylist:
            if self.posX + (self.size * self.sizeF) / 2 >= enemy.posX + (enemy.sizeF * enemy.sizeF) / 2 \
                    and self.posY + (self.size * self.sizeF) / 2 >= enemy.posY + (enemy.sizeF * enemy.sizeF) / 2 \
                    and self.posX - (self.size * self.sizeF) / 2 <= enemy.posX - (enemy.sizeF * enemy.sizeF) / 2 \
                    and self.posY - (self.size * self.sizeF) / 2 <= enemy.posY - (enemy.sizeF * enemy.sizeF) / 2:
                enemylist.remove(enemy)
                self.score -= 1
                eaten_enemy = True
            z += 1
        return [enemylist, eaten_enemy]

    def checkeatenallfood(self, foodlist):
        if len(foodlist) == 0:
            return True
        else:
            return False
