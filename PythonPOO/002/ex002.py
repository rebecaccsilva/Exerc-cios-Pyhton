#Declaração de Classe
class Gafanhoto:
    '''
    Essa classe cria um gafanhoto/aluno, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    '''
    def __init__(self, n='vazio', i=0): #Metodo Construtor
        #Atributos de Instancia
        self.nome = n
        self.idade = i

    #Metodos de Instacia
    def aniversario(self):
        self.idade += 1


    def __str__(self):
        return f"{self.nome} é aluno(a) e tem {self.idade} anos de idade!"
    

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

#Declaração de Objeto
g1= Gafanhoto('Maria', 21)
g1.aniversario()   #com parenteses == metodo
print(g1)

g2 = Gafanhoto('Pedro', 15)
print(g2)

g3= Gafanhoto()
g3.nome= 'Vinicius'
print(g3)


print(g3.__doc__) # Dunder Attribute
print(g2.__dict__) # atributo
print(g1.__getstate__()) # metodo
print(g1.__class__)