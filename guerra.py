# =========================
# GUERRA AVANÇADA
# =========================
def calcular_forca_total(pais):
    return sum(s["forca"] for s in paises[pais]["soldados"])


def declarar_guerra():
    p1 = input("Atacante: ")
    p2 = input("Defensor: ")

    if p1 == p2 or p1 not in paises or p2 not in paises:
        print(" Erro!")
        return

    guerras.append([p1, p2])
    guardar_dados()
    print(f"⚔ {p1} declarou guerra a {p2}!")


def simular_guerras():
    for g in guerras:
        p1, p2 = g

        f1 = calcular_forca_total(p1) + random.randint(0, 50)
        f2 = calcular_forca_total(p2) + random.randint(0, 50)

        print(f"\n⚔️ {p1} vs {p2}")
        print(f"Força total: {f1} vs {f2}")

        if f1 > f2:
            paises[p1]["ouro"] += 50
            print(f"🏆 {p1} venceu e ganhou ouro!")
        elif f2 > f1:
            paises[p2]["ouro"] += 50
            print(f"🏆 {p2} venceu e ganhou ouro!")
        else:
            print("🤝 Empate")

    guardar_dados()
