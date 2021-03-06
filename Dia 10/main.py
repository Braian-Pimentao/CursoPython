import pygame
import random
import math
from objects_game import *

# Inicializar Pygame
pygame.init()

# Establecer tamaño de pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("src/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("src/fondo.jpg")

# Crear jugador
player = Player(pantalla)
# Pintar jugador
player.paint_player()

# Crear Enemigo
enemy = Enemy(pantalla)

# Pintar enemigo
enemy.paint_enemy()

# Crear bala
bullet = Bullet(pantalla)

#score
score = 0


# Detectar colisiones
def calcular_distancia(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Cambiar fondo pantalla (relleno)
    pantalla.blit(fondo,(0,0))

    # Iterar eventos
    for evento in pygame.event.get():
        #Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a \
                    or evento.key == pygame.K_LEFT:
                player.x_change = -0.3
            if evento.key == pygame.K_d \
                    or evento.key == pygame.K_RIGHT:
                player.x_change = 0.3
            if evento.key == pygame.K_SPACE:
                if not bullet.visible:
                    bullet.x = player.x
                bullet.disparar()
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d \
                    or evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player.x_change = 0


    # Modificar movimiento del jugador
    player.x += player.x_change
    # Mantener bordes de pantalla del jugador
    if player.x <= 4:
        player.x = 4
    elif player.x >= 732:
        player.x = 732

    enemy.move_enemy()

    # Movimiento bala
    bullet.move_bullet()

    player.paint_player()
    enemy.paint_enemy()

    #Colision
    colision = calcular_distancia(enemy.x,enemy.y,bullet.x,bullet.y)
    if colision:
        bullet.y = 500
        bullet.visible = False
        score += 1
        print(score)
        enemy.x = random.randint(0, 736)
        enemy.y = 20

    #Actualizar pantalla
    pygame.display.update()
