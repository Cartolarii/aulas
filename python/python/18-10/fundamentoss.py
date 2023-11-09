import os
somanotas = 0
for i in range(1, 16):
    nota = float(input(f"digite a nota {i}:\n"))
    somanotas = somanotas+nota
    os.system('cls')

media = somanotas/15

if media >= 70:
    print("Parabéns, voce passou!")
else:
    print("re pro va do cabaço")
