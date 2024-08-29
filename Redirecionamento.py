import tkinter as tk

class TextRedirecionado():
    def __init__(self, texto_log):
        self.texto_log = texto_log

    def write(self, texto):
        self.texto_log.configure(state=tk.NORMAL)
        self.texto_log.insert(tk.END, texto)
        self.texto_log.configure(state=tk.DISABLED)
        self.texto_log.see(tk.END)
      
    def flush(self):
        pass
