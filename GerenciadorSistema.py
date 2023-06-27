import Jogo
import Time
import random

class GerenciadorSistema:
    def __init__(self):
        self.jogadores = []
        self.jogosAmistosos = []

    def adicionarJogador(self, jogador):
        self.jogadores.append(jogador)

    def removerJogador(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)

    def criarJogoAmistoso(self, data, local):
        jogoAmistoso = Jogo(data, local)
        self.jogosAmistosos.append(jogoAmistoso)

    def alocarTimes(self, jogoAmistoso):
        pass

    def exibirJogosAmistosos(self):
        pass
