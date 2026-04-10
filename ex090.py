#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

alunos={}

alunos['nome']= str(input('Nome: '))
alunos['media']= float(input(f'Média de {alunos['nome']}: '))
if alunos['media']>=7:
    alunos['situação']='Aprovado!'
elif 5 <= alunos['media'] <7:
    alunos['situação']='Recuperação'
else:
    alunos['situação']='Reprovado!!'
    
print('-='*45)
for k,v in alunos.items():
    print(f'{k} é igual a {v}')