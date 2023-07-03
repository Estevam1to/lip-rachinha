class Time:
    def __init__(self, nome):
        self.nome = nome
        self.__jogadores = []

    def get_nome(self):
        return self.nome

    def get_jogadores(self):
        return self.__jogadores

    def set_nome(self, nome):
        self.nome = nome

    def adicionar_jogador(self, jogador):
        if jogador.get_posicao() == "Linha":  
            self.__jogadores.append(jogador)
        elif jogador.get_posicao() == "Goleiro":  
            self.__jogadores.append(jogador)

    def remover_jogador(self, jogador):
        if jogador in self.__jogadores:
            self.__jogadores.remove(jogador)

    def calcular_nivel_time(self):
        nivel_time = 0
        for jogador in self.__jogadores:
            nivel_time += jogador.get_nivel_habilidade()
        return nivel_time / len(self.__jogadores)

    def __str__(self):
        return self.nome
