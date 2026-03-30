# =========================
# RANKING
# =========================
def ranking():
    print("\n Ranking de Países")
    ordenado = sorted(paises.items(), key=lambda x: calcular_forca_total(x[0]), reverse=True)

    for i, (nome, _) in enumerate(ordenado, 1):
        print(f"{i}. {nome} - Força: {calcular_forca_total(nome)} - Ouro: {paises[nome]['ouro']}")

# =========================
# MENU
# =========================
def menu_jogo():
    while True:
        print("\n===== JOGO AAA =====")
        print("1. Criar Soldado")
        print("2. Listar Soldados")
        print("3. Editar Soldado")
        print("4. Apagar Soldado")
        print("5. Declarar Guerra")
        print("6. Simular Guerra")
        print("7. Ranking")
        print("8. Logout")

        op = input("Escolha: ")

        if op == "1": criar_soldado()
        elif op == "2": listar_soldados()
        elif op == "3": editar_soldado()
        elif op == "4": apagar_soldado()
        elif op == "5": declarar_guerra()
        elif op == "6": simular_guerras()
        elif op == "7": ranking()
        elif op == "8": break
        else: print(" Erro")
