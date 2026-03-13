#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

cont= 0
s=0
for a in range(1,7):
    n=int(input('Digite um número: '))
    if n%2==0:
        s+=n
        cont+= 1
print('A soma dos {} números PARES é {}'.format(cont,s))