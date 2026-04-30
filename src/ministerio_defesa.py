from soldados import *
from utils import input_int, paises

missoes = []
next_missao = 1


def relatorio():
    return 200, {
        "total": len(soldados),
        "por_pais": {p: len(d["soldados"]) for p, d in paises.items()}
    }


def criar_missao(nome, pais, ids):
    global next_missao

    missao = {
        "id": next_missao,
        "nome": nome,
        "pais": pais,
        "soldados": ids
    }

    missoes.append(missao)
    next_missao += 1

    return 201, missao


def listar_missoes():
    return 200, missoes


# MENU DENTRO DO FICHEIRO
def menu_ministerio():
    while True:
        print("\n=== MINISTÉRIO ===")
        print("1. Relatório")
        print("2. Criar missão")
        print("3. Listar missões")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "0":
            break

        elif op == "1":
            print(*relatorio())

        elif op == "2":
            nome = input("Nome missão: ")
            pais = input("País: ")
            ids = list(map(int, input("IDs: ").split(",")))

            print(*criar_missao(nome, pais, ids))

        elif op == "3":
            print(*listar_missoes())

        else:
            print("Inválido")