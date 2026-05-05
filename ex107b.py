# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import ex107a

valor = float(input("Digite o valor: R$"))

ex107a.aumento(valor, 20)  #1
print(f"Aumentando 20%, temos R${ex107a.aumento(valor,20)}") #2

ex107a.dobro(valor)  #1
print(f"O dobro de R${valor} é R${ex107a.dobro(valor)}")  #2

ex107a.metade(valor)  #1
print(f"A metade de R${valor} é R${ex107a.metade(valor)}")  #2
