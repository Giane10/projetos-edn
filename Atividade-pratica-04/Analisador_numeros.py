
''' Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''


def analisar_numeros():
    print("\n---  Analisador de Números Pares e Ímpares ---")
    
    # Inicializamos os contadores
    pares = 0
    impares = 0

    while True:
        entrada = input("\nDigite um número inteiro (ou 'fim' para ver o resultado): ").strip().lower()

        if entrada == 'fim':
            break

        try:
            numero = int(entrada)
            
            # Lógica para verificar se é par ou ímpar
            if numero % 2 == 0:
                print(f"-> O número {numero} é PAR.")
                pares += 1
            else:
                print(f"-> O número {numero} é ÍMPAR.")
                impares += 1
                
        except ValueError:
            print(" Erro: Por favor, digite um número inteiro válido.")

    # Exibição do relatório final
    print("\n========================================")
    print("        RELATÓRIO DE ANÁLISE")
    print("========================================")
    print(f" Total de números PARES:   {pares}")
    print(f" Total de números ÍMPARES: {impares}")
    print(f" Total de números lidos:   {pares + impares}")
    print("========================================\n")

# Chamada da função
analisar_numeros()