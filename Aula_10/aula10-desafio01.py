import random
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = random.randint(0, 1000)
        linha.append(elemento)
    matriz.append(linha)
print(matriz)