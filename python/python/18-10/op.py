import os
os.system('cls')

sair = 1

while sair == 1:

    op = int(input("Bem vindo a central de notas.\n\nDIGITE A OPÇÃO DESEJADA: 1 SOMA | 2 - SUBTRAÇÃO | 3 - MULTIPLICAÇÃO\n"))


if op == 1:
    print("Vamos somar suas notas")

    n1 = float(input("digite o numero primeiro numero:\n"))
    n2 = float(input("digite o numero segundo numero:\n"))

    soma = n1+n2
    print(soma)


elif op == 2:
    print("Vamos subtrair suas notas")
    n1 = float(input("digite o numero primeiro numero:\n"))
    n2 = float(input("digite o numero segundo numero:\n"))

    soma = n1-n2
    print(soma)

elif op == 3:
    print("Vamos multiplicar suas notas")
    n1 = float(input("digite o numero primeiro numero:\n"))
    n2 = float(input("digite o numero segundo numero:\n"))

    soma = n1*n2
    print(soma)
else:
    print("opção invalida")

sair = int(input("Deseja continuar? 1 sim | 2 - não"))
