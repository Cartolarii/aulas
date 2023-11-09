nota1 = float(input("digite a nota 1:\n"))  # entrada de dados com conversão
nota2 = float(input("digite a nota 2:\n"))
nota3 = float(input("digite a nota 3:\n"))
nota4 = float(input("digite a nota 4:\n"))

media = (nota1+nota2+nota3+nota4)/4  # calculo de media

print(media)

if media >= 60:
    print("Parabéns, Você passou!")
else:
    print("re pro va do")
