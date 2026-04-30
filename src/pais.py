paises_data = {}
next_id = 1


def criar(nome, hino, infra, bandeira, recursos):
    global next_id

    p = {
        "id": next_id,
        "nome": nome,
        "hino": hino,
        "infraestrutura": infra,
        "bandeira": bandeira,
        "recursos": recursos
    }

    paises_data[next_id] = p
    next_id += 1

    return 201, p


def listar():
    return 200, list(paises_data.values())


def menu_pais():
    while True:
        print("\n=== PAÍS ===")
        print("1. Criar")
        print("2. Listar")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "0":
            break

        elif op == "1":
            print(*criar(
                input("Nome: "),
                input("Hino: "),
                input("Infra: "),
                input("Bandeira: "),
                input("Recursos: ")
            ))

        elif op == "2":
            print(*listar())

        else:
            print("Inválido")