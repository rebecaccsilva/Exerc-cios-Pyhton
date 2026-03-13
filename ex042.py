#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
l1= float(input('Primeiro segmento: '))
l2= float(input('Segundo segmento: '))
l3= float(input('Terceiro segmento: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Os segmentos acima PODEM formar um triangulo ', end='')
    if l1==l2 and l2==l3:
        print('EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos acima NÃO PODEM formar triangulo!!')