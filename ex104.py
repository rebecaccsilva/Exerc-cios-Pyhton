#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        n= str(input(f'{msg}'))
        if n.isnumeric():
            print(f'Você digitou o número {n}!')
            print('===FIM===')
            break
        else:
            print('\033[1;31mERRO! Isso não é um número!! Digite novamente.\033[m')



n= leiaInt('Digite um número: ')