from soldados import soldados

missoes = []
next_id = 1


def criar(nome, pais, ids_soldados):
    global next_id

    missao = {
        "id": next_id,
        "nome": nome,
        "pais": pais,
        "soldados": ids_soldados
    }

    missoes.append(missao)
    next_id += 1
    return 201, missao


def listar():
    if not missoes:
        return 404, "Sem missões"
    return 200, missoes


def buscar(id_):
    for m in missoes:
        if m["id"] == id_:
            return 200, m
    return 404, "Não encontrado"


def atualizar(id_, nome, pais, ids_soldados):
    for m in missoes:
        if m["id"] == id_:
            m.update({
                "nome": nome,
                "pais": pais,
                "soldados": ids_soldados
            })
            return 200, m

    return 404, "Não encontrado"


def apagar(id_):
    for m in missoes:
        if m["id"] == id_:
            missoes.remove(m)
            return 200, m

    return 404, "Não encontrado"


# =========================
#  PERSISTÊNCIA (ADICIONADO)
# =========================

import json


def guardar_dados(nome_ficheiro="missoes.json"):
    try:
        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            json.dump({
                "missoes": missoes,
                "next_id": next_id
            }, f, indent=4, ensure_ascii=False)

        return 200, "Dados guardados com sucesso"

    except Exception as e:
        return 500, str(e)


def carregar_dados(nome_ficheiro="missoes.json"):
    global missoes, next_id

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)

        missoes[:] = dados.get("missoes", [])
        next_id = dados.get("next_id", 1)

        return 200, "Dados carregados com sucesso"

    except FileNotFoundError:
        return 404, "Ficheiro não encontrado"

    except Exception as e:
        return 500, str(e)
