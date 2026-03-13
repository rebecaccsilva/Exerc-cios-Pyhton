#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

nt= int(input('Quantos termos você quer mostrar? '))
print('~'*30)

f1=0
f2=1
print('{} > {}'.format(f1,f2), end='')


cont=3

while cont<=nt:
    f3=f1+f2
    print(' {} >'.format(f3),end='')
    f1=f2
    f2=f3
    cont+=1

print(' FIM')
print('~'*30)
