#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
p= input('Digite uma frase: ').strip().upper()

print('A letra A aparece {} vezes na frase.'.format(p.count('A')))
print('A priemira letra A apareceu na posição {}'.format(p.find('A')+1))
print('A última letra A apareceu na posição {}'.format(p.rfind('A')+1))