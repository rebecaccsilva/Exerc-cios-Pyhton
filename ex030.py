#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n= int(input('Escreva um número qualquer: '))
num= n % 2

if num == 0:
    print('O número \033[35m{}\033[m é \033[1;35;40mPAR!\033[m'.format(n))
else:
    print('O número \033[33m{}\033[m é \033[1;33;40mÍMPAR!\033[m'.format(n))