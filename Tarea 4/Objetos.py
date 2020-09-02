class Objetos:

    def __init__(self, nombre, edad, activo, saldo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        self.saldo = saldo

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self,edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setActivo(self,activo):
        self.activo = activo

    def isActivo(self):
        return self.activo

    def setSaldo(self,saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo