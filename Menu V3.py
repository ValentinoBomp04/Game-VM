
import pygame, sys, pygame.freetype
 

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Shooter')
dimensiones = (720, 312)
screen = pygame.display.set_mode(dimensiones)

font = pygame.font.SysFont("Courier", 30)

"""fondo = pygame.image.load("fondo_menu.jpg").convert()"""
def draw_text(text, font, color, surface, x, y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0, 0, 0))
        """screen.blit(fondo, (0, 0))"""
        draw_text('Menu Principal', font, (255, 255, 255), screen, 250, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 150, 50)
        button_2 = pygame.Rect(50, 155, 150, 50)
        button_3 = pygame.Rect(30, 250, 150, 30)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
		
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        
        draw_text('PLAY', font, (255, 255, 255), screen, 90, 100)
        draw_text('OPTIONS', font, (255, 255, 255), screen, 75, 160)
        draw_text('QUIT', font, (255, 255, 255), screen, 50, 250)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
