"""2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""


def calculadora_imc():
    print("----- Calculadora de IMC Profissional! -----")

    while True:
        entrada = input(
            "\nPressione ENTER para calcular ou digite 'sair': ").strip().lower()

        if entrada == 'sair':
            print("Encerrando a calculadora. Cuide-se! ")
            break

        try:
            # Pedimos os valores e limpamos espaços
            peso = float(input("Digite seu peso em kg (ex: 70.5): ").strip())
            altura = float(
                input("Digite sua altura em metros (ex: 1.75): ").strip())

        except ValueError:
            print("Erro: Por favor, use números e utilize o ponto como separador decimal.")
            continue  # Volta para o início do loop

        # Verificação lógica: peso ou altura zero
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser maiores que zero.")
            continue


        imc = peso / (altura ** 2)
        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso ")

        elif imc < 25:
            # Se chegou aqui, é porque é 18.5 ou mais
            print("Classificação: Peso normal ")

        elif imc < 30:
            # Se chegou aqui, é porque é 25 ou mais
            print("Classificação: Sobrepeso ")

        else:
            # Qualquer valor acima de 30
            print("Classificação: Obeso ")


# Executa o programa
calculadora_imc()
