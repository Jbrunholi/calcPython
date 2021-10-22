# lab02 - construindo uma calculadora

# Funções
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Nome e indicação de operação
while True:
    print('\n******************** Python Calculator *********************')
    print('\nSelecione o número da operação desejada:\n')
    print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

    escolha = input('Digite sua opção (1/2/3/4 ou 5 para SAIR): ')
    if escolha >= '5':
        print('\n ******* Obrigado e até a próxima ****** \n************ #ForaBolsonaro *************')
        break

    # Input dos valores a serem trabalhados
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    # Lógica Operacional
    if escolha == '1':  # Soma
        print('\n')
        print(num1, ' + ', num2, ' = ', add(num1, num2))

    elif escolha == '2':  # Subtração
        print('\n')
        print(num1, ' - ', num2, ' = ', subtract(num1, num2))

    elif escolha == '3':  # Multiplicação
        print('\n')
        print(num1, ' * ', num2, ' = ', multiply(num1, num2))

    elif escolha == '4':  # Divisão
        print('\n')
        print(num1, ' / ', num2, ' = ', divide(num1, num2))

    elif escolha == '5':  # Sair
        break
