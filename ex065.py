#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = cont = soma = maior = menor =  0
r= 'S'

while r!='N':
    n= int(input('Digite um número: '))
    soma+=n
    cont+=1
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    r= str(input('Quer continuar? [S/N] ')).upper().strip()
media=soma/cont

print('Você digitou {} números e a média foi {}'.format(cont,media))
print('O maior foi {} e o menor foi {}'.format(maior,menor))
