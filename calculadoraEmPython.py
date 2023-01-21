# Lógica

# Calculadora Básica
# Preciso receber um valor do usuário(primeiro valor)
# Preciso que o usuário escolha a operação matemática desejada
# Preciso receber um valor do usuário(segundo valor)
# Preciso mostrar o resultado para o usuário

# funções

# Soma
def Soma(valor1, valor2):
    numeroUm = valor1
    numeroDois = valor2
    resultado = numeroUm + numeroDois
    print("Resultado: ", resultado)

# Subtração


def Sub(valor1, valor2):
    numeroUm = valor1
    numeroDois = valor2
    resultado = numeroUm - numeroDois
    print("Resultado: ", resultado)

# Divisão


def Div(valor1, valor2):
    numeroUm = valor1
    numeroDois = valor2
    resultado = numeroUm / numeroDois
    print("Resultado: ", resultado)

# Multiplicação


def Mult(valor1, valor2):
    numeroUm = valor1
    numeroDois = valor2
    resultado = numeroUm * numeroDois
    print("Resultado: ", resultado)


def calcular():
    print("Digite o primeiro número")
    numeroUm = int(input())
    print()
    print("Operadores Disponíveis:")
    print("'+' => Adição")
    print("'-' => Subtração")
    print("'/' => Divisão")
    print("'*' => Multiplicação")
    print()
    print("Digite um Operador")
    OperadorEscolhido = input()
    print()
    print("Digite o segundo número")
    numeroDois = int(input())
    print()

    if (OperadorEscolhido == '+'):
        Soma(numeroUm, numeroDois)
    elif (OperadorEscolhido == '-'):
        Sub(numeroUm, numeroDois)
    elif (OperadorEscolhido == '/'):
        Div(numeroUm, numeroDois)
    elif (OperadorEscolhido == '*'):
        Mult(numeroUm, numeroDois)
    else:
        print("Desculpe algo deu errado!")


print("--- Seja Bem-Vindo(a) ---")
print()
print("*Está é a calculadora Básica CC50*")
print()
calcular()
