#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
#escada de restos

print('='*30)
print('{:^30}'.format('BANCO LADRÃO'))
print('='*30)

valor=to50=to20=to10=to1=0

valor= float(input('Qual valor você deseja sacar? R$'))
to50= valor//50
to20= (valor%50)//20
to10= ((valor%50)%20)//10
to1= (((valor%50)%20)%10)//1

print(f'Total de {to50} cédulas de R$50')
print(f'Total de {to20} cédulas de R$20')
print(f'Total de {to10} cédulas de R$10')
print(f'Total de {to1} cédulas de R$1')
print('='*30)
print('Volte sempre ao Banco Ladrão!! Tenha um bom dia!')