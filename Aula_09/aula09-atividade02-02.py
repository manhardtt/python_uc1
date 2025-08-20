##
# Aula 09 - Atividade 01 - Exercicio 01
# Nome: [João Pedro]
#Data: 19/08/2025
##

#Exemplo de Vetor


'''

produtos = (
    ("Arroz", 5.99, 10),
    ("Feijão", 7.49, 3),
    ("Leite", 4.89, 5),
    ("Óleo", 9.99, 2),
    ("Açúcar", 3.29, 5)
)

total_geral = 0
print("LISTA DE PRODUTOS")
for nome, preco, qt in produtos:
    total = preco * qt
    total_geral = total_geral + total
    print(f"{nome: , <20} - {preco:6.2f} x {qt: 03} =  R$ {total:6.2f}")
total_geral = total_geral * 0.9
print(f"\n\t Valor da compra: R$ {total_geral: 8.20f}")
print(f"\t       Desconto: - 10%")
print(f"\t  Valor  Final: R$ {total_desconto: 8.2f}")

'''







import random

# gerar uma lista de 100 números aleatórios entre 1 e 100
numeros = [random.randint(1, 100) for _ in range(100)]

# calcular a média dos números
media = sum(numeros) / len(numeros)

# obter os valores maiores do que a média
maiores_que_media = [n for n in numeros if n > media]

# exibir os resultados
print(f"numeros gerados: {numeros}")
print(f"media: {media:.2f}")
print(f"numeros maiores que a media: {maiores_que_media}")
