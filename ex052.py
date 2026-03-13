#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n= int(input('Digite um número: '))
tot= 0
cont= 0

for c in range(1,n+1):
    if n%c==0:
        print('\033[32m', end='')
        tot= tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end=' \033[m')
if tot>2:
    print('\nO número {} foi divisível {} vezes.\nLogo \033[1;33mNÃO\033[m é PRIMO.'.format(n,tot))
else:
    print('\nO número {} foi divisível {} vezes.\nLogo ele \033[36mÉ\033[m PRIMO.'.format(n, tot))