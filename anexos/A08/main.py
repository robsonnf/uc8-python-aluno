# A08: integre sua versão anterior; preserve-a em outra pasta.
import tkinter as tk
from tkinter import ttk


def criar_janela():
    janela = tk.Tk()
    janela.title("A08 — minha implementação")
    janela.columnconfigure(0, weight=1)
    base = ttk.Frame(janela, padding=12)
    base.grid(row=0, column=0, sticky="nsew")
    base.columnconfigure(0, weight=1)
    ttk.Label(base, text="Traga seu layout e conecte as responsabilidades desta aula.", wraplength=430).grid(row=0, column=0)
    aviso = ttk.Label(base, text="Implementação em andamento.", wraplength=430)
    aviso.grid(row=2, column=0, pady=8)
    def testar():
        # TODO: conectar seu modelo/controller; tratar o erro sem perder dados.
        aviso.configure(text="Complete o fluxo e execute os casos do registro.")
    ttk.Button(base, text="Testar meu fluxo", command=testar).grid(row=1, column=0, pady=8)
    # TODO: organização, rótulos, listagens, ações e foco indicados no roteiro.
    return janela


if __name__ == "__main__":
    criar_janela().mainloop()
