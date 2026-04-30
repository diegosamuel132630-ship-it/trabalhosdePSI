governos = []
next_id = 1


def criar(presidente, ministro, nome, pais):
    global next_id

    g = {
        "id": next_id,
        "presidente": presidente,
        "ministro": ministro,
        "nome": nome,
        "pais": pais
    }

    governos.append(g)
    next_id += 1

    return 201, g


def listar():
    return 200, governos


def menu_governo():
    while True:
        print("\n=== GOVERNO ===")
        print("1. Criar")
        print("2. Listar")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "0":
            break

        elif op == "1":
            print(*criar(
                input("Presidente: "),
                input("Ministro: "),
                input("Nome: "),
                input("País: ")
            ))

        elif op == "2":
            print(*listar())

        else:
            print("Inválido")