#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

contm=0
contn=0
for i in range(0,7):
    a=int(input('Em que ano a {}ª pessoa nasceu?'.format(i+1)))
    id=2026-a
    if id>21:
        contm+=1
    else:
        contn+=1

print('\nAo todo tivemos {} pessoas maiores de idade.'.format(contm))
print('E também tivemos {} pessoas menores de idade.'.format(contn))