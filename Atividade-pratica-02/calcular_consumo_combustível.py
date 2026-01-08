"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""


#Dados
distancia = 300 #KM
combustivel = 25     #litros

#Cálculo
consumo_medio  = distancia / combustivel 

#Resultado
print("----- Detalhes da Viagem -----")
print(f"Distância Percorrida: {distancia} KM")
print(f"Combustível Gasto: {combustivel} Litros")
print("-" * 30)
print(f"O consumo médio (KM/L): {consumo_medio:.2f}")
print("-" * 30)



