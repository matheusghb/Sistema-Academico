class FuncAdiministrativo:
    def __init__ (self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
    def info_p(self,nome,idade,cargo):
        return print (f'O nome desse funcionário é {nome}\n'
                      f'Tem {idade} anos\n'
                      f'Trabalha como {cargo}')
