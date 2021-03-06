import pygame, random
WIDTH = 1091
HEIGHT = 614
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init() 
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shooter")
clock = pygame.time.Clock()
fondo = pygame.image.load("fondo.png").convert()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  pygame.image.load("milico.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.rect.bottom = HEIGHT  - 10
        self.rect.top = HEIGHT  + 10
        self.speed_x = 0
        self.speed_y = 0
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -10
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 10
        if keystate[pygame.K_UP]:
            self.speed_y = -10
        if keystate[pygame.K_DOWN]:
            self.speed_y = 10
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
        self.rect.y += self.speed_y
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    def shoot(self):
        bala == Bala(self.rect.centery, self.rect.right)
        all_sprites.add(balas)
        balas.add(Bala)
            
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bala.png").converrt()
        self.image.self_colorkey(WHITE)
        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.centerx = x
        self.speed_x = 10
    def update():
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.kill()
        
    
all_sprites = pygame.sprite.Group()
balas = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True
while running: 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoo
        
            
    all_sprites.update()
    screen.blit(fondo, [0, 0])
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()