# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumento(n=0, taxa=0):
    au = (taxa / 100 * n) + n
    # print(f'Aumentando {taxa}%, temos R${au:.2f}')
    return au


def dobro(n=0):
    d = 2 * n
    # print(f'O dobro de R${n:.2f} é R${d:.2f}')
    return d


def metade(n=0):
    me = n / 2
    # print(f'A metade de R${n:.2f} é R${me:.2f}')
    return me


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')