from utils import validar_nome, validar_idade, validar_texto, paises

soldados = []
next_soldado_id = 1


def criar_soldado(nome, idade, patente, pais):
    global next_soldado_id

    if not validar_nome(nome):
        return 400, "Nome inválido"

    if not validar_idade(idade):
        return 400, "Idade inválida"

    if not validar_texto(patente):
        return 400, "Patente inválida"

    if pais not in paises:
        return 404, "País inválido"

    soldado = {
        "id": next_soldado_id,
        "nome": nome.strip(),
        "idade": idade,
        "patente": patente.strip(),
        "pais": pais
    }

    soldados.append(soldado)
    paises[pais]["soldados"].append(soldado)

    next_soldado_id += 1

    return 201, soldado


def listar_soldados():
    return 200, soldados


def buscar_soldado_por_id(soldado_id):
    for s in soldados:
        if s["id"] == soldado_id:
            return 200, s
    return 404, "Soldado não encontrado"


def editar_soldado(soldado_id, nome=None, idade=None, patente=None):
    for s in soldados:
        if s["id"] == soldado_id:

            if nome is not None:
                if not validar_nome(nome):
                    return 400, "Nome inválido"
                s["nome"] = nome.strip()

            if idade is not None:
                if not validar_idade(idade):
                    return 400, "Idade inválida"
                s["idade"] = idade

            if patente is not None:
                if not validar_texto(patente):
                    return 400, "Patente inválida"
                s["patente"] = patente.strip()

            return 200, s

    return 404, "Soldado não encontrado"


def apagar_soldado(soldado_id):
    for i, s in enumerate(soldados):
        if s["id"] == soldado_id:

            if s in paises[s["pais"]]["soldados"]:
                paises[s["pais"]]["soldados"].remove(s)

            del soldados[i]
            return 200, "Soldado removido"

    return 404, "Soldado não encontrado"