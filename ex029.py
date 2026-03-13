#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v= float(input('Escreva a velocidade do carro em km/h: '))
m= (v-80)*7

if v>80:
    print('\033[1;31mMULTADO!\033[m \033[31mVoce excedeu o limite permitido de 80km/h\033[m')
    print('\033[1;41m A multa será de R${}.\033[m'.format(m))
else:
    print('\033[32mTudo certo!\033[m')
print('\033[43mTenha um bom dia! Dirija com segurança!\033[m')