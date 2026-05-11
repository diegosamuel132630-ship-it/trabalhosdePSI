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
