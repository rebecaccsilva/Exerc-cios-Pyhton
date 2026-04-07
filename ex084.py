#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

geral=list()
pessoas= list()

mai=men=0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(geral)==0:
        mai = men = pessoas[1]
    else: 
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    geral.append(pessoas[:])
    pessoas.clear()
    r= str(input('Deseja continuar[S/N]? ')).upper()
    if r=='N':
        break

print(f'Ao todo, você cadastrou {len(geral)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in geral:
    if p[1] == mai:
        print(f' [{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in geral:
    if p[1] == men:
        print(f' [{p[0]}] ',end='')