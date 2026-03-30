# =========================
# GUARDAR / CARREGAR
# =========================
def guardar_dados():
    dados = {
        "utilizadores": utilizadores,
        "soldados": soldados,
        "guerras": guerras,
        "paises": paises
    }
    with open(FICHEIRO, "w") as f:
        json.dump(dados, f, indent=4)


def carregar_dados():
    global utilizadores, soldados, guerras, paises

    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r") as f:
            dados = json.load(f)
            utilizadores = dados.get("utilizadores", {})
            soldados = dados.get("soldados", [])
            guerras = dados.get("guerras", [])
            paises = dados.get("paises", paises)

        for s in soldados:
            numeros_militares.add(s["numero"])
            paises[s["pais"]]["soldados"].append(s)
