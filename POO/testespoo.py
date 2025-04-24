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

class Gerente(Funcionario):
    def __init__(self, nome, salario, senha, departamento):
        super().__init__(nome, senha, departamento)
        self.departamento = departamento
  

    def exibir_dados(self):
        print(f'Nome: {self.nome}, Departamento: {self.departamento}')

nome1 = Gerente('Henrique', 1000, '123','Gerente')
nome1.exibir_dados()
nome1.verificar_senha('123')
print(nome1._Funcionario__senha)