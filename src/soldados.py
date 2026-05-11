soldados = []
next_id = 1


def criar(nome, idade, patente, pais):
    global next_id

    s = {
        "id": next_id,
        "nome": nome,
        "idade": idade,
        "patente": patente,
        "pais": pais
    }

    soldados.append(s)
    next_id += 1
    return 201, s


def listar():
    if not soldados:
        return 404, "Sem soldados"
    return 200, soldados


def buscar(id_):
    for s in soldados:
        if s["id"] == id_:
            return 200, s
    return 404, "Não encontrado"


def atualizar(id_, nome, idade, patente, pais):
    for s in soldados:
        if s["id"] == id_:
            s.update({
                "nome": nome,
                "idade": idade,
                "patente": patente,
                "pais": pais
            })
            return 200, s

    return 404, "Não encontrado"


def apagar(id_):
    for s in soldados:
        if s["id"] == id_:
            soldados.remove(s)
            return 200, s

    return 404, "Não encontrado"
