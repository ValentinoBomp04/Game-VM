import pygame

screen = pygame.display.set_mode((1091, 614))
personaje = pygame.image.load('user1.png').convert_alpha()
quit = False
x, y = 0, 0
color_fondo = (200, 200, 200)


while not quit:

    # Atiende los eventos de la aplicacion. Es importante
    # utilizar esta rutina en todo juego, de otro modo la
    # función "pygame.key.get_pressed" no funcionará.
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit = True

    # Realiza los movimientos del personaje con teclado
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 1
    elif keys[pygame.K_RIGHT]:
        x += 1

    if keys[pygame.K_DOWN]:
        y += 1
    elif keys[pygame.K_UP]:
        y -= 1


    # Actualiza la pantalla, imprimiento el personaje y limpiando
    # todo el fondo de color gris.
    screen.fill(color_fondo)
    screen.blit(personaje, (x, y))
    pygame.display.flip()
    pygame.time.wait(10)
