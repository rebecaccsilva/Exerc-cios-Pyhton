#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d= float(input('Quantos KM voce percorrerá? '))
a= d*0.50
b= d*0.45

if d<=200:
    print('Com \033[33m{}km\033[m, a passagem será de \033[31mR${:.2f}\033[m'.format(d,a))
else:
    print('Com \033[33m{}Km\033[m, a passagem será de \033[31mR${:.2f}\033[m'.format(d,b))
print('\033[1;32mBoa viagem!')