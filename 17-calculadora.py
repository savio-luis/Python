def exibirMenu():
    print('Calculadora das operações basicas: ')
    print('Menu escolha: ')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Resto da Divisão')
    print('6. Divisão inteira')
    print('7. Sair')
    escolha = int(input('Escolha uma opção: '))
    return escolha


def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 !=0:
        return n1 / n2
    else:
        return 'Erro: Divisão por zero não é permitida.'
    
def divisao_inteira(n1, n2):
    if n2 !=0:
        return n1 // n2
    else:
        return 'Erro: Divisão por zero não é permitida.'
    
   
def resto_divisão(n1, n2):
    if n2 != 0:
        return 'Erro Divisão por zero não é permitida.'
    
opcao= 0


while opcao !=7:
    opcao = exibirMenu()

    if opcao in [1,2,3,4,5,6]:
        n1= float(input('Primeiro valor: '))
        n2= float(input('Segundo valor: '))

    if opcao == 1:
        print(f'A soma dos valores é: {soma(n1,n2)}\n ')
    elif opcao == 2:
        print(f'A subtração dos valores é: {subtracao(n1,n2)}\n')
    elif opcao == 3:
        print(f'A multiplicação dos valores é: {multiplicacao(n1,n2)}\n')
    elif opcao == 4:
        print(f'A divisão dos valores é: {divisao(n1,n2)}\n')
    elif opcao == 5:
        print(f'O resto da divisão dos valores é: {resto_divisão(n1,n2)}\n')
    elif opcao == 6:
        print(f'A divisão inteira dos valores é: {divisao_inteira(n1,n2)}\n')   
    elif opcao == 7:
        print('Finalizando o código!')
    else:
        print('Opção inválida. Tente novamente.\n')

    
    
    
