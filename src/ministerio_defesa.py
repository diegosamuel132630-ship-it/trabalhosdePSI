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


# ❌ REMOVIDO: relatorio() (não faz parte do CRUD)
