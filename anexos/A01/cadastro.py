"""A01 — prática 2. Esqueleto funcional de janela, sem validação pronta."""
import tkinter as tk
from tkinter import ttk


def conferir_cadastro():
    # TODO: obter os textos com get().
    # TODO: adaptar a validação que você praticou no terminal.
    # TODO: mostrar o resultado no rótulo; não prometer gravação permanente.
    resultado.configure(text="Implemente e teste seu callback.")


janela = tk.Tk()
janela.title("Conferir cadastro fictício")
janela.columnconfigure(1, weight=1)
ttk.Label(janela, text="Nome fictício:").grid(row=0, column=0, padx=12, pady=8, sticky="w")
entrada_nome = ttk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=12, pady=8, sticky="ew")
ttk.Label(janela, text="Idade fictícia:").grid(row=1, column=0, padx=12, pady=8, sticky="w")
entrada_idade = ttk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=12, pady=8, sticky="ew")
ttk.Button(janela, text="Conferir cadastro", command=conferir_cadastro).grid(row=2, column=0, columnspan=2, pady=8)
resultado = ttk.Label(janela, text="Nenhum cadastro conferido nesta sessão.", wraplength=360)
resultado.grid(row=3, column=0, columnspan=2, padx=12, pady=8, sticky="w")
entrada_nome.focus_set()
janela.mainloop()
