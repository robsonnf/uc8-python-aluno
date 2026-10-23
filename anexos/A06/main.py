import tkinter as tk
from tkinter import ttk
from pathlib import Path
from aluno import Aluno


def inserir_marca(container, caminho=None):
    # TODO: procurar marca-a06.png ao lado do script com pathlib.
    # TODO: usar PhotoImage e conservar uma referência enquanto o rótulo existir.
    # TODO: manter texto se o PNG não existir ou não puder ser lido.
    return ttk.Label(container, text="Sistema escolar fictício — A06")


def abrir_consulta(principal, aluno):
    # TODO: tratar ausência de registro sem criar uma janela vazia.
    # TODO: obter o texto do confirmado no instante da abertura.
    # TODO: criar Toplevel e organizar sua consulta somente de leitura.
    # TODO: botão, X e Escape devem fechar somente a consulta.
    return None


def criar_janela():
    janela = tk.Tk()
    janela.title("Escolar com consulta — A06")
    janela.columnconfigure(0, weight=1)
    janela.rowconfigure(0, weight=1)
    base = ttk.Frame(janela, padding=12)
    base.grid(row=0, column=0, sticky="nsew")
    base.columnconfigure(0, weight=1)
    aluno = Aluno()  # Uma instância por janela principal, fora dos callbacks.
    inserir_marca(base).grid(row=0, column=0, columnspan=2, pady=6, sticky="w")
    # TODO: criar LabelFrame para identificação e notas e Frame para ações.
    # TODO: posicionar os grupos na base e configurar expansão das colunas.
    # A disposição inicial é plana; substitua os pais e ajuste as linhas internas.
    identificacao = base
    grupo_notas = base
    acoes = base
    base.columnconfigure(1, weight=1)

    ttk.Label(identificacao, text="Nome fictício:").grid(row=1, column=0, padx=6, pady=4, sticky="w")
    entrada_nome = ttk.Entry(identificacao)
    entrada_nome.grid(row=1, column=1, padx=6, pady=4, sticky="ew")
    ttk.Label(identificacao, text="Turma fictícia:").grid(row=2, column=0, padx=6, pady=4, sticky="w")
    entrada_turma = ttk.Entry(identificacao)
    entrada_turma.grid(row=2, column=1, padx=6, pady=4, sticky="ew")
    entradas_notas = []
    for numero in range(1, 6):
        ttk.Label(grupo_notas, text=f"Nota {numero} (0 a 10):").grid(row=numero+2, column=0, padx=6, pady=4, sticky="w")
        entrada = ttk.Entry(grupo_notas)
        entrada.grid(row=numero+2, column=1, padx=6, pady=4, sticky="ew")
        entradas_notas.append(entrada)

    def ao_calcular():
        # TODO: ler os sete campos e chamar aluno.atualizar com os textos.
        # TODO: mostrar a mensagem e aluno.resumo; nunca escrever atributos aqui.
        aviso.configure(text="Integração com o modelo ainda não implementada.")

    def ao_exibir():
        # TODO: adaptar sua consulta da A05 para receber aluno.
        aviso.configure(text="Consulta ainda não integrada ao modelo.")

    def ao_limpar():
        # TODO: limpar só os campos e devolver foco, preservando aluno e consultas.
        aviso.configure(text="Limpeza ainda não implementada.")

    ttk.Button(acoes, text="Calcular média", command=ao_calcular).grid(row=8, column=0, padx=4, pady=6)
    ttk.Button(acoes, text="Consultar", command=ao_exibir).grid(row=8, column=1, padx=4, pady=6)
    ttk.Button(acoes, text="Limpar campos", command=ao_limpar).grid(row=9, column=0, columnspan=2, padx=4, pady=6)
    aviso = ttk.Label(base, text="Use dados fictícios e confira as cinco notas.", wraplength=430)
    aviso.grid(row=10, column=0, columnspan=2, pady=6, sticky="w")
    resultado = ttk.Label(base, text="Nenhum registro escolar confirmado nesta sessão.", wraplength=430)
    resultado.grid(row=11, column=0, columnspan=2, pady=6, sticky="w")
    entrada_nome.focus_set()
    return janela


if __name__ == "__main__":
    criar_janela().mainloop()
