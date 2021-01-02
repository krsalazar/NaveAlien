import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/nave.png')
        self.misil = pygame.image.load('images/misil.png')
        self.rect = self.image.get_rect()
        self.misilrect = self.misil.get_rect()
        self.rect.midbottom = (90,225)
        self.speed = [0,0]
        print(self.rect)
        
    def update(self, evento):
#Para asegurarme que el jugador no se salga de la pantalla debo saber exactamente las dimensiones de la misma
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < 600:
            self.speed = [5,0]
        elif evento.key == pygame.K_UP and self.rect.top > 0 :
            self.speed = [0,-5]
        elif evento.key == pygame.K_DOWN and self.rect.bottom < 399:
            self.speed = [0,5]
        elif evento.key == pygame.K_SPACE:
            print(self.rect)
        else:
            self.speed = [0, 0]

        self.rect.move_ip(self.speed)