import pygame

pygame.init()

hecho = False
rayo = False
reloj = pygame.time.Clock()
x, y = 0, 0

dimensiones = (1091, 614)

pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("My Game VM")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR_FONDO = (200, 200, 200)
user1 = pygame.image.load('user1.png').convert()
user2 = pygame.image.load('user2.png').convert()
fondo = pygame.image.load('fondo.png').convert()
nave = pygame.image.load('user1.png').convert()
nave.set_colorkey(NEGRO)

personaje = nave

pos = pygame.mouse.get_pos()

while not hecho:
     # Atiende los eventos de la aplicacion. Es importante
    # utilizar esta rutina en todo juego, de otro modo la
    # función "pygame.key.get_pressed" no funcionará.
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit = True

    # Realiza los movimientos del personaje con teclado
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 2
    elif keys[pygame.K_RIGHT]:
        x += 2

    if keys[pygame.K_DOWN]:
        y += 2
    elif keys[pygame.K_UP]:
        y -= 2


    # Actualiza la pantalla, imprimiento el personaje y limpiando
    # todo el fondo de color gris.
    pantalla.fill(COLOR_FONDO)
    pantalla.blit(personaje, (x, y))
    pygame.display.flip()
    pygame.time.wait(0)

pygame.quit()
