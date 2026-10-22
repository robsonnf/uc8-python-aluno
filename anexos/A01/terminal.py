"""A01 — prática 1. Use somente nome e idade fictícios."""

def conferir(nome, idade_texto):
    # TODO: retirar espaços nas pontas e recusar nome sem texto.
    # TODO: converter idade para int, tratar ValueError e exigir idade > 0.
    # TODO: retornar mensagem coerente; não gravar arquivos.
    return "Complete a função conferir antes de concluir os testes."


if __name__ == "__main__":
    nome = input("Nome fictício: ")
    idade_texto = input("Idade fictícia: ")
    print(conferir(nome, idade_texto))
