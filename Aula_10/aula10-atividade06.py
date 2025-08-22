##
# Exercício 4, 5, 6:
##

#Exercício 5:

import random
matriz=[]
for i in range(4):
    linha=[]
    for j in range(4):
        linha.append(random.randint(1, 1000))
    matriz.append(linha)
print(f"{matriz}")
num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

matriz[linha_escolhida] = [num * valor for valor in matriz[linha_escolhida]]

for linha in matriz:
    print(linha)