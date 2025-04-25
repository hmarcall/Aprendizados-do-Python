class Funcionario:
    def trabalhar(self):
        print ('Trabalhando...')

class Programador(Funcionario):
    def trabalhar(self):
        print ('Programando...')

class Designer(Funcionario):
    def trabalhar(self):
        print('Criando um Design...')

emprego=[Funcionario(), Programador(), Designer()]
for i in emprego:
    i.trabalhar()     