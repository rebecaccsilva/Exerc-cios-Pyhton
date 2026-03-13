# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n=0

#1
while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    if n<0:
        break
    print('-'*30)
    print(f'{n} X 1 = {n*1}')
    print(f'{n} X 2 = {n*2}')
    print(f'{n} X 1 = {n*3}')
    print(f'{n} X 1 = {n*4}')
    print(f'{n} X 1 = {n*5}')
    print(f'{n} X 1 = {n*6}')
    print(f'{n} X 1 = {n*7}')
    print(f'{n} X 1 = {n*8}')
    print(f'{n} X 1 = {n*9}')
    print(f'{n} X 1 = {n*10}')
    print('-'*30)
print('='*35)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')

#2
while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    if n<0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')