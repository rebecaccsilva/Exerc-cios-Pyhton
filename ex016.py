#crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc

n= float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, math.trunc(n)))

