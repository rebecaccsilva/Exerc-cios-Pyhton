#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120


import math
#1 IMPORT
from math import factorial
n= int(input('Digite um número para \ncalcular o seu Fatorial:  '))
f= math.factorial(n)

print('O fatorial de {} é {}'.format(n,f))


#2 WHILE
n2= int(input('Digite um número para \ncalcular o seu Fatorial:  '))
c= n2
f2= 1

print('Calculando {}! = '.format(n2), end='')

while c>0:
    print('{}'.format(c), end='')
    print(' x 'if c>1 else ' = ', end='')
    f2 *= c
    c-=1
print(f2)


#3 FOR
n3 = int(input('Digite um número para saber o fatorial: '))
f3 = 1
for i in range(1, n3 + 1):
    f3 *= i
print(f'O resultado de {n3}! é {f3}')
