import sys
import threading
import customtkinter as ctk
import time
import tkinter as tk
from tkinter import *
from Redirecionamento import TextRedirecionado
from SavesBot import InstaSavesBot

from Validador import Validadores

janela = ctk.CTk()

class InstaBotSaveView():
    def __init__(self):
        self.janela = janela
        self.customConfig()
        self.janelaConfig()
        self.windowWidgets()
        janela.mainloop()
    def customConfig(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
    def janelaConfig(self):

        largura_janela = 1000  # Largura da janela
        altura_janela = 600   # Altura da janela
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        pos_x = largura_tela // 2 - largura_janela // 2
        pos_y = altura_tela // 2 - altura_janela // 2
        janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        janela.title("INSTABOT - SAVES")
        janela.resizable(False, False)
        janela.iconbitmap("icon.ico")
    def windowWidgets(self):
        # Janela Widgets
        self.entry_username = ctk.CTkEntry(master=janela, placeholder_text="Username", width=450, height=50)
        self.entry_username.place(x=25, y=40)

        self.entry_password = ctk.CTkEntry(master=janela, placeholder_text="Password", width=450, height=50, show="*")
        self.entry_password.place(x=25, y=120)

        self.label_repeticoes = ctk.CTkLabel(master=janela, text="REPETIÇÕES:")
        self.label_repeticoes.place(x=30, y=210)
        self.entry_repeticoes = ctk.CTkEntry(master=janela, placeholder_text="Repetições", width=200, height=50, validate="key", validatecommand=(self.janela.register(Validadores.validar_numeros), "%P"))
        self.entry_repeticoes.place(x=120, y=200)

        self.label_mensagem = ctk.CTkLabel(master=janela, text="MENSAGEM:")
        self.label_mensagem.place(x=200, y=260)
        self.mensagem_text = ctk.CTkTextbox(master=janela, width=450, height=300)
        self.mensagem_text.place(x=25, y=290)

        # Frame Config
        frame = ctk.CTkFrame(master=janela, width=500, height=600)
        frame.pack(side=RIGHT)

        # Frames Widgets
        self.btn_iniciar = ctk.CTkButton(master=frame, text="INICIAR", width=160, height=40, command=lambda: threading.Thread(target=self.IniciarAplicacao).start())
        self.btn_iniciar.place(x=90, y=40)

        self.btn_limpar = ctk.CTkButton(master=frame, text="LIMPAR LOG", width=160, height=40, command=self.limpar_log)
        self.btn_limpar.place(x=270, y=40)

        self.log_text = ctk.CTkTextbox(master=frame, width=450, height=470)
        self.log_text.place(x=25, y=120)  
    def IniciarAplicacao(self):
        # Fazendo com que as caixas de texto preenchidas não possam ser alteradas no momento em que o programa iniciar
        self.entry_username.configure(state=tk.DISABLED)
        self.entry_password.configure(state=tk.DISABLED)
        self.mensagem_text.configure(state=tk.DISABLED)
        self.entry_repeticoes.configure(state=tk.DISABLED)

        sys.stdout = TextRedirecionado(self.log_text)
        num_repeticao = int(self.entry_repeticoes.get()) + 1
        for i in range (1, num_repeticao, 1):
            print(f"INICIANDO EXECUÇÃO {i}/{num_repeticao-1}")
            # Formatando Mensagem
            todo_texto = self.mensagem_text.get("1.0", "end-1c")
            linhas = todo_texto.splitlines()
            texto_formatado = "\n".join(linhas)

            InstaBot = InstaSavesBot(self.entry_username.get(), self.entry_password.get(), texto_formatado)
            InstaBot.login()
            # Habilitando edição de texto
            self.entry_username.configure(state=tk.NORMAL)
            self.entry_password.configure(state=tk.NORMAL)
            self.mensagem_text.configure(state=tk.NORMAL)
            self.entry_repeticoes.configure(state=tk.NORMAL)
            if (i == num_repeticao-1):
                print("PROCESSO FINALIZADO")
            else:
                self.ContagemRegressiva(20*60)
    def ContagemRegressiva(self, segundos):
        for tempo_restante in range(segundos, 0, -1):
            minutos, segundos = divmod(tempo_restante, 60)
            formato_tempo = "{:02d}:{:02d}".format(minutos, segundos)
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, f"Próxima repetição em: {formato_tempo}\n")
            self.log_text.config(state=tk.DISABLED)
            self.log_text.see(tk.END)
            time.sleep(1)
    def limpar_log(self):
        self.log_text.configure(state='normal')
        self.log_text.delete('1.0', tk.END)
        self.log_text.configure(state='disabled')

InstaBotSaveView()
