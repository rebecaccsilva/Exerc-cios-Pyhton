#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista=[]
mai=men=0

for n in range(0,5):
    lista.append(int(input(f'Digite um valor pra a Posição {n} : ')))
    if n==0:
        mai=men=lista[n]
    else:
        if lista[n]>mai:
            mai=lista[n]
        if lista[n]<men:
            men=lista[n]

print('-'*45)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(lista):
    if v==mai:
        print(f'{i}...', end='')
        
print(f'\nO menor valor digitado foi {men} nas posições ',end='')
for i, v in enumerate(lista):
    if v==men:
        print(f'{i}...',end='')