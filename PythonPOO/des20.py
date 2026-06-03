from rich import print
from rich.panel import Panel
from rich import inspect


class Gamer:
    def __init__(self, nome, nick):
        self.real_name = nome
        self.nick = nick
        self.fav = list()

    def add_fav(self, jogo):
        self.fav.append(jogo)
        self.fav = sorted(self.fav, key=str.lower)

    def ficha(self):
        conteudo = f"Nome Real: [white on black]{self.real_name}[/]"
        conteudo += f"\nJogos favoritos: "
        for num, game in enumerate(self.fav):
            conteudo += f"\n:video_game: [purple]{game}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)


j1= Gamer('Rebeca Silva', 'RBCCCS')
j1.add_fav('The Last of Us')
j1.add_fav('Minecraft')
j1.add_fav('Valorant')
j1.ficha()