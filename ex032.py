#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
an= int(input('Que ano voce quer analisar? Coloque 0 para analisar o ano atual: '))
if an == 0:
    an= date.today().year
if an % 4 == 0 and an % 100 != 0 or an % 400 == 0:
    print('O ano \033[35m{}\033[m é BISSEXTO!'.format(an))
else:
    print('O ano \033[35m{}\033[m \033[31mNÃO\033[m é BISSEXTO!'.format(an))