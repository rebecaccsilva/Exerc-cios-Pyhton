from rich import print
from rich.panel import Panel


class Churrasco:
    consumo_padrao=0.4
    preco_padrao_kg=82.40

    def __init__(self, titulo, quant):
        self.titulo=titulo
        self.quant=quant

    
    def __str__(self):
        return f'Esse é {self.titulo} com {self.quant} pessoas participando.'
    
    def calcular_qtd_carn(self) -> float:
        return self.quant * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carn() * Churrasco.preco_padrao_kg
    
    def calcular_custo_pessoa(self) -> float:
        return self.calcular_custo_total() / self.quant

    def analisar(self):
        conteudo= f'Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]'
        conteudo+= f'\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_padrao_kg:,.2f}'
        conteudo+= f'\nRecomendo [yellow]comprar {self.calcular_qtd_carn()}Kg[/] de carne'
        conteudo+= f'\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]'
        conteudo+= f'\nCada pessoa pagará [purple]R${self.calcular_custo_pessoa():,.2f}[/] para participar'
        analise= Panel(conteudo, title=self.titulo, width=60)
        print(analise)


c1=Churrasco('Blablabla',20)
c2= Churrasco('Churrasco Fim de Ano',60)
c1.analisar()
c2.analisar()