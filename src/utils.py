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


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Número inválido!")


def validar_nome(n):
    return isinstance(n, str) and n.strip() != ""


def validar_idade(i):
    return isinstance(i, int) and i > 0


def validar_texto(t):
    return isinstance(t, str) and t.strip() != ""