from soldados import menu_soldados
from ministerio_defesa import menu_ministerio
from governo import menu_governo
from pais import menu_pais
from estrutura_militar import menu_estrutura


def main():
    while True:
        print("\n===== SISTEMA GERAL =====")
        print("1. Ministério da Defesa")
        print("2. Governo")
        print("3. País")
        print("4. Estrutura Militar")
        print("5. Soldados")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "0":
            print("A sair do sistema...")
            break

        elif op == "1":
            menu_ministerio()

        elif op == "2":
            menu_governo()

        elif op == "3":
            menu_pais()

        elif op == "4":
            menu_estrutura()

        elif op == "5":
            menu_soldados()

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()