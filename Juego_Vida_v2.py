"""
    El juego de la vida
    Version: 2.0
    Proyecto realizado en Python usando la librería pygame
    Autor: DPM_ES
"""
# Importaciones
import pygame
import sys
import numpy as np


# Función que controla qué se pulsa por tecládo y las funciones a realizar
def control_key(key):
    global pause, i_timer, timer, new_game_state

    # Pausa el juego a pulsar la barra espaciadora
    if key == pygame.K_SPACE:
        pause = not pause

    # Al pulsar f, pone todas las casillas a 1 (vivas)
    if key == pygame.K_f:
        new_game_state = np.full((num_cel_x, num_cel_y), 1)

    # Al pulsar e, pone todas las casillas a 0 (muertas)
    if key == pygame.K_e:
        new_game_state = np.zeros((num_cel_x, num_cel_y))

    # Al pulsar q, cierra la ventana, igual que al cerrar pulsando en la X de cerrar
    if key == pygame.K_q:
        pygame.quit()
        sys.exit()

    # Hace que el juego vaya más despacio
    if key == pygame.K_KP_PLUS:
        if i_timer < len(timer) - 1:
            i_timer += 1

    # Hace que el juego vaya más deprisa
    if key == pygame.K_KP_MINUS:
        if i_timer > 0:
            i_timer -= 1


# Función encargada de ejecutar las acciones de los eventos
def event_control(event):
    # Evento de plusar en cerrar ventana y acción de cerrar juego
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # Evento de pulsar el teclado, llama la función de control
    if event.type == pygame.KEYDOWN:
        control_key(event.key)


# Función que dibuja los cuadros de información
def draw_info():
    global cells_alive

    # Dibujamos en rojo el contorno cuando el juego está en pausa
    if pause:
        pygame.draw.polygon(game_field, c_red, external_box, 5)

    # Actualizamos el número de células vivas
    cells_alive = np.count_nonzero(game_state)

    # Crear las imágenes de texto
    time_text = font_times.render("Tiempo: {}".format(n_times), True, c_green)
    cell_text = font_cells.render("Células: {}".format(cells_alive), True, c_green)
    vel_text = font_vel.render("Velocidad: {}".format(i_timer + 1), True, c_green)

    # Dibujar las imágenes de texto y botón en la pantalla
    game_field.blit(time_text, pos_time)
    game_field.blit(cell_text, pos_cells)
    game_field.blit(vel_text, pos_vel)


# Función que dibuja el universo del juego
def draw_field():
    global game_state

    # Bucle de recorrido y dibujo de la pantalla
    for y in range(num_cel_y):
        for x in range(num_cel_x):

            if not pause:

                # Comprobación de los estados vecinos
                # se usa la operación módulo para evitar el error "IndexError" (otorga forma toroidal al mundo).
                n_neigh = game_state[(x - 1) % num_cel_x, (y - 1) % num_cel_y] + \
                          game_state[x % num_cel_x, (y - 1) % num_cel_y] + \
                          game_state[(x + 1) % num_cel_x, (y - 1) % num_cel_y] + \
                          game_state[(x - 1) % num_cel_x, y % num_cel_y] + \
                          game_state[(x + 1) % num_cel_x, y % num_cel_y] + \
                          game_state[(x - 1) % num_cel_x, (y + 1) % num_cel_y] + \
                          game_state[x % num_cel_x, (y + 1) % num_cel_y] + \
                          game_state[(x + 1) % num_cel_x, (y + 1) % num_cel_y]

                # Reglas del juego de la vida

                # Regla 1: Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.
                if game_state[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_game_state[x, y] = 0

                # Regla 2: Si una célula está muerta y tiene tres vecinas vivas, nace.
                elif game_state[x, y] == 0 and n_neigh == 3:
                    new_game_state[x, y] = 1

            # Representación de las cajas que contienen las celdas
            # Se genera dibujando un poligono siguiendo las coordenadas de cada vertice.
            cell_box = [(x * dim_cel_w + frame_margin, y * dim_cel_h + info_field_height),
                        ((x + 1) * dim_cel_w + frame_margin, y * dim_cel_h + info_field_height),
                        ((x + 1) * dim_cel_w + frame_margin, (y + 1) * dim_cel_h + info_field_height),
                        (x * dim_cel_w + frame_margin, (y + 1) * dim_cel_h + info_field_height)]

            # Dibujamos la celda
            if new_game_state[x, y]:
                pygame.draw.polygon(game_field, c_green, cell_box, 0)
            pygame.draw.polygon(game_field, c_ggray, cell_box, 1)

    # Acutualización del estado del juego.
    game_state = np.copy(new_game_state)


# Inicialización de los módulos de pygame
pygame.init()

# Colores
c_blak = (0, 0, 0)
c_white = (255, 255, 255)
c_green = (0, 255, 0)
c_ggray = (100, 200, 100)
c_red = (255, 0, 0)

# Tamño e inicialización de la pantalla del juego
height = width = 1000  # Nota: Se puede cambiar este valor para hacer la pantalla más o menos grande
info_field_height = 50
frame_margin = 10
game_field = pygame.display.set_mode((width + frame_margin * 2, height + info_field_height + frame_margin))
pygame.display.set_caption("DPM: El juego de la vida (v2.0)")
game_field.fill(c_blak)
external_box = [(frame_margin - 3, info_field_height - 3),
                (width + frame_margin + 3, info_field_height - 3),
                (width + frame_margin + 3, height + info_field_height + 3),
                (frame_margin - 3, height + info_field_height + 3)]

# Número y tamaño de las celdas
num_cel_x = num_cel_y = 50  # Se puede cambiar este valor para hacer tener más o menos casillas
dim_cel_h = height / num_cel_y
dim_cel_w = width / num_cel_x


# Estado de las celdas juego. 1: Vivas; 0: Muertas
game_state = np.zeros((num_cel_x, num_cel_y))

# Controladores de estado del juego
pause = True
timer = [200, 100, 50, 10, 1]
i_timer = 2
n_times = 0
cells_alive = 0

# Definir las fuentes y tamaños de texto
font_times = pygame.font.Font(None, 36)
font_cells = pygame.font.Font(None, 36)
font_vel = pygame.font.Font(None, 36)

# Definir las posiciones de texto y botón
pos_time = (500 + frame_margin, 15)
pos_cells = (300 + frame_margin, 15)
pos_vel  = (100 + frame_margin, 15)


# Bucle de ejecución
while True:

    # Realizamos una copia para realizar los cambios en cada tiempo y no de manera secuencial
    new_game_state = np.copy(game_state)

    # Actualizamos el contador
    if not pause:
        n_times += 1

    # Reseteamos los colores de la pantalla para poder representar el estado sin solapamientos y
    game_field.fill(c_blak)
    pygame.time.wait(timer[i_timer])

    # Recogemos eventos de teclado y ratón
    for event in pygame.event.get():
        event_control(event)

        # Nota: he decidido no mandar las acciones del ratón para que se pueda dibujar con el ratón
        # Recoge el click derecho y revive la célula
        if pygame.mouse.get_pressed()[0]:
            pos_x, pos_y = pygame.mouse.get_pos()
            pos_x -= frame_margin
            pos_y -= info_field_height
            cel_x, cel_y = int(np.floor(pos_x / dim_cel_w)), int(np.floor(pos_y / dim_cel_h))
            try:
                new_game_state[cel_x, cel_y] = 1
            except IndexError:
                pass

        # Recoge el click derecho y mata la célula
        if pygame.mouse.get_pressed()[2]:
            pos_x, pos_y = pygame.mouse.get_pos()
            pos_x -= frame_margin
            pos_y -= info_field_height
            cel_x, cel_y = int(np.floor(pos_x / dim_cel_w)), int(np.floor(pos_y / dim_cel_h))
            try:
                new_game_state[cel_x, cel_y] = 0
            except IndexError:
                pass

    # Dibuja el universo
    draw_field()

    # Dibuja los campos de información
    draw_info()

    # Acutualización de la pantalla.
    pygame.display.flip()
