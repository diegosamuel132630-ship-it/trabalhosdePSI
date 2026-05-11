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
