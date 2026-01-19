
'''Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).'''


def calculadora():
    print("------ Calculadora de Operações Básicas ------")

    while True:
        entrada = input(
            "\nPressione ENTER para calcular ou digite 'sair': ").strip().lower()

        if entrada == 'sair':
            print("Encerrando calculadora...")
            break

        try:
            numero1 = float(input("Por Favor, digite o primeiro numero: "))
            operacao = input("Digite a operação (+, -, *, /): ").strip()
            numero2 = float(input("Por Favor, digite o segundo numero: "))

        except ValueError:
            print("Erro: Digite um número válido ")
            continue

        if operacao == '+':
            print("Resultado:", numero1 + numero2)
        elif operacao == '-':
            print("Resultado:", numero1 - numero2)
        elif operacao == '*':
            print("Resultado:", numero1 * numero2)

        elif operacao == '/':
            if numero2 != 0:
                print("Resultado:", numero1 / numero2)
            else:
                print("Erro: Não é possível dividir por zero!")

        else:
            print("Operação inválida.")


calculadora()
