from elements import Food
from elements import Enemy
from elements import Player
import random
import numpy as np
import cv2


class Game:
    nFoods = 10
    nEnemies = 10
    foods = []
    enemies = []
    size, x, y = 0, 0, 0
    food_reward = 50
    enemy_penalty = 300
    idle_penalty = 5
    steps = 0

    def __init__(self, _canvas, _width, _height):
        self.canvas = _canvas

        self.width = _width
        self.height = _height
        self.oldscore = 0
        self.player = None

    def init_objects(self):
        self.steps = 0
        for enemy in self.enemies:
            self.enemies.remove(enemy)

        for food in self.foods:
            self.foods.remove(food)

        for i in range(self.nFoods):
            while True:
                flag = False
                size = int(self.width * Food.sizeF)
                x = random.uniform(int(size / 2.0)+1, self.width - int(size / 2.0)+1)
                y = random.uniform(int(size / 2.0)+1, self.width - int(size / 2.0)+1)
                for n in self.foods:
                    if abs(x - n.posX) < size+1 and abs(y - n.posY) < size+1:
                        flag = True
                if not flag:
                    break

            self.foods.extend([Food(x, y, self.width)])

        for j in range(self.nEnemies):
            while True:
                flag = False
                size = int(self.width * Enemy.sizeF)
                x = random.uniform(int(size / 2.0)+1, self.width - int(size / 2.0)+1)
                y = random.uniform(int(size / 2.0)+1, self.width - int(size / 2.0)+1)

                for n in self.enemies:
                    if abs(x - n.posX) < size+1 and abs(y - n.posY) < size+1:
                        flag = True
                for n in self.foods:
                    if abs(x - n.posX) < size+1 and abs(y - n.posY) < size+1:
                        flag = True
                if not flag:
                    break

            self.enemies.extend([Enemy(x, y, self.width)])

        while True:
            flag = False
            # size = random.randint(0, 0.1)
            size = int(self.width * Player.sizeF)
            x = random.uniform(int(size / 2.0)+1, self.width - int(size / 2.0)+1)
            y = random.uniform(int(size / 2.0)+1, self.width - int(size / 2.0)+1)
            for n in self.foods:
                if abs(x - n.posX) < size + 1 and abs(y - n.posY) < size + 1:
                    flag = True
            for n in self.enemies:
                if abs(x - n.posX) < size + 1 and abs(y - n.posY) < size + 1:
                    flag = True
            if not flag:
                break

        self.player = Player(x, y, self.width)

    def update(self, action):
        angle = 0
        if action == 0:
            angle = 0
        if action == 1:
            angle = 0.25
        if action == 2:
            angle = 0.5
        if action == 3:
            angle = 0.75
        if action == 4:
            angle = 1
        if action == 5:
            angle = 1.25
        if action == 6:
            angle = 1.5
        if action == 7:
            angle = 1.75

        collisions = self.player.checkcollision(angle)
        deltax, deltay = self.player.moveplayer(angle, collisions)

        self.foods, eaten_food = self.player.checkeatingfood(self.foods)
        self.enemies, eaten_enemy = self.player.checkeatingenemy(self.enemies)

        reward = 0
        if eaten_food:
            reward += self.food_reward
        elif eaten_enemy:
            reward -= self.enemy_penalty
        else:
            reward -= self.idle_penalty

        finished = self.player.checkeatenallfood(self.foods)
        if self.steps >= 10000:
            finished = True

        self.player.posX = deltax
        self.player.posY = deltay

        self.steps += 1
        image = self.get_image()
        imagenp = np.array(image, dtype=np.float32)[:, :, :3]
        cv2.imshow("", np.array(image.resize((720, 720))))
        cv2.waitKey(1)

        return imagenp, reward, finished

    def get_image(self):
        return self.canvas.update_image(self.foods, self.enemies, self.player)

    def reset(self):
        self.x, self.y, self.size = 0, 0, 0
        self.enemies = []
        self.foods = []
        self.init_objects()

        image = self.get_image()
        image = np.asarray(image, dtype=np.float32)[:, :, :3]

        return image



