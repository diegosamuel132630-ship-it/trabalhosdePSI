estruturas = []
next_id = 1


def criar(nome, valor, resp, pais):
    global next_id

    e = {
        "id": next_id,
        "nome": nome,
        "valor": valor,
        "responsavel": resp,
        "pais": pais
    }

    estruturas.append(e)
    next_id += 1

    return 201, e


def listar():
    return 200, estruturas


def menu_estrutura():
    while True:
        print("\n=== ESTRUTURA MILITAR ===")
        print("1. Criar")
        print("2. Listar")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "0":
            break

        elif op == "1":
            print(*criar(
                input("Nome: "),
                input("Valor: "),
                input("Responsável: "),
                input("País: ")
            ))

        elif op == "2":
            print(*listar())

        else:
            print("Inválido")