from pessoa import Pessoa
from prof import Professor
from aluno import Aluno
from funcadiministrativo import FuncAdiministrativo
nome = input("Digite o nome do seu indivíduo: ")
idade = int(input("Digite a idade do seu indivíduo: "))

p = Pessoa(nome, idade)

nome = input ("Digite o nome do professor: ")
idade = int(input("Digite a idade do professor: "))
disciplina = input("Digite a disciplina ensinada pelo professor: ")

pr = Professor(nome, idade, disciplina)

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
matricula = input("Digite o número da matrícula do aluo: ")

a = Aluno(nome, idade, matricula)

nome = input('Diga o nome do funcionário: ')
idade = int(input("Diga a idade do funcionário: "))
cargo = input("Diga o cargo do funcionário: ")

f = FuncAdiministrativo(nome, idade, cargo)

alt = ''

while (alt!='s'):
       alt = input("Qual indivíduo você deseja verificar? pe - pessoa; pr - professor; a - aluno; f - funcionário; s - fechar: ")
       if (alt == 'pe'):
              print(Pessoa.infoP(p))
       elif (alt =='pr'):
              print(pr.info_p(nome, idade, disciplina))
       elif (alt == 'a'):
              print(Aluno.infoA(a))
       elif (alt == 'f'):
              print(f.info_p(nome, idade, cargo))
       elif (alt == 's'):
              print ('Fechando programa. ')
       else:
              print ("Erro. ")
              