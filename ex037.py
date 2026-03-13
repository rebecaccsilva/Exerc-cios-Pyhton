#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('>'*35)
print('    \033[1;36mCONVERSOR DE NÚMEROS\033[m    ')
print('<'*35)

n= int(input('Digite um número: '))
escolha= int(input('Qual conversão voce deseja?\n \033[34m1---Binário\033[m\n \033[35m2---Octal\033[m\n \033[31m3---Hexadecimal\033[m\n ==> '))

if escolha==1:
    print('O número {} em \033[1;34mBINÁRIO\033[m é {}'.format(n, bin(n)[2:]))
elif escolha==2:
    print('O número {} em \033[1;35mOCTAL\033[m é {}.'.format(n, oct(n)[2:]))
elif escolha==3:
    print('O número {} em \033[1;31mHEXADECIMAL\033[m é {}.'.format(n, hex(n)[2:]))
