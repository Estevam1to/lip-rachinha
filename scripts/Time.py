class Time:
    QUANTIDADE_TIMES = 0

def __init__(self):
    self.__numero = Time.QUANTIDADE_TIMES + 1
    Time.QUANTIDADE_TIMES += 1
    self.__jogadoresLinha = []
    self.__goleiro = None

    def get_numero(self):
        return self.__numero

    def get_jogadoresLinha(self):
        return self.__jogadoresLinha

    def get_goleiro(self):
        return self.__goleiro

    def set_numero(self, numero: int):
        self.__numero = numero

    def set_jogadores_linha(self, jogadoresLinha):
        self.__jogadoresLinha.append(jogadoresLinha)

    def set_goleiro(self, goleiro):
        self.__goleiro = goleiro


    def adicionar_jogador(self, jogador):
        if jogador.posicao == "linha":
            self.__jogadoresLinha.append(jogador)
        elif jogador.posicao == "goleiro":
            self.__goleiro = jogador

    def remover_jogador(self, jogador):
        if jogador in self.__jogadoresLinha:
            self.__jogadoresLinha.remove(jogador)
        elif self.__goleiro == jogador:
            self.__goleiro = None

    def calcular_nivel_time(self):
        nivel_time = 0
        for jogador in self.__jogadoresLinha:
            nivel_time += jogador.nivel_habilidade
        if self.__goleiro is not None:
            nivel_time += self.__goleiro.nivel_habilidade
        return nivel_time / len(self.__jogadoresLinha)
