#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('==*=='*20)
print('ANALISADOR DE TRIANGULOS')
print('==*=='*20)

r1= float(input('Primeiro Segmento: '))
r2= float(input('Segundo Segmento: '))
r3= float(input('Terceiro Segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima \033[32mPODEM\033[m formar um Triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um Triângulo!!')