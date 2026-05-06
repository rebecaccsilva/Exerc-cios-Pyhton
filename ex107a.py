# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumento(n=0, taxa=0, format=False):
    au = (taxa / 100 * n) + n
    # print(f'Aumentando {taxa}%, temos R${au:.2f}')
    return au if format is False else moeda(au)


def dobro(n=0, format=False):
    d = 2 * n
    # print(f'O dobro de R${n:.2f} é R${d:.2f}')
    return d if format is False else moeda(d)


def metade(n=0, format=False):
    me = n / 2
    # print(f'A metade de R${n:.2f} é R${me:.2f}')
    return me if format is False else moeda(me)


def desconto(n=0, taxa=0, format=False):
    des = n - (taxa / 100 * n)
    return des if format is False else moeda(des)


def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:>.2f}".replace(".", ",")
