import json

governos = []
next_id = 1


# =========================
# PERSISTÊNCIA
# =========================

def guardar_dados(nome_ficheiro="governos.json"):
    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            json.dump({
                "governos": governos,
                "next_id": next_id
            }, f, indent=4, ensure_ascii=False)

        return 200, "Dados guardados com sucesso"

    except Exception as e:
        return 500, str(e)


def carregar_dados(nome_ficheiro="governos.json"):
    global governos, next_id

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)

        governos[:] = dados.get("governos", [])
        next_id = dados.get("next_id", 1)

        return 200, "Dados carregados com sucesso"

    except FileNotFoundError:
        return 404, "Ficheiro não encontrado"

    except Exception as e:
        return 500, str(e)

def criar(presidente, ministro, nome, pais):
    global next_id

    carregar_dados()

    g = {
        "id": next_id,
        "presidente": presidente,
        "ministro": ministro,
        "nome": nome,
        "pais": pais
    }

    governos.append(g)

    next_id += 1
    guardar_dados()

    return 201, g


def listar():
    carregar_dados()

    if not governos:
        return 404, "Sem governos"

    return 200, governos


def buscar(id_):
    carregar_dados()

    for g in governos:
        if g["id"] == id_:
            return 200, g

    return 404, "Não encontrado"


def atualizar(id_, presidente, ministro, nome, pais):
    carregar_dados()

    for g in governos:
        if g["id"] == id_:

            g.update({
                "presidente": presidente,
                "ministro": ministro,
                "nome": nome,
                "pais": pais
            })

            guardar_dados()
            return 200, g

    return 404, "Não encontrado"


def apagar(id_):
    carregar_dados()

    for g in governos:
        if g["id"] == id_:

            governos.remove(g)

            guardar_dados()
            return 200, g

    return 404, "Não encontrado"
