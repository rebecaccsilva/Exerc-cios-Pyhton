#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

num=[]

for c in range(0,5):
    n=int(input('Digite um valor: '))
    #verifica se é maior que último da lista, se sim, é colocado no final
    if c==0 or n > num[-1]:
        num.append(n)
        print(f'Adicionado ao final da lista....')
    #verifica se é menor que o primeiro, se sim, é colocado no início
    #se não, ele verifica todas as posições até achar a que o n é menor e coloca na posição
    else:
        pos=0
        while pos < len(num):
            if n<= num[pos]:
                num.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1

print('~-'*45)
print(f'Os valores obtidos foram {num}')