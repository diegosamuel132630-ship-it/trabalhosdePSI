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
    if not governos:
        return 404, "Sem governos"
    return 200, governos


def buscar(id_):
    for g in governos:
        if g["id"] == id_:
            return 200, g
    return 404, "Não encontrado"


def atualizar(id_, presidente, ministro, nome, pais):
    for g in governos:
        if g["id"] == id_:
            g.update({
                "presidente": presidente,
                "ministro": ministro,
                "nome": nome,
                "pais": pais
            })
            return 200, g

    return 404, "Não encontrado"


def apagar(id_):
    for g in governos:
        if g["id"] == id_:
            governos.remove(g)
            return 200, g

    return 404, "Não encontrado"
