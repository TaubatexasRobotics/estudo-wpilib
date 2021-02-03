class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.vel = 0

    def cumprimentar(self):
        print('Olá! Seu nome é:', self.nome)
        print('Sua idade é:', self.idade)
    
    def getVel(self):
        return self.vel
   
class Jovem(Pessoa):
    def __init__(self, nome, idade):
        self.vel = 10

class Idoso(Pessoa):
    def __init__(self, nome, idade):
        self.vel = 5

'''
a = input('Qual é seu nome: ')
b = int(input('Qual é sua idade: '))

p1 = Pessoa(a, b)
p1.cumprimentar()
'''

j = Jovem('Samuel', 16)
i = Idoso('João', 62)

print(j.getVel())
print(i.getVel())
