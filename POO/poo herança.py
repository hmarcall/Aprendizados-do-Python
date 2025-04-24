class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    def mostrar_dados(self):
        print(f'Nome: {self.nome}, Salário: {self._salario}')


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, departamento)
        self.departamento = departamento
  

    def exibir_dados(self):
        print(f'Nome: {self.nome}, Departamento: {self.departamento}')

nome1 = Gerente('Henrique', 1000,'Gerente')
nome1.exibir_dados()