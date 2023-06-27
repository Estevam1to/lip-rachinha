class Time:
    def __init__(self, numero):
        self.numero = numero
        self.jogadoresLinha = []
        self.goleiro = None

    def getNumero(self):
        return self.numero
    
    def getJogadoresLinha(self):
        return self.jogadoresLinha
    
    def getGoleiro(self):
        return self.goleiro
    
    def setNumero(self, numero):
        self.numero = numero
    
    def setJogadoresLinha(self, jogadoresLinha):
        self.jogadoresLinha = jogadoresLinha
    
    def setGoleiro(self, goleiro):
        self.goleiro = goleiro
  
    def adicionarJogador(self, jogador):
        if jogador.getPosicao() == "linha":
            self.jogadoresLinha.append(jogador)
        elif jogador.getPosicao() == "goleiro":
            self.goleiro = jogador
    
    def removerJogador(self, jogador):
        if jogador in self.jogadoresLinha:
            self.jogadoresLinha.remove(jogador)
        elif self.goleiro == jogador:
            self.goleiro = None

    def calcularNivelTime(self):
        pontuacaoTotal = 0
        numJogadores = len(self.jogadoresLinha)
        if self.goleiro is not None:
            numJogadores += 1
            pontuacaoTotal += self.goleiro.getPontuacao()
        for jogador in self.jogadoresLinha:
            pontuacaoTotal += jogador.getPontuacao()
        return pontuacaoTotal / numJogadores if numJogadores > 0 else 0
