# 1 - Vamos criar um menu em Python, usando modularização.
# 2 - Vamos ver como fazer acesso a arquivos usando o Python.
from time import sleep
from ex115b import *

def ver():
    print('-'*40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-'*40)
    

def cadastro():
    print('-'*40)
    print('Opção 2'.center(40))
    print('-'*40)


def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        ver()
        print(a.read())


def menu(msg):
    print("*-" * 20)
    print("MENU PRINCIPAL".center(40))
    print("*-" * 20)
    print("\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m")
    print("\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m")
    print("\033[33m3\033[m - \033[34mSair do Sistema\033[m")
    print("-" * 40)
    while True:
        try:
            o = int(input(msg))
            if o < 1 or o > 3:
                raise ValueError
        except (ValueError, TypeError):
            print("\033[1;31mERRO!! Por favor, digite uma opção válida.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mERRO!! Por favor, digite um número INTEIRO válido.\033[m")
            continue
        else:
            break
    if o == 1:
        lerArquivo()
    elif o == 2:
        criarArquivo('Cadastro')
    elif o == 3:
        print('='*40)
        print("Saindo do sistema.... Até Logo!".center(40))
        print('='*40)




menu("\033[33mSua opção: \033[m")
