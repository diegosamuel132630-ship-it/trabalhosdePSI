import json

soldados = []
next_id = 1


# =========================
# PERSISTÊNCIA
# =========================

def guardar_dados(nome_ficheiro="soldados.json"):
    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            json.dump({
                "soldados": soldados,
                "next_id": next_id
            }, f, indent=4, ensure_ascii=False)

        return 200, "Dados guardados com sucesso"

    except Exception as e:
        return 500, str(e)


def carregar_dados(nome_ficheiro="soldados.json"):
    global soldados, next_id

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)

        soldados[:] = dados.get("soldados", [])
        next_id = dados.get("next_id", 1)

        return 200, "Dados carregados com sucesso"

    except FileNotFoundError:
        return 404, "Ficheiro não encontrado"

    except Exception as e:
        return 500, str(e)

def criar(nome, idade, patente, pais):
    global next_id

    carregar_dados()

    s = {
        "id": next_id,
        "nome": nome,
        "idade": idade,
        "patente": patente,
        "pais": pais
    }

    soldados.append(s)

    next_id += 1

    guardar_dados()

    return 201, s


def listar():
    carregar_dados()

    if not soldados:
        return 404, "Sem soldados"

    return 200, soldados


def buscar(id_):
    carregar_dados()

    for s in soldados:
        if s["id"] == id_:
            return 200, s

    return 404, "Não encontrado"


def atualizar(id_, nome, idade, patente, pais):
    carregar_dados()

    for s in soldados:
        if s["id"] == id_:

            s.update({
                "nome": nome,
                "idade": idade,
                "patente": patente,
                "pais": pais
            })

            guardar_dados()

            return 200, s

    return 404, "Não encontrado"


def apagar(id_):
    carregar_dados()

    for s in soldados:
        if s["id"] == id_:

            soldados.remove(s)

            guardar_dados()

            return 200, s

    return 404, "Não encontrado"
