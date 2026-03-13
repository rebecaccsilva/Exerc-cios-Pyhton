#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens= ('Pedra', 'Papel','Tesoura' )
computador= randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jo= int(input('Qual é a sua jogada? '))
print('''JO
KEN
PO!!!''')

print('-='*20)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador jogou 2{}'.format(itens[jo]))
print('-='*20)

if computador==0:
    if jo==0:
        print('EMPATE')
    elif jo==1:
        print('JOGADOR VENCEU!')
    elif jo==2:
        print('COMPUTADOR VENCEU!!')
elif computador==1:
    if jo==0:
        print('COMPUTADOR VENCEU!!')
    elif jo==1:
        print('EMPATE')
    elif jo==2:
        print('JOGADOR VENCEU!')
elif computador==2:
    if jo==0:
        print('JOGADOR VENCEU!')
    elif jo==1:
        print('COMPUTADOR VNECEU!!')
    elif jo==2:
        print('EMPATE')