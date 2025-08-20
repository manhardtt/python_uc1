##
# Aula 09 - Atividade 01 - Exercicio 01
# Nome: [João Pedro]
#Data: 19/08/2025
##

#Exemplo de Vetor
vetor = [10, 20 , 30, 40, 50]
print(f"dados da 4a posição: {vetor}")

print(f"dados da 4a posição: {vetor[3]}")


for elemento in vetor:
    print(f"Valor do elemento {elemento}")


for i in range(5):
    print(f"{vetor[i]}")




for i in range(5):
    print(f"O valor da {i+1}a posição é {vetor[i]}")



indicie = 1
for elemento in range(5):
    print(f"o valor do indicie {indicie} é {elemento}")
    indicie +=1




import random  
numero = random.randint(1, 187)
print(f"{numero}")





numeros = []
for i in range (20):
    numeros.append(random.randint(1,187))
    print(f"{numeros}")




numeros = []
for i in range (20):
    numeros.append(random.randint(1,187))
    print(f"{numeros}")

    soma = sum(numeros)
    maior = max(numeros)
    menor = min(numeros)
    qt_elementos = len(numeros)
    media = soma/qt_elementos




numeros = []
for i in range (20):
    numeros.append(random.randint(1,187))
    
print(f"{numeros}")

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
qt_elementos = len(numeros)
media = soma/qt_elementos

print(f"A soma dos elementos é: {soma:6}")
print(f"A soma dos elementos é: {soma:89}")
print(f"A soma dos elementos é: {soma}")
print(f"O maior valor dos elementos é: {maior} ")
print(f"O menor valor dos elemntos é: {menor}")
print(f"A qt dos elementos é: {qt_elementos} ")
print(f"O valo médio é: {media}")





vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in vetor if num % 2 == 0]
impares = [num for num in vetor if num % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)

       
produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
for nome, preco in produtos:
    print(f"{nome:.<20} R$ {preco:.2f}")






    produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
total = 0

for nome, preco in produtos:
    quantidade = int(input(f"Quantidade de {nome}: "))
    subtotal = preco * quantidade
    total += subtotal
    print(f"{nome:.<20} R$ {preco:.2f} x {quantidade} = R$ {subtotal:.2f}")

print(f"\nTOTAL A PAGAR: R$ {total:.2f}")