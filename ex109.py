# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import ex107a

valor = float(input("Digite o valor: R$"))

print(f"Aumentando 20%, temos {ex107a.aumento(valor,20, True)}")
print(f"O dobro de R${valor} é {ex107a.dobro(valor, True)}")
print(f"A metade de R${valor} é {ex107a.metade(valor,True)}")
print(f"Com desconto de 30%, temos {ex107a.desconto(valor,30)}")
