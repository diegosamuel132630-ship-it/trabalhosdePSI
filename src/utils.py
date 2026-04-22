paises = {
    "Portugal": {"soldados": []},
    "Brasil": {"soldados": []},
    "EUA": {"soldados": []},
    "Espanha": {"soldados": []},
    "Itália": {"soldados": []},
    "Reino Unido": {"soldados": []},
    "Canadá": {"soldados": []},
    "México": {"soldados": []},
    "Argentina": {"soldados": []},
    "China": {"soldados": []},
    "Japão": {"soldados": []},
    "Coreia do Sul": {"soldados": []},
    "Rússia": {"soldados": []},
    "Austrália": {"soldados": []},
    "África do Sul": {"soldados": []},
    "Turquia": {"soldados": []},
    "Egito": {"soldados": []}
}


def input_int(mensagem):
    while True:
        valor = input(mensagem)
        try:
            return int(valor)
        except:
            print("Digite um número válido!")


def validar_nome(nome):
    return isinstance(nome, str) and nome.strip() != ""


def validar_idade(idade):
    return isinstance(idade, int) and idade > 0


def validar_texto(texto):
    return isinstance(texto, str) and texto.strip() != ""