from Animal import Animal

class Pajaro(Animal):
    _totalCreados = 0
    
    def __init__(self, nombre, edad, raza, colorAlas):
        super.__init__(nombre, edad, raza)
        self._colorAlas = colorAlas
        Pajaro._totalCreados += 1

    def setColorAlas(self, colorAlas):
        self._colorAlas = colorAlas

    def getColorAlas(self):
        return self._colorAlas

    def caminar(self):
        return "se mueve poco"

    def correr(self):
        return "no corre"

    def volar(self):
        return "vuela al punto"
    
    @classmethod
    def getTotalCreados(cls):
        return cls._totalCreados