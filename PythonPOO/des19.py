from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo,paginas):
        self.titulo= titulo
        self.paginas= paginas
        self.atual= 1

        print(f":open_book: Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.atual}[/]")


    def avancar_paginas(self, qtd=1):
        cont=0
        for pg in range(0,qtd,1):
            if not self.fim_do_livro():
                self.atual+=1
                print(f'[green] Pág{self.atual}[/] :arrow_forward: ', end='')
                sleep(0.5)
                cont+=1
        print(f'[blue]Você avançou {cont} paginas e agora está na [yellow]página {self.atual}[/][/]')
        if self.fim_do_livro():
            print(f" :closed_book: [red] Você chegou ao final do livro '{self.titulo}' [/]")

    def fim_do_livro(self):
        return True if self.atual == self.paginas else False

livro= Livro('Pequenos', 20)
livro.avancar_paginas(2)
livro.avancar_paginas(15)
livro.avancar_paginas(40)