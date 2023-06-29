from Time import Time
from Jogador import Jogador
 
class Racha:
    def __init__(self, data, local, quantidade_jogadores, quantidade_times):
        if quantidade_jogadores < 0:
            raise ValueError("A quantidade de jogadores deve ser um valor não negativo.")
        
        if quantidade_times < 0:
            raise ValueError("A quantidade de times deve ser um valor não negativo.")
        
        self.__data = data
        self.__local = local
        self.__quantidade_jogadores = quantidade_jogadores
        self.__quantidade_times = quantidade_times
        self.__times = []
        self.__placar = None

    def criar_time(self):
        time = Time()
        self.__times.append(time)

    def remover_time(self, time):
        if time in self.__times:
            self.__times.remove(time)
        else:
            raise ValueError("O time não está presente na lista de times.")

    def adicionar_jogador_no_time(self, jogador):
        if not isinstance(jogador, Jogador):
            raise ValueError("O objeto passado não é um jogador válido.")
        
        for _ in range(jogador.quantidade):
            self.__times.append(jogador)

    def definir_placar(self, gols_time1, gols_time2):
        self.__placar = (gols_time1, gols_time2)

    def get_data(self):
        return self.__data

    def get_quantidade_jogadores(self):
        return self.__quantidade_jogadores

    def set_data(self, data):
        self.__data = data

    def get_local(self):
        return self.__local

    def set_local(self, local):
        self.__local = local

    def get_times(self):
        return self.__times

    def set_times(self, times):
        self.__times = times

    def get_placar(self):
        return self.__placar

    def set_placar(self, gols_time1, gols_time2):
        self.__placar = (gols_time1, gols_time2)

    def distribuir_jogadores(self):
        matriz_jogadores = []
        for time in self.__times:
            matriz_jogadores.append(time.get_jogadores())

        lista_jogadores = [jogador for linha in matriz_jogadores for jogador in linha]

        lista_jogadores.sort(key=lambda jogador: jogador.nivel)

        qtd_times = len(self.__times)
        for j, jogador in enumerate(lista_jogadores):
            time = self.__times[j % qtd_times]
            time.adicionar_jogador(jogador)
