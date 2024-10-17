# Algoritmo que imprime os números de 1 a 100
print("Números de 1 a 100:")
for i in range(1, 101):
    print(i)

# Algoritmo que exibe a tabuada de um número fornecido pelo usuário
numero = int(input("\nDigite um número para ver sua tabuada: "))
print(f"\nTabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Algoritmo que calcula a soma dos pares entre 1 e 50
soma = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma += i
print(f"\nA soma dos números pares entre 1 e 50 é: {soma}")
