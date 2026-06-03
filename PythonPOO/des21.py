from rich import print


class Caneta:
    def __init__(self, cor):
        self.tampada = True
        # 1.
        # if self.tinta.lower() == "azul":
        # self.tinta = "blue"
        # elif self.tinta.lower() == "vermelho":
        # self.tinta = "red"
        # elif self.tinta.lower() == "verde":
        # self.tinta = "green"
        # elif self.tinta.lower() == "roxo":
        #   self.tinta = "purple"
        # elif self.tinta.lower() == "amarelo":
        #   self.tinta = "yellow"
        # elif self.tinta.lower() == "preto":
        #   self.tinta = "black"

        # 2.
        tradutor_cores = {
            "azul": "[blue]",
            "vermelho": "[red]",
            "verde": "[green]",
            "roxo": "[purple]",
            "amarelo": "[yellow]",
            "rosa":"[magenta]",
            "branco":"[white]"
        }
        cor_comum = cor.lower()
        self.tinta = tradutor_cores.get(cor_comum, "unknown")

    def destampar(self):
        self.tampada = False

    def tampar(self):
        if self.tampada== True:
            print(f'A {self.tinta}caneta[/] já está tampada!!')
        else: 
            self.tampada = True

    def quebrar_linha(self, li):
        print("\n" * li, end="")

    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.tinta}caneta[/] está tampada!")
        else:
            print(f"{self.tinta}{msg}[/]", end="  ")


c1 = Caneta("amarelo")
c1.tampar()
c1.escrever("Hellow World")
c2 = Caneta("rosa")
c2.destampar()
c1.quebrar_linha(3)
c2.escrever("Blebleblubla")

c3= Caneta("rosa")
c3.destampar()
c3.quebrar_linha(2)
c3.escrever('Oi denilson')

