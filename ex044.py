#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
print('='*10, 'LOJAS BECA','='*10)
p= float(input('Preço das compras: R$'))
fp= int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

j=p+(20/100*p)

if fp==1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com desconto de 10%.'.format(p, p-(10/100*p)))
elif fp==2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com desconto de 5%.'.format(p, p-(5/100*p)))
elif fp==3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(p/2))
    print('Sua compra de R${:.2f} continuará custando R${:.2f}.'.format(p,p))
elif fp==4:
    pa=int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(pa,j/pa))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p,j))