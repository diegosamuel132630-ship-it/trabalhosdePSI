from soldados import (
    criar_soldado,
    listar_soldados,
    editar_soldado,
    apagar_soldado,
    buscar_soldado_por_id
)
from utils import input_int, paises


def mostrar_resposta(code, data):
    if code in (200, 201):
        print(" Sucesso:")
    else:
        print(" Erro:")

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
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1. Criar soldado")
        print("2. Listar soldados")
        print("3. Editar soldado")
        print("4. Apagar soldado")
        print("5. Buscar soldado por ID")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "0":
            print("Encerrando sistema...")
            break

        elif op == "1":
            nome = input("Nome: ")
            idade = input_int("Idade: ")
            patente = input("Patente: ")

            print("Países:", list(paises.keys()))
            pais = input("País: ")

            code, data = criar_soldado(nome, idade, patente, pais)
            mostrar_resposta(code, data)

        elif op == "2":
            code, data = listar_soldados()
            mostrar_resposta(code, data)

        elif op == "3":
            idx = input_int("ID: ")

            nome = input("Novo nome (enter para manter): ") or None

            idade_txt = input("Nova idade (enter para manter): ")
            idade = int(idade_txt) if idade_txt else None

            patente = input("Nova patente (enter para manter): ") or None

            code, data = editar_soldado(idx, nome, idade, patente)
            mostrar_resposta(code, data)

        elif op == "4":
            idx = input_int("ID: ")
            code, data = apagar_soldado(idx)
            mostrar_resposta(code, data)

        elif op == "5":
            idx = input_int("ID: ")
            code, data = buscar_soldado_por_id(idx)
            mostrar_resposta(code, data)

        else:
            print(" Opção inválida")


if __name__ == "__main__":
    main()
