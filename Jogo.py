class Jogo:
    def __init__(self, data, local):
        self.data = data
        self.local = local
        self.times = []
        self.placar = None

    def getData(self):
        return self.data
    
    def getLocal(self):
        return self.local
    
    def getTimes(self):
        return self.times
    
    def getPlacar(self):
        return self.placar
    
    def setData(self, data):
        self.data = data
    
    def setLocal(self, local):
        self.local = local
    
    def setTimes(self, times):
        self.times = times
    
    def setPlacar(self, placar):
        self.placar = placar
    
    def adicionarTime(self, time):
        self.times.append(time)
    
    def removerTime(self, time):
        if time in self.times:
            self.times.remove(time)
    
    def definirPlacar(self, placar):
        self.placar = placar
