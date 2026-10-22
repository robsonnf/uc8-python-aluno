"""A02 — prática 1: campos em edição e registro confirmado."""

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


if __name__ == "__main__":
    campos = {"nome": "Lia", "sobrenome": "Costa", "idade": "18"}
    registro = {}
    print(registrar(campos, registro))
    print(exibir(registro))
    limpar(campos)
    print("Campos após limpar:", campos)
    print(exibir(registro))
    # Acrescente os outros cenários da matriz, um de cada vez.
