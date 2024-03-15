import pessoa

class Professor(pessoa):
    def __init__ (self, nome, idade, disciplina):
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina
    def info_p(self,nome,idade,disciplina):
        return print (f'O nome desse professor é {nome}\n'
                      f'Tem {idade} anos\n'
                      f'Trabalha na disciplina de {disciplina}')