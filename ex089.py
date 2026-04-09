#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

fi=list()

while True:
    nome= str(input('Nome: '))
    n1= float(input('Nota 1: '))
    n2= float(input('Nota 2: '))
    media= (n1+n2)/2
    fi.append([nome,[n1,n2],media])
    r= str(input('Quer continuar[S/N]? ')).upper()
    if r=='N':
        break

print('-='*45)
print(f'{"No.":<4}{'NOME':<10}{'MEDIA':>8}')
print('-='*45)
for i,a in enumerate(fi):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*45)
    opc=int(input('Mostrar notas de qual aluno(999 interrope)? '))
    if opc==999:
        print('Finalizando.....')
        break
    if opc<=len(fi)-1:
        print(f'Notas de {fi[opc][0]} são {fi[opc][1]}')
print('<<<<  VOLTE SEMPRE  >>>>')