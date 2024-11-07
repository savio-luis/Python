#solicita os 5 números aos usuários 
alunos = []
notas = []

for i in range(5):
  aluno = input("Digite o nome do aluno: ")
  nota = input("Digite a nota do aluno: ")
  alunos.append(aluno)
  notas.append(nota)
for i in range(5):
  print(f"o aluno {alunos[i]} tirou nota {notas[i]}")
