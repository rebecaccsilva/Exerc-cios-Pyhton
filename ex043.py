#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela

p= float(input('Qual o seu peso? '))
a= float(input('Qual a sua altura? '))

imc=p/a**2

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print('Você está ABAIXO DO PESO normal!!')
elif imc>=18.5 and imc<25:
    print('Você está com o PESO IDEAL!')
elif 25 <= imc < 30:
    print('Cuidado! Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Voce está OBESO')
elif 40 <= imc:
    print('\033[1;31mCUIDADO1 VOCE JÁ ESTÁ COM OBESIDADE MÓRBIDA!!!\033[m')