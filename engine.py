from elements import Food
from elements import Enemy
from elements import Player
from field import Field

class GameEnigine:
    player = None
    foods = []
    enemies = []
    field = None
    def __init__(self, player, foods, enemies, field):
        self.player = player
        self.foods = foods
        self.enemies = enemies
        self.field = field

    def update(self, angle):
        collisions = self.player.checkcollision()
        deltax, deltay = self.player.move(angle, self.field, collisions)
        self.player.checkeatingfood(self.foods, self.field)
        self.player.checkeatingenemy(self.enemies, self.field)
        self.player.posX = deltax
        self.player.posY = deltay
        self.field.delete(self.field.drawnplayer)
        self.field.drawplayer(self.player)


