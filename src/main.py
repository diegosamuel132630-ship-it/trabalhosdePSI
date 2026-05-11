from soldados import criar as c_sold, listar as l_sold, buscar as b_sold, atualizar as u_sold, apagar as d_sold
from governo import criar as c_gov, listar as l_gov, buscar as b_gov, atualizar as u_gov, apagar as d_gov
from estrutura_militar import criar as c_est, listar as l_est, buscar as b_est, atualizar as u_est, apagar as d_est
from pais import criar as c_pais, listar as l_pais, buscar as b_pais, atualizar as u_pais, apagar as d_pais
from ministerio_defesa import criar as c_mis, listar as l_mis, buscar as b_mis, atualizar as u_mis, apagar as d_mis


def mostrar(code, data):
    print(f"\n[{code}]")
    print(data)


# =========================
# SOLDADOS
# =========================
def menu_soldados():
    while True:
        print("\n=== SOLDADOS ===")
        print("1 Criar 2 Listar 3 Buscar 4 Atualizar 5 Apagar 0 Voltar")

        op = input("Op: ")

        if op == "0":
            print("A sair do sistema...")
            break
        elif op == "1":
            mostrar(*c_sold(input("Nome: "), int(input("Idade: ")), input("Patente: "), input("País: ")))
        elif op == "2":
            mostrar(*l_sold())
        elif op == "3":
            mostrar(*b_sold(int(input("ID: "))))
        elif op == "4":
            mostrar(*u_sold(int(input("ID: ")), input("Nome: "), int(input("Idade: ")), input("Patente: "), input("País: ")))
        elif op == "5":
            mostrar(*d_sold(int(input("ID: "))))


# =========================
# GOVERNO
# =========================
def menu_governo():
    while True:
        print("\n=== GOVERNO ===")
        print("1 Criar 2 Listar 3 Buscar 4 Atualizar 5 Apagar 0 Voltar")

        op = input("Op: ")

        if op == "0":
            break
        elif op == "1":
            mostrar(*c_gov(input("Presidente: "), input("Ministro: "), input("Nome: "), input("País: ")))
        elif op == "2":
            mostrar(*l_gov())
        elif op == "3":
            mostrar(*b_gov(int(input("ID: "))))
        elif op == "4":
            mostrar(*u_gov(int(input("ID: ")), input("Presidente: "), input("Ministro: "), input("Nome: "), input("País: ")))
        elif op == "5":
            mostrar(*d_gov(int(input("ID: "))))


# =========================
# ESTRUTURA
# =========================
def menu_estrutura():
    while True:
        print("\n=== ESTRUTURA ===")
        print("1 Criar 2 Listar 3 Buscar 4 Atualizar 5 Apagar 0 Voltar")

        op = input("Op: ")

        if op == "0":
            break
        elif op == "1":
            mostrar(*c_est(input("Nome: "), int(input("Valor: ")), input("Responsável: "), input("País: ")))
        elif op == "2":
            mostrar(*l_est())
        elif op == "3":
            mostrar(*b_est(int(input("ID: "))))
        elif op == "4":
            mostrar(*u_est(int(input("ID: ")), input("Nome: "), int(input("Valor: ")), input("Responsável: "), input("País: ")))
        elif op == "5":
            mostrar(*d_est(int(input("ID: "))))


# =========================
# PAÍS
# =========================
def menu_pais():
    while True:
        print("\n=== PAÍS ===")
        print("1 Criar 2 Listar 3 Buscar 4 Atualizar 5 Apagar 0 Voltar")

        op = input("Op: ")

        if op == "0":
            break
        elif op == "1":
            mostrar(*c_pais(input("Nome: ")))
        elif op == "2":
            mostrar(*l_pais())
        elif op == "3":
            mostrar(*b_pais(int(input("ID: "))))
        elif op == "4":
            mostrar(*u_pais(int(input("ID: ")), input("Nome: ")))
        elif op == "5":
            mostrar(*d_pais(int(input("ID: "))))


# =========================
# MINISTÉRIO DEFESA
# =========================
def menu_ministerio():
    while True:
        print("\n=== MINISTÉRIO ===")
        print("1 Criar missão 2 Listar 3 Buscar 4 Atualizar 5 Apagar 0 Voltar")

        op = input("Op: ")

        if op == "0":
            break
        elif op == "1":
            ids = list(map(int, input("IDs soldados: ").split(",")))
            mostrar(*c_mis(input("Nome missão: "), input("País: "), ids))
        elif op == "2":
            mostrar(*l_mis())
        elif op == "3":
            mostrar(*b_mis(int(input("ID: "))))
        elif op == "4":
            ids = list(map(int, input("Novos IDs: ").split(",")))
            mostrar(*u_mis(int(input("ID: ")), input("Nome: "), input("País: "), ids))
        elif op == "5":
            mostrar(*d_mis(int(input("ID: "))))


# =========================
# MAIN
# =========================
def main():
    while True:
        print("\n===== SISTEMA GERAL =====")
        print("1 Soldados")
        print("2 Governo")
        print("3 Estrutura Militar")
        print("4 País")
        print("5 Ministério Defesa")
        print("0 Sair")

        op = input("Escolha: ")

        if op == "0":
            break
        elif op == "1":
            menu_soldados()
        elif op == "2":
            menu_governo()
        elif op == "3":
            menu_estrutura()
        elif op == "4":
            menu_pais()
        elif op == "5":
            menu_ministerio()


if __name__ == "__main__":
    main()
