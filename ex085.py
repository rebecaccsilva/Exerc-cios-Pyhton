#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num=list()
pares=list()
impares=list()
nu=list()

for n in range(1,8):
    nu.append(int(input(f'Digite o {n}º número:')))
    if nu[0]%2==0:
        pares.append(nu[0])
    else:
        impares.append((nu[0]))
    num.append(nu[:])
    nu.clear()
    
print(f'Os valores digitados foram {sorted(num)}')
print(f'Os valores \033[1;31mpares\033[m foram: {sorted(pares)}')
print(f'Os valores \033[1;35mímpares\033[m foram: {sorted(impares)}')