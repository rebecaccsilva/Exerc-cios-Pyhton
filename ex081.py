#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

val=list()

while True: 
    n=int(input('Digite um valor: '))
    val.append(n)
    r=str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if r=='N':
        break
    
print('~_~'*45)
print(f'Você digitou {len(val)} elementos')
print(f'Os valores em ordem decrescente são {sorted(val, reverse=True)}')
if 5 in val:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
