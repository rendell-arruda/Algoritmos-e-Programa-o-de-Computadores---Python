# definir uma entidade Funcionario que possue nome, data de admissão e salário.
# implemente sua classe, definindo tambem alguns metodos para manipulacao dos atributos.
# em seguida considere a entidade Gerente, que tambem é um funcionario. Alem dos atributis
# de funcionario, um gerente tambem contem um bonus, que é uma porcentagem adicional aplicada
# no seu salario.
# Implemente a classe Gerente como uma extensao de Funcionario

class Funcionario:
    def __init__(self, nome=0, data=0, salario=0):
        self.nome = nome
        self.data = data
        self.salario = salario

    def setNome(self):  # ADICIONA/MUDA O NOME DO FUNCIONARIO
        nome = input("Digite o nome do Funcionário: ")
        self.nome = nome

    def setData(self):
        data = str(input("Digite a data de admissão do funcionário:"))
        self.data = data

    def setSalarioBase(self):
        salarioBase = str(input("Digite o salário base do funcionario :"))
        self.salario = salarioBase

    def get(self):
        return self.nome, self.data, self.salario

    def __repr__(self):
        return 'O funcionário ' + self.nome + ' recebe o valor de ' + self.salario + ' reais, e foi adimitido na data de ' + self.data


funci = Funcionario()

funci.nome = "Fred"
funci.data = "10/02/22"