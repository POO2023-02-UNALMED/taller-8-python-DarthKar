from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas=[]

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, goles, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol", añosPracticando)
        self._golesMarcados = goles
        self._tarjerasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,goles):
        self._golesMarcados = goles
    
    def getTarjetasRojas(self):
        return self._tarjerasRojas
    def setTarjetasRojas(self,tar):
        self._tarjetasRojas = tar

    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self, pie):
        self._piernaHabil=pie

    def __str__(self):
        return "Mi nombre es "+self._nombre+" soy profesional en el deporte "+self._deporte+" Tengo "+str(self._edad)+" años de edad y llevo "+str(self._añosPracticando)+" años en el deporte"
    