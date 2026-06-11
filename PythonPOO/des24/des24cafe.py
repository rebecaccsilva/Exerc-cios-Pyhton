from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print("--- Iniciando o Preparo ---")

        self.ferver_agua()
        self.misturar()
        self.servir()

        print("=== Bebida Pronta ===\n")

    def ferver_agua(self):
        print("1. Fervendo a agua a 100°C.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Servindo em xícara pequena")


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Mergulhando o sache de ervas na água.")

    def servir(self):
        print("3. Servindo xícara de porcelana com limão.")


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3.  Servindo em caneca térmica já com café.")
