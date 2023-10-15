class Deportista:

    def __init__(self, deporte="futbol", anosPracticando=None):
        self._deporte=deporte
        self._anosPracticando=anosPracticando

    def getDeporte(self):
        return self._deporte
    def setDeporte(self,deporte):
        self._deporte=deporte

    def getAnosPracticando(self):
        return self._anosPracticando
    def setAnosPracticando(self,anosPracticando):
        self._anosPracticando=anosPracticando
    