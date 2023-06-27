class Jogador:
    def __init__(self, nome, pontuacao, posicao):
        self.nome = nome
        self.pontuacao = pontuacao
        self.posicao = posicao
    
    def getNome(self):
        return self.nome
       
    def getPontuacao(self):
        return self.pontuacao
    
    def getPosicao(self):
        return self.posicao
    
    def setNome(self, nome):
        self.nome = nome
    
    def setPontuacao(self, pontuacao):
        self.pontuacao = pontuacao
    
    def setPosicao(self, posicao):
        self.posicao = posicao
