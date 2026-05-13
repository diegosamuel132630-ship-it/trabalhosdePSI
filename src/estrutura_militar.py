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
    if not estruturas:
        return 404, "Sem estruturas"
    return 200, estruturas


def buscar(id_):
    for e in estruturas:
        if e["id"] == id_:
            return 200, e
    return 404, "Não encontrado"


def atualizar(id_, nome, valor, resp, pais):
    for e in estruturas:
        if e["id"] == id_:
            e.update({
                "nome": nome,
                "valor": valor,
                "responsavel": resp,
                "pais": pais
            })
            return 200, e

    return 404, "Não encontrado"


def apagar(id_):
    for e in estruturas:
        if e["id"] == id_:
            estruturas.remove(e)
            return 200, e

    return 404, "Não encontrado"


# =========================
#  PERSISTÊNCIA (ADICIONADO)
# =========================

import json


def guardar_dados(nome_ficheiro="estruturas.json"):
    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            json.dump({
                "estruturas": estruturas,
                "next_id": next_id
            }, f, indent=4, ensure_ascii=False)

        return 200, "Dados guardados com sucesso"

    except Exception as e:
        return 500, str(e)


def carregar_dados(nome_ficheiro="estruturas.json"):
    global estruturas, next_id

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)

        estruturas[:] = dados.get("estruturas", [])
        next_id = dados.get("next_id", 1)

        return 200, "Dados carregados com sucesso"

    except FileNotFoundError:
        return 404, "Ficheiro não encontrado"

    except Exception as e:
        return 500, str(e)
