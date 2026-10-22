"""A02 — prática 2: complete a lógica e os callbacks."""
import tkinter as tk
from tkinter import ttk


def registrar(campos, registro):
    # TODO: ler e normalizar nome e sobrenome; recusar texto vazio.
    # TODO: converter idade e validar inteiro maior que zero.
    # TODO: atualizar registro somente depois de todas as validações.
    return "Complete a função registrar."


def exibir(registro):
    # TODO: tratar a ausência de registro e consultar o último válido.
    return "Complete a função exibir."


def limpar(campos):
    # TODO: esvaziar os três textos editáveis.
    # O registro confirmado é separado e não é recebido por esta função.
    pass


def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro em memória — A02")
    janela.columnconfigure(1, weight=1)
    campos = {"nome": "", "sobrenome": "", "idade": ""}
    registro = {}

    ttk.Label(janela, text="Nome fictício:").grid(row=0, column=0, padx=12, pady=6, sticky="w")
    entrada_nome = ttk.Entry(janela)
    entrada_nome.grid(row=0, column=1, padx=12, pady=6, sticky="ew")
    ttk.Label(janela, text="Sobrenome fictício:").grid(row=1, column=0, padx=12, pady=6, sticky="w")
    entrada_sobrenome = ttk.Entry(janela)
    entrada_sobrenome.grid(row=1, column=1, padx=12, pady=6, sticky="ew")
    ttk.Label(janela, text="Idade fictícia:").grid(row=2, column=0, padx=12, pady=6, sticky="w")
    entrada_idade = ttk.Entry(janela)
    entrada_idade.grid(row=2, column=1, padx=12, pady=6, sticky="ew")

    def ao_registrar():
        # TODO: copiar os textos atuais para campos e chamar registrar.
        # TODO: atualizar a mensagem e a consulta ao registro confirmado.
        aviso.configure(text="Complete o callback Registrar.")

    def ao_exibir():
        # TODO: consultar apenas registro; não ler os campos em edição.
        aviso.configure(text="Complete o callback Exibir.")

    def ao_limpar():
        # TODO: limpar campos e Entry; manter registro e consulta intactos.
        aviso.configure(text="Complete o callback Limpar campos.")

    ttk.Button(janela, text="Registrar", command=ao_registrar).grid(row=3, column=0, padx=12, pady=8)
    ttk.Button(janela, text="Exibir", command=ao_exibir).grid(row=3, column=1, padx=12, pady=8)
    ttk.Button(janela, text="Limpar campos", command=ao_limpar).grid(row=4, column=0, columnspan=2, pady=6)
    aviso = ttk.Label(janela, text="Preencha os dados fictícios e registre.", wraplength=390)
    aviso.grid(row=5, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    resultado = ttk.Label(janela, text="Nenhum cadastro registrado nesta sessão.", wraplength=390)
    resultado.grid(row=6, column=0, columnspan=2, padx=12, pady=8, sticky="w")
    entrada_nome.focus_set()
    return janela


if __name__ == "__main__":
    criar_janela().mainloop()
