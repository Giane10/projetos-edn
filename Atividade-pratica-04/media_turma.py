
'''Criar um código que registre as notas de alunos e calcular a média da turma.'''


def calcular_media():
    print("\n----- Calculadora de Média da Turma ------")
    soma_notas = 0.0
    contador_notas = 0

    while True:
        entrada = input(
            "Digite a nota (ou 'ok' para calcular): ").strip().lower()

        if entrada == 'ok':
            print("---------- Resultado da Média ------------")
            break

        try:
            nota_aluno = float(entrada)
            soma_notas += nota_aluno
            contador_notas += 1

        except ValueError:
            print("Erro: Digite um número válido ")
            continue

    if contador_notas > 0:
        media = soma_notas / contador_notas
        print(f"\n Total de notas: {contador_notas}")
        print(f" A média da turma é: {media:.2f}")
        print("\n------------------------------------------")
    else:
        print("\nNenhuma nota foi registrada.")


calcular_media()
