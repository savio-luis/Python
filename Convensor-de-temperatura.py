
def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def celsius_to_kelvin(temp):
    return temp + 273.15

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def fahrenheit_to_kelvin(temp):
    return (temp - 32) * 5/9 + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def kelvin_to_fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32

while True:
    print("\nEscolha uma opção de conversão:")
    print("1- Converter de Celsius para Fahrenheit")
    print("2- Converter de Celsius para Kelvin")
    print("3- Converter de Fahrenheit para Celsius")
    print("4- Converter de Fahrenheit para Kelvin")
    print("5- Converter de Kelvin para Celsius")
    print("6- Converter de Kelvin para Fahrenheit")
    print("0- Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        temp = float(input("Digite a temperatura em Celsius: "))
        print("A temperatura em Fahrenheit é:", celsius_to_fahrenheit(temp))
    elif opcao == '2':
        temp = float(input("Digite a temperatura em Celsius: "))
        print("A temperatura em Kelvin é:", celsius_to_kelvin(temp))
    elif opcao == '3':
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        print("A temperatura em Celsius é:", fahrenheit_to_celsius(temp))
    elif opcao == '4':
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        print("A temperatura em Kelvin é:", fahrenheit_to_kelvin(temp))
    elif opcao == '5':
        temp = float(input("Digite a temperatura em Kelvin: "))
        print("A temperatura em Celsius é:", kelvin_to_celsius(temp))
    elif opcao == '6':
        temp = float(input("Digite a temperatura em Kelvin: "))
        print("A temperatura em Fahrenheit é:", kelvin_to_fahrenheit(temp))
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.")