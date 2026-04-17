# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# 1
def area(lst):
    ar = a * b
    print(f"A área de um terreno de {a}m de comprimento e {b}m de largura é {ar}m2")


valores = list()
print(" Controle de Terrenos ")
print("-" * 45)
a = float(input("COMPRIMENTO (m): "))
b = float(input("LARGURA (m): "))
valores.append([a, b])
area(valores)


# 2
def area2(a, b):
    ar = a * b
    print(f"A área de um terreno de {a}m de comprimento e {b}m de largura é {ar}m2")


print(" Controle de Terrenos ")
print("-" * 45)
co = float(input("COMPRIMENTO (m): "))
la = float(input("LARGURA (m): "))
area2(co, la)
