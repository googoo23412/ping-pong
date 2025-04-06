from pygame import *
# from random import randint
# from time import time as timer

FPS = 60
game = True
# finish = False
clock = time.Clock()

window = display.set_mode((700, 500))
display.set_caption("ping-pong")


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_height,player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_width
        self.height = player_height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerOne(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y < 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y > 490:
            self.rect.y += self.speed

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(10,590)
#             lost = lost + 1

# class Asteroid(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(10,590)

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < 0:
#             self.kill() 

ping = PlayerOne('pling.png',50,250,3,100,20)
pong = GameSprite('pling.png',625,250,5.5,100,20)
ball = GameSprite('ballin.png',300,250,2,50,50)

background = transform.scale(image.load("blue.png"),(700,500))

while game == True:

    ping.reset()
    pong.reset()
    ball.reset()

    clock.tick(FPS)
    display.update()