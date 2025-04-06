from pygame import *
# from random import randint
# from time import time as timer

FPS = 60
game = True
# finish = False
clock = time.Clock()

window = display.set_mode((700, 500))
display.set_caption("ping-pong")

speed_x = 5
speed_y = 5

score_p1 = 0
score_p2 = 0

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

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerTwo(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 410:
            self.rect.y += self.speed
        window.blit(self.image, (self.rect.x, self.rect.y))

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


pong = PlayerOne('pling.png',625,250,5,100,20)
ping = PlayerTwo('pling.png',50,250,5,100,20)
ball = GameSprite('ballin.png',300,250,2,50,50)

background = transform.scale(image.load("blue.png"),(700,500))

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))
    ping.update()
    pong.update()
    ball.reset()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1
    if ball.rect.x > 650:
        speed_x *= -1
        score_p2 += 1
    if ball.rect.x < 0:
        speed_x *= -1
        score_p1 += 1
    if ball.rect.colliderect(ping.rect):
        speed_x *= -1
        
    if ball.rect.colliderect(pong.rect):
        speed_x *= -1

    clock.tick(FPS)
    display.update()