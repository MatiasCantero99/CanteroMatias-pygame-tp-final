from Enemy_laberinto_class import Enemy

class Object(Enemy):
    def __init__(self, x, y, escalar, pantalla,delay,nombre,width,hight):
        super().__init__(x, y, escalar, pantalla,delay,nombre,width,hight)