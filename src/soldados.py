from utils import validar_nome, validar_idade, validar_texto, paises

soldados = []
next_id = 1


# =========================
# LÓGICA
# =========================

def criar_soldado(nome, idade, patente, pais):
    global next_id

    if not validar_nome(nome):
        return 400, "Nome inválido"
    if not validar_idade(idade):
        return 400, "Idade inválida"
    if not validar_texto(patente):
        return 400, "Patente inválida"
    if pais not in paises:
        return 404, "País inválido"

    s = {
        "id": next_id,
        "nome": nome.strip(),
        "idade": idade,
        "patente": patente.strip(),
        "pais": pais
    }

    soldados.append(s)
    paises[pais]["soldados"].append(s)

    next_id += 1
    return 201, s


def listar_soldados():
    return 200, list(soldados)


def buscar(id_):
    for s in soldados:
        if s["id"] == id_:
            return 200, s
    return 404, "Não encontrado"


def apagar(id_):
    code, s = buscar(id_)
    if code != 200:
        return 404, "Não encontrado"

    paises[s["pais"]]["soldados"].remove(s)
    soldados.remove(s)

    return 200, "Removido"


# =========================
# MENU
# =========================

def menu_soldados():
    while True:
        print("\n=== SOLDADOS ===")
        print("1. Criar soldado")
        print("2. Listar soldados")
        print("3. Buscar soldado")
        print("4. Apagar soldado")
        print("0. Voltar")

        op = input("Escolha: ")

        if op == "0":
            break

        elif op == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            patente = input("Patente: ")
            pais = input("País: ")

            print(*criar_soldado(nome, idade, patente, pais))

        elif op == "2":
            print(*listar_soldados())

        elif op == "3":
            id_ = int(input("ID: "))
            print(*buscar(id_))

        elif op == "4":
            id_ = int(input("ID: "))
            print(*apagar(id_))

        else:
            print("Opção inválida")