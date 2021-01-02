import director
alto = 400
ancho = 600

direct = director.Director('Nave Alien', (ancho,alto))
direct.agregarEscena('Nivel1')
direct.ejecutar('Nivel1')