#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

si=0
muve=0
idhove=0
nohove=0
for p in range(1,5):
    print('====={}ªPESSOA====='.format(p))
    n=str(input('Nome: ')).strip()
    i=int(input('Idade: '))
    s=str(input('Sexo[M/F]: ')).upper()
    si+=i
    if s=='F':
        if i<20:
            muve+=1
    if s=='M' and p==1:
        idhove= i
        nohove= n
    if s=='M' and i>idhove:
        idhove= i
        nohove= n
media=si/4

print('\nA média das idades é do grupo é de {:.1f}.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idhove, nohove))
print('Ao todo são {} mulheres com menos de 20.'.format(muve))

