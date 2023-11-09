import os

os.system('cls')


nome = input("Digite seu nome: ")


limite_minimo = 100000000
limite_maximo = 999999999

while True:
    doc = input("Digite seu CPF: ")
    numero = int(doc)

    if limite_minimo <= numero <= limite_maximo:
        print("CPF válido dentro dos limites.")
        break
    else:
        print("CPF fora dos limites. Tente novamente.")

somanota = 0

for i in range(1, 7):
    nota = float(input(f"Digite a nota {i}: "))
    somanota += nota

media = somanota / 6  # Cálculo da média

os.system('cls')

print(f"Média: {media}")

if media > 0 and media < 60:
    print("Você reprovou!")
elif media >= 60 and media <= 80:
    print("Parabéns, você passou!")
elif media > 80 and media <= 90:
    print("Parabéns, você comeu feijão!")
elif media > 90 and media <= 100:
    print("Parabéns, você comeu arroz e feijão!")
else:
    print("Média inválida")
