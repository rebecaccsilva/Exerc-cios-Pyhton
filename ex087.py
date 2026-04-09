#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna
#C) O maior valor da segunda linha.

matriz= [[0,0,0],[0,0,0],[0,0,0]]
pares=0
ter=0
mai=0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c]%2==0:
            pares += matriz[l][c]
        if c==2:
            ter += matriz[l][c]
        if c == 0:
            mai = matriz[1][c]
        elif matriz[1][c]>mai:
            mai= matriz[1][c]   
print('-='*35)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {ter}'),
print(f'O maior valor da segunda linha é {mai}')