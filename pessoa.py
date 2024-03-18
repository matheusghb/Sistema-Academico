class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def infoP(self):
        return print (f'Nome: {self.nome}\n'
                      f'Idade: {self.idade}')