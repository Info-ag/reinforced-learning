from PIL import Image, ImageDraw


class Field:
    height = 0
    width = 0

    fieldImage = None

    def __init__(self,  width, height):
        self.height = height
        self.width = width
        self.fieldImage = Image.new('RGB', (self.width, self.height), (255, 255, 255))

    def update_image(self, foodlist, enemylist, player):
        self.fieldImage = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        self.drawfoods(foodlist)
        self.drawenemies(enemylist)
        self.drawplayer(player)
        return self.fieldImage

    def drawfoods(self, foodlist):
        for food in foodlist:
            size = food.size
            x0 = food.posX - (int(0.5 * food.sizeF * size))
            y0 = food.posY - (int(0.5 * food.sizeF * size))
            x1 = x0 + (int(0.5 * food.sizeF * size))
            y1 = y0 + (int(0.5 * food.sizeF * size))
            draw = ImageDraw.Draw(self.fieldImage)
            draw.rectangle([x0, y0, x1, y1], fill=food.color)
            del draw

    def drawenemies(self, enemylist):
        for enemy in enemylist:
            size = enemy.size
            x0 = enemy.posX - (int(0.5 * enemy.sizeF * size))
            y0 = enemy.posY - (int(0.5 * enemy.sizeF * size))
            x1 = x0 + (int(0.5 * enemy.sizeF * size))
            y1 = y0 + (int(0.5 * enemy.sizeF * size))
            draw = ImageDraw.Draw(self.fieldImage)
            draw.rectangle([x0, y0, x1, y1], fill=enemy.color)
            del draw

    def drawplayer(self, player):
        size = player.size
        x0 = player.posX - (int(0.5 * player.sizeF * size))
        y0 = player.posY - (int(0.5 * player.sizeF * size))
        x1 = x0 + (int(0.5 * player.sizeF * size))
        y1 = y0 + (int(0.5 * player.sizeF * size))
        draw = ImageDraw.Draw(self.fieldImage)
        draw.rectangle([x0, y0, x1, y1], fill=player.color)
        del draw
