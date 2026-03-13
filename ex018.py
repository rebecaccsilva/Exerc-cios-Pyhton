#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n= float(input('Digite o ângulo que você deseja: '))
sen= math.sin(math.radians(n))
cos= math.cos(math.radians(n))
tan= math.tan(math.radians(n))

print('O SENO de {} é {:.2f}'.format(n, sen))
print('O COSSENO de {} é {:.2f}'.format(n,cos))
print('A TANGENTE de {} é {:.2f}'.format(n,tan))
