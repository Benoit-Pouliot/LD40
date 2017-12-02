from LDEngine.app.sprites.bullet import Bullet

from LDEngine.app.sprites.enemy.enemy import Enemy
from LDEngine.app.scene.platformScreen.collisionPlayerPlatform import *

import os

class FireBullet(Bullet):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('LDEngine\img', 'biere32x32.png'))

        self.name = "bullet"

        image1 = pygame.image.load(os.path.join('Sprite', 'bullet.png'))
        image2 = pygame.image.load(os.path.join('Sprite', 'bullet_2.png'))
        self.frames = [image1,image2]
        self.image = self.frames[0]

        self.animation = self.stand_animation(self.frames,6)

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height / 2

        if direction == RIGHT:
            self.speedx = 10
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.friendly = friendly
