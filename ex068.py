#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
import time

c=0
u=0
s=0

while True:
    u=int(input('Diga um valor: '))
    c=randint(0,10)
    s=u+c
    r=' '
    while r not in 'PI':
        r=str(input('Par ou Ímpar[P/I]: ')).upper()[0]
    print(f'Você jogou {u} e o computador {c}. Total de {s}')
    print(f'Deu PAR!'if s%2==0 else 'Deu ÍMPAR!')
    if r=='P':
        if s%2==0:
            print('Você Venceu!!!')
            v+=1
        else:
            print('Você Perdeu!')
            break
    elif r == "I":
        if s%2==0:
            print('Você Perdeu!!')
            break
        else:
            print('Você Venceu!!!')
    print('Vamos jogar novamente...')
    time.sleep(2)