velocidade = float(input("Digite a velocidade media"))
tempo = float(input("Digite o tempo da viagem total"))
distancia = velocidade * tempo
consumo = distancia / 12
print("velocidade média:", velocidade, "km/h")
print("tempo gasto na viagem total:", tempo, "h")
print("distancia:", distancia, "km")
print("quantidade de combustivel consumido:", consumo, "litros")
