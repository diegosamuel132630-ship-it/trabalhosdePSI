# =========================
# SISTEMA DE SOLDADOS
# =========================
def criar_soldado():
    print("\n--- Criar Soldado ---")

    numero = input("Número militar: ").strip()

    if numero in numeros_militares:
        print("❌ Já existe!")
        return

    nome = input("Nome: ").strip()

    try:
        idade = int(input("Idade: "))
    except:
        print("❌ Idade inválida!")
        return

    patente = input("Patente: ").strip()

    # validar país em loop
    while True:
        print("Países disponíveis:", list(paises.keys()))
        pais = input("País: ").strip()

        if pais in paises:
            break
        else:
            print("❌ País inválido! Tenta novamente.")

    forca = random.randint(50, 100)

    soldado = {
        "numero": numero,
        "dados": [nome, idade],
        "patente": patente,
        "forca": forca,
        "pais": pais
    }

    soldados.append(soldado)
    paises[pais]["soldados"].append(soldado)
    numeros_militares.add(numero)

    guardar_dados()
    print(f"✅ Soldado criado com força {forca}!")


def listar_soldados():
    for s in soldados:
        nome, idade = s["dados"]
        print(f"{s['numero']} - {nome} ({idade}) - {s['patente']} - Força:{s['forca']} - {s['pais']}")


def editar_soldado():
    numero = input("Número: ")
    for s in soldados:
        if s["numero"] == numero:
            s["dados"][0] = input("Novo nome: ")
            s["dados"][1] = int(input("Nova idade: "))
            s["patente"] = input("Nova patente: ")
            guardar_dados()
            print("✅ Editado!")
            return
    print("❌ Não encontrado!")


def apagar_soldado():
    numero = input("Número: ")
    for s in soldados:
        if s["numero"] == numero:
            soldados.remove(s)
            paises[s["pais"]]["soldados"].remove(s)
            numeros_militares.remove(numero)
            guardar_dados()
            print("🗑️ Apagado!")
            return
    print("❌ Não encontrado!")
