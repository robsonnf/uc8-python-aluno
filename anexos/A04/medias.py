"""A04 — complete as funções e teste as cinco notas no terminal."""
def calcular(campos, registro):
    # TODO: normalizar nome/turma e recusar texto vazio.
    # TODO: conferir a presença de exatamente cinco notas.
    # TODO: converter cada texto, validar de 0 a 10 e criar uma nova lista.
    # TODO: calcular a média com sum e len.
    # TODO: confirmar nome, turma, notas e média somente após validar tudo.
    return "Complete a função calcular."


def exibir(registro):
    # TODO: tratar ausência; consultar apenas o último registro confirmado.
    # TODO: mostrar identificação e cinco notas usadas, com média em uma casa.
    return "Complete a função exibir."


def limpar(campos):
    # TODO: esvaziar nome, turma e os cinco textos de notas.
    # O registro confirmado não é recebido por esta função.
    pass


if __name__ == "__main__":
    campos = {"nome": "Lia", "turma": "T1", "notas": ["6", "7", "8", "9", "10"]}
    registro = {}
    print(exibir(registro))
    print(calcular(campos, registro))
    print(exibir(registro))
    # Acrescente as sequências da matriz, prevendo antes de executar.
