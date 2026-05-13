# 1 - Vamos criar um menu em Python, usando modularização.
# 2 - Vamos ver como fazer acesso a arquivos usando o Python.
# 3 - Vamos finalizar o projeto de acesso a arquivos em Python.
from ex115.lib.arquivo import *
from ex115.lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta= menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Lista o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar nova pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = str(input('Idade: '))
        cadastro(arq, nome, idade)
    elif resposta == 3:
        #Sair do Sistema
        cabeçalho('Saindo do Sistema.... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)

