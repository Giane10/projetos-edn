"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

"""
Fahrenheir = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15
Celsius = Kelvin - 273.15
Celsius = (Fahrenheit - 32) * 5/9
"""


def conversor_temperatura():
    print("\n----- Conversor de Temperatura Inteligente -----")

    while True:
        entrada = input(
            "\nDigite a temperatura (ou 'sair' para encerrar): ").strip().lower()

        # Condição de Saída
        if entrada == 'sair':
            print("Encerrando o conversor. Até logo!")
            break

        # Tratamento de Erros
        try:
            valor_temp = float(entrada)
        except ValueError:
            print(" Erro: Por favor, digite um número válido.")
            continue  # Volta para o início do loop imediatamente

        # Escolha das Unidades com Padronização (.upper transforma em MAIÚSCULA)
        origem = input("Unidade de origem (C, F, K): ").strip().upper()
        destino = input("Unidade de destino (C, F, K): ").strip().upper()

        # Validação das unidades permitidas
        unidades_validas = ['C', 'F', 'K']
        if origem not in unidades_validas or destino not in unidades_validas:
            print("Erro: Use apenas C (Celsius), F (Fahrenheit) ou K (Kelvin).")
            continue

        #  Lógica da "Ponte Celsius" (Transforma tudo na mesma base primeiro)
        # Primeiro: De Origem para Celsius
        if origem == 'C':
            temp_celsius = valor_temp
        elif origem == 'F':
            temp_celsius - (valor_temp - 32) * 5/9
        else:  # origem é Kelvin (K)
            temp_celsius = valor_temp - 273.15

        # Segundo: De Celsius para o Destino final
        if destino == 'C':
            resultado = temp_celsius
        elif destino == 'F':
            resultado = (temp_celsius * 9/5) + 32
        else:  # Destino é Kelvin (K)
            resultado = temp_celsius + 273.15

        # Exibição do Resultado Final (:.2f formata para 2 casas decimais)
        print(
            f"Resultado: {valor_temp:.1f}°{origem} equivale a {resultado:.2f}°{destino}")

 # Chamada para executar o programa
conversor_temperatura()
