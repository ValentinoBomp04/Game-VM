import pygame

pygame.init()

pantalla = pygame.display.set_mode([824, 584])

BLANCO = (255, 255, 255)
GRIS = (255, 255, 255)

auto = pygame.image.load('auto.jpg').convert()
auto.set_colorkey(BLANCO)
auto_izq = pygame.image.load('auto-izq.jpg').convert()
auto_izq.set_colorkey(BLANCO)
auto_der = pygame.image.load('auto-der.jpg').convert()
auto_der.set_colorkey(BLANCO)
imagen_de_fondo = pygame.image.load("fondo.jpg").convert()


x = 0
offset_x = 0
offset_x_obj = 0
y = 0
offset_y = 0

reloj = pygame.time.Clock()

hecho = False
personaje = auto
pos = [380, 450]

while not hecho:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			hecho = True
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_RIGHT:
				offset_x = -1
				offset_x_obj = -2
				personaje = auto_der
			if evento.key == pygame.K_LEFT:
				offset_x = 1
				offset_x_obj = 2
				personaje = auto_izq
			if evento.key == pygame.K_DOWN:
				offset_y = 0
			if evento.key == pygame.K_UP:
				offset_y = 0
		if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_RIGHT:
			   offset_x = 0
			   offset_x_obj = 0
			if evento.key == pygame.K_LEFT:
				offset_x = 0
				offset_x_obj = 0
	x += offset_x
	y += offset_y
	x += offset_x_obj
	
	offset = pos

    # 
    
	pantalla.blit(imagen_de_fondo, [x, y])
	pantalla.blit(personaje, offset)
   
	pygame.display.flip()
	reloj.tick(50)

pygame.quit()
