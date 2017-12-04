from LDEngine.app.sprites.bullet import Bullet

from LDEngine.app.sprites.enemy.enemy import Enemy
from LDEngine.app.scene.platformScreen.collisionPlayerPlatform import *

import os

class FireBullet(Bullet):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('Sprite', 'bullet.png'))

        self.name = "bullet"

        image1 = pygame.image.load(os.path.join('Sprite', 'bullet.png'))
        image2 = pygame.image.load(os.path.join('Sprite', 'bullet_2.png'))

        if direction == RIGHT:
            image1 = pygame.transform.flip(image1, True, False)
            image2 = pygame.transform.flip(image2, True, False)
        elif direction == LEFT:
            pass
        elif direction == UP:
            image1 = pygame.transform.rotate(image1, 270)
            image2 = pygame.transform.rotate(image2, 270)
        elif direction == DOWN:
            image1 = pygame.transform.rotate(image1, 90)
            image2 = pygame.transform.rotate(image2, 90)

        self.frames = [image1, image2]
        self.image = image1

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height / 2

        if direction == RIGHT:
            self.speedx = 6
            self.speedy = 0
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -6
            self.speedy = 0
            self.rect.x = x - self.rect.width
        elif direction == UP:
            self.speedx = 0
            self.speedy = -6
            self.rect.x = x
            self.rect.y = y
        elif direction == DOWN:
            self.speedx = 0
            self.speedy = 6
            self.rect.x = x
            self.rect.y = y

        self.animation = self.stand_animation(self.frames,6)

        self.friendly = friendly
