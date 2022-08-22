import pygame
import random


class Player:
    img_player = pygame.image.load("src/nave.png")

    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.x = 368
        self.y = 500
        self.x_change = 0

    def paint_player(self):
        self.pantalla.blit(self.img_player, (self.x, self.y))


class Enemy:
    img_enemy = pygame.image.load("src/enemigo.png")

    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.x = random.randint(0, 736)
        self.y = 20
        self.x_change = 0.3
        self.y_change = 50

    def paint_enemy(self):
        self.pantalla.blit(self.img_enemy, (self.x, self.y))

    def move_enemy(self):
        # Modificar movimiento del enemigo
        if self.y > 250:
            self.y = 1000
        self.x += self.x_change
        # Mantener bordes de pantalla del enemigo
        if self.x <= 4:
            self.x_change = 0.3
            self.y += self.y_change
        elif self.x >= 732:
            self.x_change = -0.3
            self.y += self.y_change


class Bullet:
    img_bala = pygame.image.load("src/bala.png")

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.x = 0
        self.y = 500
        self.y_change = 0.6
        self.visible = False

    def disparar(self):
        self.visible = True
        self.pantalla.blit(self.img_bala, (self.x + 16, self.y + 10))

    def move_bullet(self):
        if self.y <= -64:
            self.y = 500
            self.visible = False

        if self.visible:
            self.disparar()
            self.y -= self.y_change

class Score:
    score = 0
    text_x = 10
    text_y = 10

    def __init__(self, pantalla,font):
        self.pantalla = pantalla
        self.x = 10
        self.font = font
        self.y = 10

    def mostrar_puntaje(self):
        text = self.font.render(f"{self.score}", True, (255, 255, 255))
        self.pantalla.blit(text, (self.x, self.y))
