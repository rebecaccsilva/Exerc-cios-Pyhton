#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

i=md=mv=h=0
r=s=' '

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    i= int(input('Idade: '))
    s= str(input('Sexo[M/F]: ')).strip().upper()
    if i>=18:
        md+=1
    if s=='F':
        if i<20:
            mv+=1
    if s=='M':
        h+=1
    r=str(input('Quer continuar?[S/N] ' )).strip().upper()[0]
    if r=='N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {md}.')  
print(f'Ao todo temos {h} homens cadastrados.')  
print(f'E temos {mv} mulheres com menos de 20 anos')