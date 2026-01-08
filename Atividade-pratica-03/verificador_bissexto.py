
'''Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Para um ano ser bissexto, ele precisa seguir estas regras:

* Ser divisível por 4 (o resto da divisão por 4 deve ser 0).
* PORÉM, se ele for divisível por 100, ele não é bissexto...
* A MENOS que ele também seja divisível por 400.'''


def verificador_bissexto():
    print("------------------ Verificador de Ano Bissexto ------------------")

    while True:
        entrada = input(
            "\nDigite um ano para verificar(ou 'sair' para encerrar o programa): ").strip().lower()

        if entrada == 'sair':
            print("Encerrando o programa. Até mais!")
            break

        try:
            ano = int(entrada)
        except ValueError:
            print("Erro: Por favor, digite um ano válido (número inteiro).")
            continue

        # ("É divisível por 4 E não é divisível por 100") OU ("se for divisível por 400")
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f" O ano {ano} é BISSEXTO. ")
        else:
            print(f"O ano {ano} NÂO é bissexto.")


verificador_bissexto()
