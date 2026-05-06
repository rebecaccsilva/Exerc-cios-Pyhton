
def aumento(n=0, taxaa=0, format=False):
    au = (taxaa / 100 * n) + n
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


def desconto(n=0, taxad=0, format=False):
    des = n - (taxad / 100 * n)
    return des if format is False else moeda(des)


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:>.2f}".replace(".", ",")


def resumo(n=0, taxaa=0, taxad=0):
    print('='*50)
    print(f'RESUMO DO VALOR '.center(50))
    print('='*50)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'{taxaa}% de aumento: \t{aumento(n,taxaa,True):.>6}')
    print(f'{taxad}% de desconto: \t{desconto(n,taxad,True)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print('-'*50)

