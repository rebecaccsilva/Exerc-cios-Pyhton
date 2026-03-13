#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-='*20)
print('     GERADOR DE PA (2.0)')
print('-='*20)

pt= int(input('Primeiro Termo:  '))
ra= int(input('Razão: '))
n=1

while n<=10:
    print('{} > '.format(pt), end='')
    pt= pt+ra
    n+=1
print ('FIM')