# Crie um programa que leia dois valores e mostre um menu na tela
import time

n1= float(input('Primeiro Valor: '))
n2= float(input('Segundo valor: '))

r=0

while r!=5:
    r = int(input('''=-==-==-==-==-==-==-==-==-==-==-=
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    >>>>>>>> Qual é a sua opção? '''))
    time.sleep(1)
    if r==1:
        print('A soma entre {} + {} é {}'.format(n1,n2,n1+n2))
    elif r==2:
        print('O resultado de {} X {} é {}'. format(n1,n2,n1*n2))
    elif r==3:
        if n1<n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
        elif n1==n2:
            print('Eles são iguais!')
        else:
            print('Entre {} e {} o maior é {}'.format(n1,n2,n1))
    elif r==4:
        print('Informe os números novamente: ')
        n1= float(input('Primeiro Valor: '))
        n2= float(input('Segundo valor:  '))
    elif r>5 or r==0:
        print('Opção inválida. Tente novamente')

print('Finalizando...')
time.sleep(2)
print('=-='*11)
print('Fim do programa! Volte Sempre!')
