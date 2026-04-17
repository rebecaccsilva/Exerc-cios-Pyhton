#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

#PODE SER ASSIM TBM
li=[randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
print(li)
print('-='*25)

def sorteia(lst):
    print('Sorteando 5 números da lista: ', end='')
    for cont in range(0,5):
        n=randint(1,10)
        lst.append(n)
        print(f'{n} ', end=' ', flush=True)
    print('PRONTO!')


def somaPar(lst):
    soma=0 
    for valor in lst:
        if valor%2==0:
            soma+=valor
    print(f'Somando os pares de {lst}, temos {soma}')


números=list()
sorteia(números)
somaPar(números)