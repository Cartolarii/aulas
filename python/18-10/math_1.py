import os
numero = int(input("digite o numero desejado:\n"))
os.system('cls')
for i in range(1, 11):
    arroz = numero*i
    print(i, "*", numero, "=", arroz)
