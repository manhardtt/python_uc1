## Desafio/Avaliação

# 1) Criar 2 Matrizes 10x10 com números aleatórios entre 1 e 999:

import random



matriz_1 = [[random.randint(1, 999) for i in range(10)] for j in range(10)]
matriz_2 = [[random.randint(1, 999) for i in range(10)] for j in range(10)]

print("Matriz 1:")
for linha in matriz_1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz_2:
    print(linha) 

# 2) Criar uma nova Matriz 10x10 com a soma dos elementos das 2 matrizes anteriores:

matriz_1 = [[random.randint(1, 999) for i in range(10)] for j in range(10)]
matriz_2 = [[random.randint(1, 999) for i in range(10)] for j in range(10)]

matriz_soma = [[matriz_1[i][j] + matriz_2[i][j] for j in range(10)] for i in range(10)]

print("\nSoma das Matrizes:")
for linha in matriz_soma:
    print(linha)
  
#3) Calcular a média dos valores da nova matriz:

soma_total = sum(sum(linha) for linha in matriz_soma)
media = soma_total / 100  # pois 10x10 = 100 elementos

print(f"\nmédia dos valores das matrizes: {media:.2f}")




