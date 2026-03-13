l= float(input('Qual a largura da parede? '))
a= float(input('Qua a altura da parede? '))
area = l*a
volume= area/2

print('A dimensão da parede é de {} X {} e a área é de {}m²'. format(l, a, area))
print(' Voce precisará de {} l de tinta para pintar a parede toda.'.format(volume))