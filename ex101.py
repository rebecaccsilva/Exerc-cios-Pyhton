#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

#1
idade=ano=0
def voto():
    ano= int(input('Em que ano você nasceu? '))
    idade= date.today().year - ano
    print(f'Com {idade} anos:', end=' ')
    if idade<16:
        print('NÃO VOTA')
    elif 18>idade>=16:
        print('VOTO OPCIONAL.')
    elif idade>=18:
        print('VOTO OBRIGATÓRIO.')


voto()

#2
def voto(ano):
    idade= date.today().year - ano
    if idade<16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16<= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc= int(input("Em que ano você nasceu? "))
print(voto(nasc))