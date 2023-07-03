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
        self.__times = []
        self.__placar = None

    def criar_time(self, nome):
        time = Time(nome)
        self.__times.append(time)

    def remover_time(self, time):
        if time in self.__times:
            self.__times.remove(time)
        else:
            raise ValueError("O time não está presente na lista de times.")

    def definir_placar(self, gols_time1, gols_time2):
        self.__placar = (gols_time1, gols_time2)

    def get_data(self):
        return self.__data

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

    def distribuir_jogadores(self, times, jogadores, niveis, posicoes, jogadores_por_time, quantidade_times):
        times_dict = {}
        nivel_minimo_diferenca = 3  

        for i in range(len(times)):
            if times[i] not in times_dict:
                times_dict[times[i]] = Time(times[i])

            jogador = Jogador(jogadores[i], int(niveis[i]), posicoes[i])
            times_dict[times[i]].adicionar_jogador(jogador)

        for time in times_dict.values():
            nivel_time = time.calcular_nivel_time()

            time_adicionado = False

            for existing_time in self.__times:
                nivel_time_existente = existing_time.calcular_nivel_time()
                diferenca = abs(nivel_time - nivel_time_existente)

                if diferenca >= nivel_minimo_diferenca:
                    continue

                if len(existing_time.get_jogadores()) >= jogadores_por_time:
                    continue

                if len(existing_time.get_jogadores()) + len(time.get_jogadores()) <= jogadores_por_time:
                    for jogador in time.get_jogadores():
                        existing_time.adicionar_jogador(jogador)
                else:
                    jogadores_excedentes = jogadores_por_time - len(existing_time.get_jogadores())
                    for jogador in time.get_jogadores()[:jogadores_excedentes]:
                        existing_time.adicionar_jogador(jogador)

                time_adicionado = True
                break

            if not time_adicionado and len(self.__times) < quantidade_times and len(time.get_jogadores()) > 0:
                if len(time.get_jogadores()) <= jogadores_por_time:
                    self.__times.append(time)
                else:
                    novo_time_excedente = Time(time.get_nome())
                    for jogador in time.get_jogadores()[:jogadores_por_time]:
                        novo_time_excedente.adicionar_jogador(jogador)
                    self.__times.append(novo_time_excedente)

