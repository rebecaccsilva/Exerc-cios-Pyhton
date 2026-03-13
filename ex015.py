q= float(input('Quantos Km voce percorreu? '))
d= float(input('Quantos dias voce percorreu? '))
qi= q*0.15
di= d*60
t= qi+di
print('Você percorreu {}Km por {} dias, logo o total a pagar é de R${}'.format(q,d,t))