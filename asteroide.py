import pygame, random



class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ast = pygame.image.load('images/asteroide.png')
        self.image = self.ast.subsurface(self.ast.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = ((random.randint(350,520 ), random.randint(1,350)))
    
    def movimiento(self):
        rotar = pygame.transform.rotate(self.image, self.grados)
        rect = rotar.get_rect()
        self.rect.center = rect.center
        self.grados += 10
        if self.grados > 360:
            self.grados = 0