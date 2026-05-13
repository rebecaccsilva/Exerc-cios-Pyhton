from time import sleep
from ex115.lib.arquivo import *

#def ver():

    
def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except(ValueError, TypeError):
            print("\033[1;31mERRO!! Por favor, digite um número INTEIRO válido.\033[m")
        except(KeyboardInterrupt):
            ("\033[1;31mERRO!! Por favor, digite um número INTEIRO válido.\033[m")
            return 0
        else:
            return n


def linha(tam=40):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc= leiaInt('\033[32mSua opção: \033[m')
    return opc




    """def menu(lista): 
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
        print('='*40)"""