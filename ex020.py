# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a= input('Primeiro aluno: ')
b= input('Segundo aaluno: ')
c= input('Terceiro aluno: ')
d= input('Quarto aluno: ')
lista= [a,b,c,d]
random.shuffle(lista)

print('A ordem será:')
print(lista)

#'shuffle' = embaralhar