from tkinter import Tk, Label, Button, OptionMenu, StringVar, Entry, Toplevel
from tkcalendar import DateEntry
from Racha import Racha
from Time import Time
from Jogador import Jogador
from tkinter import messagebox

class Interface:
    def __init__(self):
        # Janela principal
        self.window = Tk()
        self.window.title("Racha")
        self.window.geometry("400x400")

        self.label = Label(self.window, text="Bem-vindo(a) ao Rachinha!")
        self.label.pack()

        # Data
        self.data_label = Label(self.window, text="Selecione a Data")
        self.data_label.pack()
        self.data_var = StringVar()
        self.data_entry = DateEntry(self.window, textvariable=self.data_var, date_pattern="dd/MM/yyyy")
        self.data_entry.pack()

        # Localização
        self.local_label = Label(self.window, text="Insira a localização")
        self.local_label.pack()
        self.local_var = StringVar()
        self.local_entry = Entry(self.window, textvariable=self.local_var)
        self.local_entry.pack()

        # Quantidade Jogadores
        self.quantidade_jogadores_label = Label(self.window, text="Insira a Quantidade de jogadores")
        self.quantidade_jogadores_label.pack()
        self.quantidade_jogadores_var = StringVar()
        self.quantidade_jogadores_entry = Entry(self.window, textvariable=self.quantidade_jogadores_var)
        self.quantidade_jogadores_entry.pack()

        # Quantidade de Times
        self.quantidade_times_label = Label(self.window, text="Insira a Quantidade de Times")
        self.quantidade_times_label.pack()
        self.quantidade_times_var = StringVar()
        self.quantidade_times_entry = Entry(self.window, textvariable=self.quantidade_times_var)
        self.quantidade_times_entry.pack()

        # Crie um botão para criar o objeto Racha com base nas informações fornecidas
        self.create_racha_button = Button(self.window, text="Criar Racha", command=self.criar_racha)
        self.create_racha_button.pack()

        self.window.mainloop()

    def criar_racha(self):
        # Criar Racha
        data = self.data_var.get()
        local = self.local_var.get()
        quantidade_jogadores = int(self.quantidade_jogadores_var.get())
        quantidade_times = int(self.quantidade_times_var.get())

     
        racha = Racha(data, local, quantidade_jogadores, quantidade_times)

        # Janela Time e Jogadores
        nova_janela = Toplevel(self.window)
        nova_janela.title("Inserir Times e Jogadores")

        times_entries = []
        jogadores_entries = []
        niveis_entries = []
        posicoes_entries = []

        for i in range(quantidade_times):
            time_label = Label(nova_janela, text=f"Time {i+1}:")
            time_label.grid(row=(i * (quantidade_jogadores+1)), column=0, padx=5, pady=5)

            for j in range(quantidade_jogadores):
                jogador_label = Label(nova_janela, text=f"Jogador {j+1} (Time {i+1}):")
                jogador_label.grid(row=(i * (quantidade_jogadores+1)) + j + 1, column=0, padx=5, pady=5)

                time_entry_var = StringVar()
                time_entry = Entry(nova_janela, textvariable=time_entry_var)
                time_entry.grid(row=(i * (quantidade_jogadores+1)), column=1, padx=5, pady=5)
                times_entries.append(time_entry_var)

                jogador_entry_var = StringVar()
                jogador_entry = Entry(nova_janela, textvariable=jogador_entry_var)
                jogador_entry.grid(row=(i * (quantidade_jogadores+1)) + j + 1, column=1, padx=5, pady=5)
                jogadores_entries.append(jogador_entry_var)

                nivel_var = StringVar()
                nivel_option = OptionMenu(nova_janela, nivel_var, "1", "2", "3", "4", "5")
                nivel_option.grid(row=(i * (quantidade_jogadores+1)) + j + 1, column=2, padx=5, pady=5)
                niveis_entries.append(nivel_var)

                posicao_var = StringVar()
                posicao_option = OptionMenu(nova_janela, posicao_var, "Goleiro", "Linha")
                posicao_option.grid(row=(i * (quantidade_jogadores+1)) + j + 1, column=3, padx=5, pady=5)
                posicoes_entries.append(posicao_var)

        distribuir_button = Button(nova_janela, text="Distribuir Times", command=lambda: self.distribuir_times(racha, times_entries, jogadores_entries, niveis_entries, posicoes_entries))
        distribuir_button.grid(row=(quantidade_times * (quantidade_jogadores+1)) + 1, column=0, columnspan=4, padx=5, pady=10)

    def distribuir_times(self, racha, times_entries, jogadores_entries, niveis_entries, posicoes_entries):
        times = [entry.get() for entry in times_entries]
        jogadores = [entry.get() for entry in jogadores_entries]
        niveis = [int(var.get()) for var in niveis_entries]
        posicoes = [var.get() for var in posicoes_entries]

        # if "" in times or "" in jogadores or "" in posicoes:
        #     messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        #     return

        for i in range(len(times)):
            time = Time(times[i])
            jogador = Jogador(jogadores[i], niveis[i], posicoes[i])
            time.adicionar_jogador(jogador)
            racha.adicionar_time(time)

        racha.distribuir_jogadores()

        resultado_janela = Toplevel(self.window)
        resultado_janela.title("Resultados do Racha")

        detalhes_label = Label(resultado_janela, text="Detalhes do Racha:")
        detalhes_label.pack()

        data_label = Label(resultado_janela, text=f"Data: {racha.data}")
        data_label.pack()

        local_label = Label(resultado_janela, text=f"Local: {racha.local}")
        local_label.pack()

        times_label = Label(resultado_janela, text="Times:")
        times_label.pack()

        for time in racha.get_times():
            time_label = Label(resultado_janela, text=f"{time.nome}:")
            time_label.pack()
            for jogador in time.get_jogadores():
                jogador_label = Label(resultado_janela, text=f"Jogador: {jogador.nome}, Nível: {jogador.habilidade}, Posição: {jogador.posicao}")
                jogador_label.pack()

        self.window.destroy()

interface = Interface()
