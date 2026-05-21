#Declaração de Classe
class Gafanhoto:
    def __init__(self): #Metodo Construtor
        #Atributos de Instancia
        self.nome = ""
        self.idade = 0

    #Metodos de Instacia
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é aluno(a) e tem {self.idade} anos de idade!"

#Declaração de Objeto
g1= Gafanhoto()
g1.nome= 'Maria'  #sem parenteses == atributo
g1.idade= 21
g1.aniversario()   #com parenteses == metodo
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome= 'Pedro'
g2.idade= 15
print(g2.mensagem())

g3= Gafanhoto()
g3.idade= 89
g3.aniversario()
g3.nome= 'Vinicius'
print(g3.mensagem())