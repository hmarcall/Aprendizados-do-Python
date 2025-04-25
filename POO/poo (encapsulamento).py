class Funcionario:
    def __init__(self, nome, salario, senha):
        self.nome = nome
        self._salario = salario
        self.__senha = senha

    def mostrar_dados(self):
        print(f'Nome: {self.nome}, Salário: {self._salario}')

    def verificar_senha(self, senha):
        if senha == self.__senha:
            print("Senha correta!")   
        else:
            print("Senha incorreta!")

login1 = Funcionario('Henrique', 1000, '123456')
login1.mostrar_dados()
login1.verificar_senha('123456')
#print(login1._Funcionario__senha)






        