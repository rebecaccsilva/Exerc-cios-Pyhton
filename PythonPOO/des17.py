from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        conteudo= f'{self.nome.center(30, ' ')}'
        conteudo+= f'{'-'*30}'
        precof= f'R${self.preco:,.2f}'
        conteudo+= f'{precof.center(30,'_')}'
        etiqueta= Panel(conteudo, title='Produto', width=34)
        print(etiqueta)

p1= Produto('Teclado', 345)
p2= Produto('Headset GAmer H398',400)
p1.etiqueta()
p2.etiqueta()
#inspect(Panel)