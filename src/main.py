from soldados import *
from utils import input_int, paises
from ministerio_defesa import *


def mostrar_resposta(code, data):
    if code in (200, 201):
        print(f"\nSucesso ({code})")
    else:
        print(f"\nErro ({code})")

    if isinstance(data, dict):
        for k, v in data.items():
            print(f"{k}: {v}")

    elif isinstance(data, list):
        if not data:
            print("Lista vazia")
        else:
            for item in data:
                print(item)

    else:
        print(data)


def main():
    while True:
        print("\n===== SISTEMA =====")
        print("1. Criar soldado")
        print("2. Listar soldados")
        print("3. Editar soldado")
        print("4. Apagar soldado")
        print("5. Buscar soldado")
        print("6. Ministério da Defesa")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "0":
            break

        # =========================
        # SOLDADOS
        # =========================
        elif op == "1":
            nome = input("Nome: ")
            idade = input_int("Idade: ")
            patente = input("Patente: ")

            print("Países:", list(paises.keys()))
            pais = input("País: ")

            if pais not in paises:
                print("País inválido!")
                continue

            resultado = criar_soldado(nome, idade, patente, pais)
            print(*resultado)

        elif op == "2":
            print(*listar_soldados())

        elif op == "3":
            sid = input_int("ID: ")

            nome = input("Novo nome: ") or None

            idade_txt = input("Nova idade: ")
            if idade_txt:
                try:
                    idade = int(idade_txt)
                except:
                    print("Idade inválida!")
                    continue
            else:
                idade = None

            patente = input("Nova patente: ") or None

            print(*editar_soldado(sid, nome, idade, patente))

        elif op == "4":
            sid = input_int("ID: ")
            print(*apagar_soldado(sid))

        elif op == "5":
            sid = input_int("ID: ")
            print(*buscar_soldado_por_id(sid))

        # =========================
        # MINISTÉRIO DA DEFESA
        # =========================
        elif op == "6":
            while True:
                print("\n=== MINISTÉRIO ===")
                print("1. Relatório")
                print("2. Transferir soldado")
                print("3. Criar missão")
                print("4. Listar missões")
                print("5. Ranking")
                print("0. Voltar")

                sub = input("Escolha: ")

                if sub == "0":
                    break

                elif sub == "1":
                    print(*relatorio_geral())

                elif sub == "2":
                    sid = input_int("ID: ")
                    print("Países:", list(paises.keys()))
                    pais = input("Novo país: ")

                    print(*transferir_soldado(sid, pais))

                elif sub == "3":
                    nome = input("Nome missão: ")
                    print("Países:", list(paises.keys()))
                    pais = input("País: ")

                    ids = input("IDs (1,2,3): ")
                    lista = [int(x) for x in ids.split(",") if x.strip()]

                    print(*criar_missao(nome, pais, lista))

                elif sub == "4":
                    print(*listar_missoes())

                elif sub == "5":
                    print(*ranking_paises())

                else:
                    print("Opção inválida")

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()