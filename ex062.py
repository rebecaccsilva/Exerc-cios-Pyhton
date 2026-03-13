#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-='*20)
print('     GERADOR DE PA (3.0)')
print('-='*20)

pt= int(input('Primeiro Termo:  '))
ra= int(input('Razão: '))
n=1
total=0
mais = 10

while mais!=0:
    total= total+mais
    while n<=total:
        print('{} > '.format(pt), end='')
        pt= pt+ra
        n+=1
    print('PAUSA')
    mais= int(input('Quantos termos voce quer mostrar a mais? '))
print ('Progressão finalizada com {} termos mostrados.'.format(total))