"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""


#Dados
distancia_percorrida = 300 #KM
combustivel_gasto = 25     #litros

#Cálculo
consumo_medio  = distancia_percorrida / combustivel_gasto 

#Resultado
print("----- Detalhes da Viagem -----")
print(f"Distância Percorrida: {distancia_percorrida} KM")
print(f"Combustível Gasto: {combustivel_gasto} Litros")
print("-" * 30)
print(f"O consumo médio (KM/L): {consumo_medio:.2f}")
print("-" * 30)



