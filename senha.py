# ==================================================
# Mini Projeto 1 - Gerador de Siglas (Versão Complexa)
# Autor: Diego
# ==================================================

def gerar_sigla(frase):
    # Palavras a ignorar
    ignorar = ["de", "da", "do", "das", "dos", "e", "em"]

    palavras = frase.split()
    sigla = ""

    for palavra in palavras:
        if palavra.lower() not in ignorar:
            sigla += palavra[0]

    return sigla.upper()


def gerar_password(sigla):
    # Cria uma password simples a partir da sigla
    return sigla + "2026#"


# -------- PROGRAMA PRINCIPAL --------
print("=== GERADOR DE SIGLAS ===")

frase = input("Digite uma palavra ou frase: ").strip()

if frase == "":
    print("Erro: não foi introduzido nenhum texto.")
else:
    print("\nEscolha uma opção:")
    print("1 - Gerar apenas sigla")
    print("2 - Gerar sigla + password")

    opcao = input("Opção: ")

    sigla = gerar_sigla(frase)

    if opcao == "1":
        print("\nSigla gerada:", sigla)

    elif opcao == "2":
        password = gerar_password(sigla)
        print("\nSigla:", sigla)
        print("Password gerada:", password)

    else:
        print("\nOpção inválida.")
