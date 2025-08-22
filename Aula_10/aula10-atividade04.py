##
# Exercicios 4, 5, 6:
##

# Exercício 4:

matriz=[]
for i in range(4):
    linha=[]
    for j in range(4):
        valor=float(input("Digite um valor entre 0 e 99: "))
        linha.append(valor)
    matriz.append(linha)
print(f"{matriz}")
for linha in matriz: 
    maior = 0
    for valor in linha:
        if valor > maior:
            maior = valor 
            print(f"O maior valor da linha: {linha} \n\t\t >> {valor} <<")






