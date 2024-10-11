from Animal import Animal

class Perro(Animal):
    _totalCreados = 0
    
    def __init__(self, nombre, edad, raza, pelaje):
        super.__init__(nombre, edad, raza)
        self._pelaje = pelaje
        Perro._totalCreados += 1
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def getPelaje(self):
        return self._pelaje
    
    def caminar():
        return "camina muchos pasos"
    
    def correr():
        return "corre al punto"
    
    def ruido():
        print("guau")
    
    @classmethod
    def getTotalCreados(cls):
        return cls._totalCreados