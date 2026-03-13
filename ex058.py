#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

print('--=--'*20)
print('Vou escolher um número entre 0 e 10. tente adivinhar...\n(VERSÃO 2.0)')
print('--=--'*20)

rc= randint(0,10)

ru= int(input('Qual o seu palpite? '))

tent=1

while ru!=rc:
    tent+=1
    if ru<rc:
        ru= print('Mais... Tente mais uma vez.')
    else:
        ru= print('Menos... Tente mais uma vez.')
    ru= int(input('Qual é o seu palpite? '))

print('\nAcertou com {} tentativas. PARABÉNS!'.format(tent))