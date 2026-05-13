paises = []
next_id = 1


def criar(nome):
    global next_id

    p = {"id": next_id, "nome": nome}
    paises.append(p)

    next_id += 1
    return 201, p


def listar():
    if not paises:
        return 404, "Sem países"
    return 200, paises


def buscar(id_):
    for p in paises:
        if p["id"] == id_:
            return 200, p
    return 404, "Não encontrado"


def atualizar(id_, nome):
    for p in paises:
        if p["id"] == id_:
            p["nome"] = nome
            return 200, p

    return 404, "Não encontrado"


def apagar(id_):
    for p in paises:
        if p["id"] == id_:
            paises.remove(p)
            return 200, p

    return 404, "Não encontrado"


# =========================
#  PERSISTÊNCIA (ADICIONADO)
# =========================

import json


def guardar_dados(nome_ficheiro="paises.json"):
    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            json.dump({
                "paises": paises,
                "next_id": next_id
            }, f, indent=4, ensure_ascii=False)

        return 200, "Dados guardados com sucesso"

    except Exception as e:
        return 500, str(e)


def carregar_dados(nome_ficheiro="paises.json"):
    global paises, next_id

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)

        paises[:] = dados.get("paises", [])
        next_id = dados.get("next_id", 1)

        return 200, "Dados carregados com sucesso"

    except FileNotFoundError:
        return 404, "Ficheiro não encontrado"

    except Exception as e:
        return 500, str(e)
