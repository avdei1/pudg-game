#создай игру "Лабиринт"!
from pygame import *

#music
mixer.init()
mixer.music.load("Dota2.mp3")
mixer.music.play()
#не music
font.init()
font = font.SysFont("Arial", 70)
loos = font.render("LOOSEER", True, (170,0,85))
win = font.render("Ты правда сделал это?", True, (232,204,4))

#класс игрока
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#фон
window1 = 700
window2 = 500
window = display.set_mode((window1, window2))
display.set_caption("Pudge runner")
gendolf = transform.scale(image.load("forest.jpg"),(window1, window2))
#управление
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 10
        if keys_pressed[K_s]:
            self.rect.y += 10
        if keys_pressed[K_d]:
            self.rect.x += 10
        if keys_pressed[K_a]:
            self.rect.x -= 10

class Enemy(GameSprite):
    direction = "left"
    def update(self):   
        if self.rect.x <= 300:
            self.direction = "right"
        if self.rect.x >= window1 - 50:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
#стеночки
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#cтеночки видны, бьют       
wall1 = Wall(0,153,102, 100, 100, 100, 20)
wall2 = Wall(0,153,102, 100, 100, 20, 1000)
wall3 = Wall(0,153,102, 280, 100, 20, 300)
wall4 = Wall(0,153,102, 100, 400, 100, 20)
wall5 = Wall(0,153,102, 280, 400, 168, 20)
wall6 = Wall(0,153,102, 400, 0, 20, 200)
wall7 = Wall(0,153,102, 400, 270, 20, 50)
wall8 = Wall(0,153,102, 510, 400, 80, 20)
wall9 = Wall(0,153,102, 510, 270, 20, 50)
wall10 = Wall(0,153,102, 510, 100, 20, 100)
#стеночки невидны и бьют
wallred1 = Wall(255, 64, 0, 448, 419, 62, 1)
wallred2 = Wall(255, 64, 0, 198, 119, 1, 3000)
wallred3 = Wall(255, 64, 0, 448, 419, 1, 100)
wallred4 = Wall(255, 64, 0, 529, 300, 1, 100)
wallred5 = Wall(255, 64, 0, 520, 99, 100, 1)
wallred6 = Wall(255, 64, 0, 620, 199, 100, 1)
wallred7 = Wall(255, 64, 0, 0, 0, 1000, 1)
wallred8 = Wall(255, 64, 0, 0, 0, 1, 1000)
wallred9 = Wall(255, 64, 0, 0, 0, 1000, 1)
wallred10 = Wall(255, 64, 0, 700, 0, 1, 1000)
#стеночки видны, не бьют
wall11 = Wall(0,153,102, 280, 0, 20, 100)
wall22 = Wall(0,153,102, 200, 250, 80, 20)
wall33 = Wall(0,153,102, 510, 0, 20, 100)

#штуки всякие двигающиеся
pudg = Player("Pudg.png", 30, 400, 10)
rosha = Enemy("Roshan_icon.png", 500, 200, 10)
taras = GameSprite("Tarrasque.png", 450, 420, 10)

clock = time.Clock()
FPS = 60

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(gendolf, (0, 0))

        pudg.update()
        rosha.update()
        pudg.reset()
        rosha.reset()
        taras.reset()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()

        wall11.draw_wall()
        wall22.draw_wall()
        wall33.draw_wall()

        if sprite.collide_rect(pudg, taras):
            window.blit(win, (100, 200))
            finish = True
        if sprite.collide_rect(pudg, rosha) or sprite.collide_rect(pudg, wall1) or sprite.collide_rect(pudg, wall2) or sprite.collide_rect(pudg, wall3) or sprite.collide_rect(pudg, wall4) or sprite.collide_rect(pudg, wall5) or sprite.collide_rect(pudg, wall6) or sprite.collide_rect(pudg, wall7) or sprite.collide_rect(pudg, wall8) or sprite.collide_rect(pudg, wall9) or sprite.collide_rect(pudg, wall10) or sprite.collide_rect(pudg, wallred1) or sprite.collide_rect(pudg, wallred2) or sprite.collide_rect(pudg, wallred3) or sprite.collide_rect(pudg, wallred4) or sprite.collide_rect(pudg, wallred5) or sprite.collide_rect(pudg, wallred6) or sprite.collide_rect(pudg, wallred7) or sprite.collide_rect(pudg, wallred8) or sprite.collide_rect(pudg, wallred9) or sprite.collide_rect(pudg, wallred10):
            window.blit(loos, (200, 200))
            finish = True
        
    display.update()

    clock.tick(FPS)
