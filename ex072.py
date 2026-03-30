#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

números= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

r=''
n=0

while True:
    n=int(input('Digite um número de 0 a 20: '))
    if n>20:
        n=int(input('Tente Novamente! Digite um número de 0 a 20: '))
    print(f'Você digitou o número {números[n]}')
    r=str(input('Deseja continuar [S/N]: ')).upper().strip()
    if r=='N':
        break

print('===FIM!===')