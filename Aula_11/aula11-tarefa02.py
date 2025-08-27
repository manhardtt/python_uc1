alunos = {}

# adicionar alunos:

alunos[1] = {"nome": "Maria", "notas": [7.5, 8.0, 9.2]}
alunos[2] = {"nome": "João", "notas": [6.0, 7.8, 8.5]}
alunos[3] = {"nome": "Carlos", "notas": [5.5, 6.5, 7.0]}

#calcular medidas:

for id_aluno, info in alunos.items():
    notas = info["notas"]
    media = sum(notas) / len(notas)
    info["média"] = round(media, 2)

print(alunos)