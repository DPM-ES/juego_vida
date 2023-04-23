"""
    El juego de la vida (con color)
    Version: 1.0
    Proyecto realizado en Python usando la librería pygame
    Autor: DPM_ES
"""
# Importaciones
import pygame
import sys
import numpy as np


# Función que controla qué se pulsa por tecládo y las funciones a realizar
def control_key(key):
    global pause, i_timer, new_game_state, i_color
    # Pausa el juego a pulsar la barra espaciadora
    if key == pygame.K_SPACE:
        pause = not pause

    # Al pulsar f, pone todas las casillas a 1 (vivas)
    if key == pygame.K_f:
        new_game_state = np.full((num_cel_x, num_cel_y, 3), 1)

    # Al pulsar e, pone todas las casillas a 0 (muertas)
    if key == pygame.K_e:
        new_game_state = np.zeros((num_cel_x, num_cel_y, 3))

    # Al pulsar q, cierra la ventana, igual que al cerrar pulsando en la X de cerrar
    if key == pygame.K_q:
        pygame.quit()
        sys.exit()

    # Hace que el juego vaya más despacio
    if key == pygame.K_KP_MINUS:
        if i_timer < 4:
            i_timer += 1

    # Hace que el juego vaya más deprisa
    if key == pygame.K_KP_PLUS:
        if i_timer > 0:
            i_timer -= 1

    # Activa el color rojo
    if key == pygame.K_1:
        i_color = 0

    # Activa el color verde
    if key == pygame.K_2:
        i_color = 1

    # Activa el color azul
    if key == pygame.K_3:
        i_color = 2

    # Activa el color azul
    if key == pygame.K_4:
        i_color = 3


# Función para generar los colores
def color_maker(status):
    return 255 * status[0], 255 * status[1], 255 * status[2]


# Inicialización de los módulos de pygame
pygame.init()

# Colores
c_blak = (0, 0, 0)
c_gray = (128, 128, 128)
c_red = (255, 0, 0)

# Tamño e inicialización de la pantalla del juego
height = width = 1000  # Nota: Se puede cambiar este valor para hacer la pantalla más o menos grande
game_field = pygame.display.set_mode((width + 1, height + 1))  # Nota: añado un pixel para que no se corte la cuadrícula
pygame.display.set_caption("DPM: El juego de la vida a color (v1.0)")
game_field.fill(c_blak)
external_box = [(0, 0), (width, 0), (width, height), (0, height)]

# Número y tamaño de las celdas
num_cel_x = num_cel_y = 50  # Se puede cambiar este valor para hacer tener más o menos casillas
dim_cel_h = height / num_cel_y
dim_cel_w = width / num_cel_x


# Estado de las celdas juego. 1: Vivas; 0: Muertas
game_state = np.zeros((num_cel_x, num_cel_y, 3))

# Controladores de estado del juego
pause = True
timer = [50, 100, 200, 300, 400]
i_timer = 2
i_color = 0  # 0: Rojo; 1: Verde; 2: Azul; 3: Blanco


# Bucle de ejecución
while True:

    # Realizamos una copia para realizar los cambios en cada tiempo y no de manera secuencial
    new_game_state = np.copy(game_state)

    # Reseteamos los colores de la pantalla para poder representar el estado sin solapamientos y
    game_field.fill(c_blak)
    pygame.time.wait(timer[i_timer])

    # Recogemos eventos de teclado y ratón
    for event in pygame.event.get():

        # Evento de plusar en cerrar ventana y acción de cerrar juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Evento de pulsar el teclado, llama la función de control
        if event.type == pygame.KEYDOWN:
            control_key(event.key)

        # Recoge el click izquierdo y pone la casilla en 1
        if pygame.mouse.get_pressed()[0]:
            pos_x, pos_y = pygame.mouse.get_pos()
            cel_x, cel_y = int(np.floor(pos_x / dim_cel_w)), int(np.floor(pos_y / dim_cel_h))
            try:
                if i_color == 3:
                    new_game_state[cel_x, cel_y] = 1
                else:
                    new_game_state[cel_x, cel_y][i_color] = 1
            except IndexError:
                pass

        # Recoge el click derecho y pone la casilla en 0
        if pygame.mouse.get_pressed()[2]:
            pos_x, pos_y = pygame.mouse.get_pos()
            cel_x, cel_y = int(np.floor(pos_x / dim_cel_w)), int(np.floor(pos_y / dim_cel_h))
            try:
                new_game_state[cel_x, cel_y] = 0
            except IndexError:
                pass

    # Bucle de recorrido y dibujo de la pantalla
    for y in range(num_cel_y):
        for x in range(num_cel_x):

            if not pause:

                # Comprobación de los estados vecinos
                # se usa la operación módulo para evitar el error "IndexError" (otorga forma toroidal al mundo).
                n_neigh = game_state[(x - 1) % num_cel_x, (y - 1) % num_cel_y] + \
                          game_state[ x     % num_cel_x,  (y - 1) % num_cel_y] + \
                          game_state[(x + 1) % num_cel_x, (y - 1) % num_cel_y] + \
                          game_state[(x - 1) % num_cel_x,  y      % num_cel_y] + \
                          game_state[(x + 1) % num_cel_x,  y      % num_cel_y] + \
                          game_state[(x - 1) % num_cel_x, (y + 1) % num_cel_y] + \
                          game_state[ x     % num_cel_x,  (y + 1) % num_cel_y] + \
                          game_state[(x + 1) % num_cel_x, (y + 1) % num_cel_y]

                #Reglas del juego de la vida
                for color in range(3):
                    # Regla 1: Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.
                    if game_state[x, y][color] == 1 and (n_neigh[color] < 2 or n_neigh[color] > 3):
                        new_game_state[x, y][color] = 0

                    # Regla 2: Si una célula está muerta y tiene tres vecinas vivas, nace.
                    elif game_state[x, y][color] == 0 and n_neigh[color] == 3:
                        new_game_state[x, y][color] = 1

            # Representación de las cajas que contienen las celdas
            # Se genera dibujando un poligono siguiendo las coordenadas de cada vertice.
            cell_box = [( x  * dim_cel_w,      y  * dim_cel_h),
                        ((x + 1) * dim_cel_w,  y      * dim_cel_h),
                        ((x + 1) * dim_cel_w, (y + 1) * dim_cel_h),
                        ( x      * dim_cel_w, (y + 1) * dim_cel_h)]

            # Dibujamos la celda
            if new_game_state[x, y].any():
                pygame.draw.polygon(game_field, color_maker(new_game_state[x, y]), cell_box, 0)
            pygame.draw.polygon(game_field, c_gray, cell_box, 1)

    # Dibujamos en rojo el contorno cuando el juego está en pausa
    if pause:
        pygame.draw.polygon(game_field, c_red, external_box, 5)

    # Acutualización del estado del juego.
    game_state = np.copy(new_game_state)

    # Acutualización de la pantalla.
    pygame.display.flip()
