"""1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais)."""


def classificador_idade():
    print("\n----- Classificador de Idade Inteligente -----")

    while True:
        entrada = input(
            "\nDigite a idade (ou 'sair' para encerrar): ").strip().lower()

        if entrada == 'sair':
            print("Encerrando o programa. Até Logo!")
            break

        try:
            idade = int(entrada)
        except ValueError:
            print("❌ Erro: Por favor, digite um número inteiro válido.")
            continue

        # Checa se a idade faz sentido
        if idade < 0:
            print("Erro: Idade não pode ser negativa")
            continue

        # Agora as categorias em ordem:
        if idade <= 12:
            print("Categoria: Criança ")
        elif idade <= 17:
            print("Categoria: Adolescente ")
        elif idade <= 59:
            print("Categoria: Adulto")
        else:
            print("Categoria: Idoso")


classificador_idade()
