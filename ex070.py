# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)

p=tc=mm=vmba=nmba=0
cont=0
r=''
while True:
    np= str(input('Nome do Produto: '))
    va=int(input('Preço: R$'))
    tc+=va
    cont+=1
    if va>1000:
        mm+1
    if cont==1:
        vmba=va
        nmba=np
    else:
        if va<vmba:
            vmba=va
            nmba=np
    r= str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if r=='N':
        break

print('-'*15,'FIM DO PROGRAMA','-'*15)
print(f'O total da compra foi R${tc:.2f}')
print(f'Temos {mm} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi \033[4;32m{nmba}\033[m que custa R${vmba:.2f}')
    