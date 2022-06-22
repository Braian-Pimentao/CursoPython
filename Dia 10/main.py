import pygame
import  random

# Inicializar Pygame
pygame.init()

# Establecer tamaño de pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Space Invaders")
icono = pygame.image.load("src/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("src/fondo.jpg")

# Crear player
img_player = pygame.image.load("src/nave.png")
player_x = 368
player_y = 500
player_x_change = 0

# Crear enemigo
img_enemy = pygame.image.load("src/enemigo.png")
enemy_x = random.randint(0,736)
enemy_y = 20
enemy_x_change = 0.6
enemy_y_change = 50

def player(x, y):
    pantalla.blit(img_player, (x,y))

def enemy(x, y):
    pantalla.blit(img_enemy, (x,y))

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

        #Evento flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a \
                    or evento.key == pygame.K_LEFT:
                player_x_change = -0.6
            elif evento.key == pygame.K_d \
                    or evento.key == pygame.K_RIGHT:
                player_x_change = 0.6
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d \
                    or evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modificar movimiento del jugador
    player_x += player_x_change
    # Mantener bordes de pantalla del jugador
    if player_x <= 4:
        player_x = 4
    elif player_x >= 732:
        player_x = 732

    # Modificar movimiento del enemigo
    enemy_x += enemy_x_change
    # Mantener bordes de pantalla del enemigo
    if enemy_x <= 4:
        enemy_x_change = 0.6
        enemy_y += enemy_y_change
    elif enemy_x >= 732:
        enemy_x_change = -0.6
        enemy_y += enemy_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    #Actualizar pantalla
    pygame.display.update()
