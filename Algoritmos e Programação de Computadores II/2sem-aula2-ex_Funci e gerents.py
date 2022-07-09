# definir uma entidade Funcionario que possue nome, data de admissão e salário.
# implemente sua classe, definindo tambem alguns metodos para manipulacao dos atributos.
# em seguida considere a entidade Gerente, que tambem é um funcionario. Alem dos atributis
# de funcionario, um gerente tambem contem um bonus, que é uma porcentagem adicional aplicada
# no seu salario.
# Implemente a classe Gerente como uma extensao de Funcionario

class Funcionario:
    def __init__(self, nome=0, data=0, salario_base=0):
        self.nome = nome
        self.data = data
        self.salario_base = salario_base

    def setNome(self):  # ADICIONA/MUDA O NOME DO FUNCIONARIO
        nome = input("Digite o nome do Funcionário: ")
        self.nome = nome

    def setData(self):
        data = str(input("Digite a data de admissão do funcionário:"))
        self.data = data

    def set_salario_base(self):
        salario_base = str(input("Digite o salário base do funcionario :"))
        self.salario_base = salario_base

    def get(self):
        return self.nome, self.data, self.salario_base

    def __repr__(self):
        return '(' + str(self.nome) + ',' + str(self.salario_base) + ',' + str(self.data) + ')'


class Gerente(Funcionario):
    def __init__(self, nome=0, data=0, salario_base=0, salario_bonificado = 0):
        super(Gerente, self).__init__(nome, data, salario_base)
        self.salario_bonificado = salario_bonificado

    def setSalario_bonificado(self):
         self.salario_bonificado = (int(self.salario_base) + int(self.salario_base) * 0, 5)

    def getSalario_bonificafo(self):
        return self.salario_bonificado


funcionario2 = Gerente("Fred", "21/05/22", 5000, 0)


'''
# para testar chamar outra classe chamando para cadastro

class Cadastro:
 
    def __init__(self):
        print("Cadastro de Funcionários")

    while True:
        print("1.Cadastrar")
        print("2.Lista de empregados")
        op = int(input("Digite sua opção"))
        if op == 1:
            Funcionario.setNome(self)
        else

'''
