#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
n= input('Digite seu nome completo: ').strip().title()

print('Seu nome tem Silva? {}'.format('Silva' in n))