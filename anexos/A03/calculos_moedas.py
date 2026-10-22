"""A03 — complete as funções antes de conectá-las à janela."""
def calcular(campos, registro):
    # TODO: ler reais e as duas cotações; aceitar vírgula ou ponto decimal.
    # TODO: tratar conversão inválida, reais negativos e cotações <= 0.
    # TODO: dividir reais por cada cotação.
    # TODO: confirmar entradas e os dois resultados somente após validar tudo.
    return "Complete a função calcular."


def exibir(registro):
    # TODO: tratar ausência de conversão; consultar somente registro.
    # TODO: mostrar entradas usadas e resultados, estes com duas casas.
    return "Complete a função exibir."


def limpar(campos):
    # TODO: esvaziar os três campos; preservar registro e resultados.
    pass


if __name__ == "__main__":
    campos = {"reais": "100", "cotacao_dolar": "5", "cotacao_euro": "4"}
    registro = {}
    print(exibir(registro))
    print(calcular(campos, registro))
    print(exibir(registro))
    # Acrescente as outras sequências da matriz, prevendo antes de executar.
