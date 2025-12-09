"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais
"""
#Dados
nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5

total_notas = 3

#calculo
media_notas = (nota_1 + nota_2 + nota_3) / total_notas

#Exibição do Resultado
print("-" * 25)
print(f"Nota 1: {nota_1}")
print(f"Nota 1: {nota_2}")
print(f"Nota 1: {nota_3}")
print("-" * 25)
print(f"A média das notas é: {media_notas:.2f}") #duas casas decimais
print("-" * 25)