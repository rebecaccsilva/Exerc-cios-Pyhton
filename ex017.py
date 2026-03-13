#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

#1
co= float(input('Comprimento do cateto oposto: '))
ca= float(input('Comprimento do cateto adjacente: '))
hi= ca**2 + co**2
h= hi**(1/2)
print('A hipotenusa é {:.2f}'.format(h))


#2
co= float(input('Comprimento do cateto oposto: '))
ca= float(input('Comprimento do cateto adjacente: '))
h= math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(h))