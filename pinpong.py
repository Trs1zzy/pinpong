from pygame import *
 
#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
speed_x = 3
speed_y = 3
window = display.set_mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
 


class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

       #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



    
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 105:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 105:
            self.rect.y += self.speed




raketka1 = Player('nonavw.png', 580, 200, 25, 100, 5) 


ball = GameSprite('pngwing.com.png', 290, 200, 60, 60, 5)


raketka2 = Player('nonavw.png', 0, 200, 25, 100, 5)














while game:
    for e in event.get():
        if e.type == QUIT:
            game = False  
    if finish != True:
        window.fill(back)
        raketka1.update_l()
        raketka2.update_r()
        raketka2.reset()
        raketka1.reset()
        ball.reset()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(raketka1, ball) or sprite.collide_rect(raketka2, ball):
            speed_x *=  -1

    display.update()
    clock.tick(FPS)
