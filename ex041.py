# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade

a= int(input('Ano de Nascimento: '))
idade= 2026-a

print('O atleta tem {} anos.'.format(idade))
if idade<=9:
    print('Classificação: \033[34mMIRIM\033[m')
elif idade>9 and idade<=14:
    print('Classificação: \033[34mINFANTIL\033[m')
elif idade>14 and idade<=19:
    print('Classificação: \033[34mJÚNIOR\033[m')
elif idade>19 and idade<=25:
    print('Classificação: \033[34mSENIOR\033[m')
elif idade>25:
    print('Classificação: \033[34mMASTER\033[m')