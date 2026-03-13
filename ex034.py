#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sa= float(input('Qual é o salário do funcionário? '))
au1= sa + (10/100*sa)
au2= sa + (15/100*sa)

if sa>1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sa,au1))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sa,au2))