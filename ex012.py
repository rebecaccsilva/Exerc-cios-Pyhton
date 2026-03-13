p= float(input('Digite o preço do produto: R$ '))
d= 0.05*p
pd= p-d
print ('O valor do produto era R${}, mas foi aplicado um desconto de 5%, logo o novo valor é de R${}'.format(p, pd))