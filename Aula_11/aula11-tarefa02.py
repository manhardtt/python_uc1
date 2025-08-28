
alunos = {}


# adicionar alunos:

alunos[1] = {"nome": "gabriel", "notas": [7.5, 8.0, 9.2]}
alunos[2] = {"nome": "joão", "notas": [6.0, 7.8, 8.5]}
alunos[3] = {"nome": "kauan", "notas": [5.5, 6.5, 7.0]}

#calcular medidas:

for id_aluno, info in alunos.items():
    notas = info["notas"]
    media = sum(notas) / len(notas)
    info["média"] = round(media, 2)

print(alunos)


alunos[1] ["notas"].append(2.3)
alunos[2] ["notas"].append(8.1)
alunos[3] ["notas"].append(6.4)

alunos[1] ["notas"].append(5.2)
alunos[2] ["notas"].append(7.5)
alunos[3] ["notas"].append(9.4)

alunos[1] ["notas"].append(10.0)
alunos[2] ["notas"].append(6.1)
alunos[3] ["notas"].append(5.7)

print(alunos[1])
