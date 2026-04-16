#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
#galera.append(pessoa.copy())

galera=[]
pessoa={}
idades=0

while True:
    pessoa.clear()
    pessoa['nome']= str(input('Nome: '))
    while True:
        pessoa['sexo']= str(input('Sexo[M/F]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO!!! Digite o sexo corretamente!')
    pessoa['idade']= int(input('Idade: '))
    idades+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r= str(input('Quer continuar[S/N]? ')).upper()
        if r in 'SN':
            break
        else:
            print('ERRO!!! Responda corretamente!')
    if r=='N':
        break

mediaid=idades/len(galera)

print('-='*45)
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
print(f'A média de idades é {mediaid:5.2f} anos.')
print('As mulheres cadastradas são ', end='')
for m in galera:
    if m['sexo']=='F':
        print(f'{m["nome"]} ', end='')
print('\nAs pessoas com a idade acima da média são ', end='')
for p in galera:
    if p['idade']>mediaid:
        print(f'{p["nome"]} com {p["idade"]} anos | ', end=' ')

print('\n<<<ENCERRADO>>>')