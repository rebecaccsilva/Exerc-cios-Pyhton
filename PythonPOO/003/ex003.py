class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(
            f"\033[1;33mConta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}\033[m"
        )

    def depositar(self, valor):
        self.saldo += valor
        print(
            f"\033[1;32mDepósito de R${valor:,.2f} autorizado na conta {self.id}.\033[m"
        )

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f"\033[1;31mSAQUE NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE!!\033[m"
            )
        else:
            self.saldo -= valor
            print(
                f"\033[1;32mSaque de R${valor:,.2f} autorizado na conta {self.id}.\033[m "
            )

    def __str__(self):
        return f"\033[1;35mA conta {self.id} de {self.nome} tem R${self.saldo:,.2f} de saldo.\033[m"


c1 = ContaBancaria(1654, "Rebeca", 8956)
c1.depositar(20)
c1.sacar(265)
c1.sacar(5000000)
print(c1)
