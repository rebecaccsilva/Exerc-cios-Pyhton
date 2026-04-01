#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista= []
pares=[]
impar=[]

while True:
    n=int(input('Digite um valor: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impar.append(n)
    r=str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if r=='N':
        break

print('~_~'*45)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impar}')