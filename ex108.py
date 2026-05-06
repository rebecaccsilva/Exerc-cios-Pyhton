# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import ex107a

valor = float(input("Digite o valor: R$"))

print(f"Aumentando 20%, temos {ex107a.moeda(ex107a.aumento(valor,20))}")
print(f"O dobro de R${valor} é {ex107a.moeda(ex107a.dobro(valor))}")
print(f"A metade de R${valor} é {ex107a.moeda(ex107a.metade(valor))}")