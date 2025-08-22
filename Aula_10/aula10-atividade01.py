##
# Aula 09 - Atividade 01 - Exercicio 01
# Nome: [João Pedro]
#Data: 21/08/2025
##

"""
# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9,]
]
print("Elemento (0,0):", matriz[0][0])  # Saída: 1
print("Elemento (2,1):", matriz[2][1])  # Saída: 8
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()


# Código 2
import random
matriz_1 = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = random.randint(0, 100)
        linha.append(elemento)
    matriz_1.append(linha)

for linha in matriz_1:
    print(linha)


"""


# Código 3
import random
matriz_2 = []
for i in range(3):
    linha = []

    for j in range(3):
        #linha.append(i)
        #linha.append(j)
        #linha.append(random.randint(0, 100))
        valor = random.randint(0, 100)
        linha.append(valor)

    matriz_2.append(linha)

# Imprime a matriz 3x3
print (f"{matriz_2}")


# Código 4:
for linha in matriz_2:
    print(f"{linha}")

# Código 5:

for linha in matriz_2 :
    for valor in linha :
        print(f"{linha}")



# Código 6:
for linha in matriz_2 :
    for valor in linha :
        print(f"{valor:02}", end=" ")

# Neste código utilizamos o "for" de maneira similar a outras linguagens de programação.
for i in range(3): 
    for j in range(3):
        print(f"Elemento ({i},{j}) >>> {matriz_2 [i][j]:02}")

