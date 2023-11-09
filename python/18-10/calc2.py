import os
def soma(a,b):
    print(f'sua soma deu: {a+b}\n')

def sub(a,b):
    
    print(f'sua sub deu: {a-b}\n')

def div(a,b):
    print(f'sua div deu: {a/b}\n')
    
def mult(a,b):
    print(f'sua mult deu: {a*b}\n')



while True:
    a = float(input('Digite o primeiro numero:\n'))
    b = float(input('Digite o segundo numero:\n'))    
    op = int(input("Olá, digite a opção desejada:\n\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - DIVISÃO\n4 - MULTIPLICAÇÃO\n5 - SAIR\n"))

    if op == 1:
        soma(a,b)
    
    elif op == 2:
        sub(a,b)

    elif op == 3:
        div(a,b)

    elif op == 4:
        mult(a,b)

    elif op == 5:
        print("Programa finalizado")
        break
    else:
        print("numero invalido")

def teste(a,b,c):
    if c == 1:
        print(a+b)

teste(1,2,1)