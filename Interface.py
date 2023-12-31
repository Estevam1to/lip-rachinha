from tkinter import Tk, Label, Button, OptionMenu, StringVar, Entry, Toplevel
from tkcalendar import DateEntry
from Racha import Racha
from Time import Time
from Jogador import Jogador
from tkinter import messagebox
from tkinter import ttk

class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Racha")
        self.window.geometry("400x400")

        style = ttk.Style()

        style.theme_use("clam")  # Set the desired theme

        self.label = ttk.Label(self.window, text="Bem-vindo(a) ao Rachinha!", font=("Helvetica", 14, "bold"))
        self.label.pack()

        self.data_label = Label(self.window, text="Selecione a Data", font=("Helvetica", 12))
        self.data_label.pack()
        self.data_var = StringVar()
        self.data_entry = DateEntry(self.window, textvariable=self.data_var, date_pattern="dd/MM/yyyy", font=("Helvetica", 12))
        self.data_entry.pack()

        self.local_label = Label(self.window, text="Insira a localização", font=("Helvetica", 12))
        self.local_label.pack()
        self.local_var = StringVar()
        self.local_entry = Entry(self.window, textvariable=self.local_var, font=("Helvetica", 12))
        self.local_entry.pack()

        self.quantidade_jogadores_label = Label(self.window, text="Insira a Quantidade de jogadores por Time", font=("Helvetica", 12))
        self.quantidade_jogadores_label.pack()
        self.quantidade_jogadores_var = StringVar()
        self.quantidade_jogadores_entry = Entry(self.window, textvariable=self.quantidade_jogadores_var, font=("Helvetica", 12))
        self.quantidade_jogadores_entry.pack()

        self.quantidade_times_label = Label(self.window, text="Insira a Quantidade de Times", font=("Helvetica", 12))
        self.quantidade_times_label.pack()
        self.quantidade_times_var = StringVar()
        self.quantidade_times_entry = Entry(self.window, textvariable=self.quantidade_times_var, font=("Helvetica", 12))
        self.quantidade_times_entry.pack()

        self.create_racha_button = Button(self.window, text="Criar Racha", command=self.criar_racha, font=("Helvetica", 12))
        self.create_racha_button.pack()

        self.window.mainloop()

    def criar_racha(self):
        data = self.data_var.get()
        local = self.local_var.get()
        quantidade_jogadores = int(self.quantidade_jogadores_var.get())
        quantidade_times = int(self.quantidade_times_var.get())

        racha = Racha(data, local, quantidade_jogadores, quantidade_times)

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


        distribuir_button = Button(nova_janela, text="Distribuir Times",
                                command=lambda: self.distribuir_times(racha, times_entries, jogadores_entries,
                                                                        niveis_entries, posicoes_entries, quantidade_jogadores, quantidade_times ))
        distribuir_button.grid(row=(quantidade_times * (quantidade_jogadores+1)) + 1, column=0, columnspan=5, padx=5,
                            pady=10)

    def distribuir_times(self, racha, times_entries, jogadores_entries, niveis_entries, posicoes_entries, qtd_jogador, qtd_time):
        times = []
        jogadores = []
        niveis = []
        posicoes = []

        for i in range(len(times_entries)):
            times.append(times_entries[i].get())
            jogadores.append(jogadores_entries[i].get())
            niveis.append(niveis_entries[i].get())
            posicoes.append(posicoes_entries[i].get())

        racha.distribuir_jogadores(times, jogadores, niveis, posicoes, qtd_jogador, qtd_time) 
        self.mostrar_resultados(racha)

    def mostrar_resultados(self, racha):
        resultado_janela = Toplevel(self.window)
        resultado_janela.title("Resultados do Racha")

        detalhes_label = Label(resultado_janela, text="Detalhes do Racha", font=("Helvetica", 14, "bold"))
        detalhes_label.pack(padx=5, pady=5)

        data_label = Label(resultado_janela, text=f"Data: {racha.get_data()}", font=("Helvetica", 12))
        data_label.pack(padx=5, pady=5)

        local_label = Label(resultado_janela, text=f"Local: {racha.get_local()}", font=("Helvetica", 12))
        local_label.pack(padx=5, pady=5)

        for i, time in enumerate(racha.get_times()):
            time_label = Label(resultado_janela, text=f"Time {i+1}: {time.get_nome()}", font=("Helvetica", 12))
            time_label.pack(padx=5, pady=5)

            jogadores_label = Label(resultado_janela, text="Jogadores:", font=("Helvetica", 12, "bold"))
            jogadores_label.pack(padx=5, pady=5)

            jogadores = time.get_jogadores()
            for j, jogador in enumerate(jogadores):
                if jogador.get_posicao() == "Goleiro":
                    jogador_label = Label(resultado_janela, text=f"Jogador {j+1}: {jogador.get_nome()} - Nível: {jogador.get_nivel_habilidade()} - Posição: {jogador.get_posicao()}", font=("Helvetica", 12))
                    jogador_label.pack(padx=5, pady=2)
                else:
                    jogador_label = Label(resultado_janela, text=f"Jogador {j+1}: {jogador.get_nome()} - Nível: {jogador.get_nivel_habilidade()} - Posição: {jogador.get_posicao()}", font=("Helvetica", 12))
                    jogador_label.pack(padx=5, pady=2)

            jogador_separator = Label(resultado_janela, text="-----------------------", font=("Helvetica", 12))
            jogador_separator.pack(padx=5, pady=2)

        messagebox.showinfo("Racha", "Racha criado com sucesso!")



interface = Interface()
