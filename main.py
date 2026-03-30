# =========================
# MAIN
# =========================
def main():
    carregar_dados()

    while True:
        print("\n===== MENU =====")
        print("1. Login")
        print("2. Registar")
        print("3. Sair")

        op = input("Escolha: ")

        if op == "1":
            if login():
                menu_jogo()
        elif op == "2": registar()
        elif op == "3": break
        else: print(" Erro")

if __name__ == "__main__":
    main()
