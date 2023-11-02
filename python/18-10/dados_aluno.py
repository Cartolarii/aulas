# pedir nota, nome, 6 notas e media
# nota >0 e <60 reprovado
# >=60 e <=80 aprovado
# >80 e <=90 aprovado com feijao
# <90 e <=100 aprovado com arroz
import os
os.system('cls')
# entrada de dados com conversão
nome = input("digite seu nome:\n")
limite_minimo = 99999999
limite_maximo = 1000000000
# Solicitar um número ao usuário
while True:

    doc = input("Digite seu cpf: ")

    # Converter a entrada para um número (assumindo que o usuário sempre fornece um número válido)
    numero = float(doc)

    # Verificar se o número está dentro dos limites
    if limite_minimo <= numero <= limite_maximo:
        print("Número válido dentro dos limites.")
        break
    else:
        print("Número fora dos limites.")

somanota = 0
for i in range(1, 7):
    nota = float(input("digite a nota 1:\n"))
    somanota += nota

    media = somanota/6  # calculo de media
os.system('cls')
print(media)

if media > 0 and media < 60:
    print("voce reprovou!")
if media >= 60 and media <= 80:
    print("Parabéns, Você passou!")
if media > 80 and media <= 90:
    print("parabens, voce comeu feijao")
if media > 90 and media <= 100:
    print("parabens, voce comeu arroz e feijao")
else:
    print("invalido")
