#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
print('='*30)
print('ANÁLISE DE EMPRÉSTIMO')
print('='*30)


va= float(input('Qual o valor da casa? R$'))
sa= float(input('Qual o seu salário? R$'))
tem= int(input('Em quanto anos voce vai pagar? '))

pm= va/(tem*12)

if pm>30/100*sa:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
    print('As parcelas mensais seriam de R${:.2f}'.format(pm))
else:
    print('\033[1;33mTudo certo!\033[m as parcelas mensais serão de R${:.2f}'.format(pm))