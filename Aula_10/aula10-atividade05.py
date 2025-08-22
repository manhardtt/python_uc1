##
# Exercício 4, 5, 6:
##

#Exercício 5:
matriz=[]
for i in range(4):
    linha=[]
    for j in range(4):
        valor=float(input("Digite um valor entre 0 e 99: "))
        linha.append(valor)
    matriz.append(linha)
print(f"{matriz}")
par = 0
for i in range(4): 
    for j in range(4):
        if matriz[i][j] % 2 == 0:
         par += 1
print(f"Quantidade de números pares: {par}")

#possibilidade de usar import random ao invez de utilizar o input