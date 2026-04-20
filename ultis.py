paises = {
    "Portugal": {"soldados": []},
    "Brasil": {"soldados": []},
    "EUA": {"soldados": []},
    "França": {"soldados": []},
    "Alemanha": {"soldados": []}
}

def input_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print(" Digite um número válido!")


def validar_nome(nome):
    return bool(nome.strip())


def validar_idade(idade):
    return idade > 0


def validar_texto(texto):
    return bool(texto.strip())
