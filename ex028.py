#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from asyncio import wait
from random import randint
print('--=--'*20)
print('Vou escolher um número entre 0 e 5. tente adivinhar...')
print('--=--'*20)

n= randint(0,5) #faz o computador "pensar"

r= int(input('Em que número eu pensei? '))

if r==n:
    print('Acertou miserávi!')
else:
    print('errou otário! Eu pensei no {} heheheh'.format(n))