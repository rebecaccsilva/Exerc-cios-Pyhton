#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

s=0
n= int(input('Digite um número para ver sua tabuada: '))
for a in range(0,10):
    s+=n
    print('{} X {:2} = {}'.format(n,a+1,s))