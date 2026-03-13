import random
nums = [0, 1, 2, 3, 4, 5]
n = random.choice(nums)
print('Vou pensar em um número de 0 a 5... Tente adivinhar qual é o número!')

adivinhe = int(input('Qual é o número? '))
if adivinhe == (n):
    print('VOCÊ ACERTOU, PARABÉNS!')
else:
    print('O Computador VENCEU! Eu pensei em {}'.format(n))
