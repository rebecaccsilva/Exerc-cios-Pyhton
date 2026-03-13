#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano= int(input('Ano de nascimento: '))
idade= 2026-ano

print('Quem nasceu em {} tem \033[34m{} anos\033[m em 2026.'.format(ano, idade))

if idade<18:
    print('Relaxa...Ainda faltam {} anos para o seu alistamento.'.format(18-idade))
    print('Seu alistamento será em \033[34m{}\033[m'.format(2026+(18-idade)))
elif idade>18:
    print('Você já deveria ter se alistado há \033[1;31m{}\033[m anos!!'.format(idade-18))
    print('Seu alistamento foi em \033[31m{}\033[m.'.format(2026-(idade-18)))
elif idade==18:
    print('Você tem que se alistar \033[1;32mIMEDIATAMENTE\033[m!!!')