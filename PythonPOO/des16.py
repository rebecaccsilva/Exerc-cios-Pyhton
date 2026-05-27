from rich import print
from rich import inspect
class Funcionário:
    """
    Cadastra Nome, Setor e Cargo de funcionário e permite que o funcionário se apresente
    """
    empresa= 'Beca Interprise'
    def __init__(self,n,s,c):
        self.nome= n
        self.setor= s
        self.cargo= c

    def apresentação(self) -> str:
        return f'Olá, sou [green]{self.nome}[/] e sou [black]{self.cargo}[/] do setor de [blue]{self.setor}[/] da empresa [purple]{self.__class__.empresa}[/]'
    

f1=Funcionário('Jorge', 'Vendas', 'Gerente')
f1.empresa='Marisa'
print(f1.apresentação())
inspect(f1)


f2= Funcionário('Maria', 'Administração', 'Diretora')
print(f2.apresentação())