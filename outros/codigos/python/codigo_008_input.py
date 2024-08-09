def obtem_numero() -> int:
    return (int(input("Digite um numero inteiro: ")))

def obter_tres_numeros_simples() -> list:
    return [obtem_numero(), obtem_numero(), obtem_numero()]

def obter_trinta_numeros() -> list:
    resultado: list = []
    while len(resultado) < 30:
        resultado.append(obtem_numero())
    return resultado

def obter_n_numeros(quantidade: int = 90) -> list:
    resultado: list = []
    while len(resultado) < quantidade:
        resultado.append(obtem_numero())
    return resultado

