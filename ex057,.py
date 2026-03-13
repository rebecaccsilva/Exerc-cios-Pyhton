# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

r= str(input('Digite o seu sexo[M/F]: ')).strip.upper()[0]

while r!= 'F' and r!='M':
    r=str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0]

print('Sexo {} registrado com sucesso!'.format(r))
