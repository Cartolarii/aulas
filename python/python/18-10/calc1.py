import os
def soma():
    
    a = float(input('Digite o primeiro numero:\n'))
    b = float(input('Digite o segundo numero:\n'))
    soma=a+b
    os.system('cls')
    print(f'sua soma deu: {soma}\n')

def sub():
    a = float(input('Digite o primeiro numero:\n'))
    b = float(input('Digite o segundo numero:\n'))
    sub=a-b
    os.system('cls')
    print(f'sua subtração deu: {sub}\n')

def div():
    a = float(input('Digite o primeiro numero:\n'))
    b = float(input('Digite o segundo numero:\n'))
    div=a/b
    os.system('cls')
    print(f'sua divisão deu: {div}\n')
    
def mult():
    a = float(input('Digite o primeiro numero:\n'))
    b = float(input('Digite o segundo numero:\n'))   
    mult=a*b
    os.system('cls')
    print(f'sua multiplicação deu: {mult}\n')

op = 6

while op !=5:
    
    op = int(input("Olá, digite a opção desejada:\n\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - DIVISÃO\n4 - MULTIPLICAÇÃO\n5 - SAIR\n"))

    if op == 1:
        soma()
    
    elif op == 2:
        sub()

    elif op == 3:
        div()

    elif op == 4:
        mult()

    elif op == 5:
        print("Programa finalizado")
