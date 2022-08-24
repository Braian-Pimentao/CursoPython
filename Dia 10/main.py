import pygame
import random
import math
from objects_game import *
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Establecer tamaño de pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("src/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("src/fondo.jpg")

# Agregar musica
mixer.music.load("src/musicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Crear jugador
player = Player(pantalla)

# Pintar jugador
player.paint_player()

# Crear Enemigos
enemies = []
enemy_count = 8

for e in range(enemy_count):
    enemies.append(Enemy(pantalla))
    enemies[e].paint_enemy()



# Crear bala
bullet = Bullet(pantalla)

# Crear puntaje
font = pygame.font.Font('freesansbold.ttf', 32)
score = Score(pantalla, font)

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
                disparo = mixer.Sound("src/disparo.mp3")
                disparo.set_volume(0.5)
                disparo.play()
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

    for e in range(enemy_count):
        enemies[e].move_enemy()

        colision = calcular_distancia(enemies[e].x, enemies[e].y, bullet.x, bullet.y)
        if colision:
            golpe = mixer.Sound("src/golpe.mp3")
            golpe.set_volume(0.3)
            bullet.y = 500
            bullet.visible = False
            score += 1
            print(score)
            enemies[e].x = random.randint(0, 736)
            enemies[e].y = 20
            enemy_count -=1

        enemies[e].paint_enemy()

    # Movimiento bala
    bullet.move_bullet()

    player.paint_player()


    score.mostrar_puntaje()

    #Actualizar pantalla
    pygame.display.update()
