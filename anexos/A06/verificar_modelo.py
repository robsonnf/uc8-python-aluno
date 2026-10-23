from aluno import Aluno


def verificar_independencia():
    lia = Aluno()
    rui = Aluno()
    # TODO: comparar os objetos, suas listas, médias e alterações independentes.
    # TODO: usar assert nos resultados esperados; só então retornar True.
    return False


def verificar_validacao():
    # TODO: válido seguido de erro; conferir preservação de todos os atributos.
    # TODO: testar limites 0/10, vírgula e lista de textos independente.
    # TODO: retornar True somente depois das verificações implementadas.
    return False


if __name__ == "__main__":
    independencia = verificar_independencia()
    validacao = verificar_validacao()
    if independencia and validacao:
        print("Verificações do modelo concluídas.")
    else:
        print("Verificações incompletas; implemente e execute os casos.")
