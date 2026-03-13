#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a= float(input('Primeiro Valor:'))
b= float(input('Segundo valor:'))
c= float(input('Terceiro Valor:'))

#Quem é o menor
if a<b and a<c:
    menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

#Quem é o maior
if a>b and a>c:
    maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print('O \033[32mMENOR\033[m valor é \033[34m{}\033[m'.format(menor))
print('O \033[31mMAIOR\033[m valor é \033[34m{}\033[m'.format(maior))