# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros=list()

while True:
    n=int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.....')
    else:
        print(f'O número {n} já está na lista!!')
    r=str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if r=='N':
        break
    
print('-='*45)
print(f'Você digitou os valores {sorted(numeros)}')