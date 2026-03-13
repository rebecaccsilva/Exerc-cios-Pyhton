#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*31)
print(' '*5,'10 TERMOS DE UMA PA',' '*5)
print('='*31)

p= int(input('Primeiro termo: '))
r= int(input('Razão: '))

de= p + (10-1) * r

for c in range(p,de,r):
    print(' {}'.format(c), end=' ➡')
print('FIM')