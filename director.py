import pygame, random ,sys, time, base ,nave, asteroide

ancho = 600
alto = 450
cant_aster = 7
grupo_aster = []
bang = True
grados = 0

class Director(base.Escena):
    def __init__(self, titulo = "", res = (ancho,alto)):
        pygame.init()
        self.pantalla = pygame.display.set_mode(res)
        pygame.display.set_caption(titulo)
        self.reloj = pygame.time.Clock()
        self.escena = None
        self.escenas = {}

    def ejecutar(self, escena_inicial, fps = 10):
        self.escena = self.escenas[escena_inicial]
        jugando = True
        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    jugando = False
            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self.pantalla)

            self.elegirEscena(self.escena.proximaEscena)
            if jugando:
                jugando = self.escena.jugando
            pygame.display.flip()
        time.sleep(3)
    
    def elegirEscena(self, proximaEscena):
        if proximaEscena:
            if proximaEscena not in self.escenas:
                self.agregarEscena(proximaEscena)
            self.escena = self.escenas[proximaEscena]
    
    def agregarEscena(self, escena):
        escenaClase = 'Escena'+escena
        escenaObj = globals()[escenaClase]
        self.escenas[escena] = escenaObj()

class EscenaNivel1(base.Escena):
    def __init__(self):
        base.Escena.__init__(self)

        self.jugador = nave.Nave()
        for x in range(cant_aster):
            self.aster = asteroide.Asteroide()
            grupo_aster.append(self.aster)

        pygame.key.set_repeat(30)
    
    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                self.jugador.update(evento)
    
    #def actualizar(self):
    def dibujar(self, pantalla):
        grados = 0
        fondo = pygame.image.load('images/fondo.jpg').convert()
        pantalla.blit(fondo,(0,0))            
        pantalla.blit(self.jugador.image, self.jugador.rect)
        for x in grupo_aster:
            pantalla.blit(x.image, x.rect)
            grados += 6
            x.rect.x -= 5
            if x.rect.x < 0:
                    x.rect.x = ancho - 80
                    x.rect.y =  random.randint(1, 400)
            if grados > 360:
                grados = 0            