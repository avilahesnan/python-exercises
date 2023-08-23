class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, value):
        self.__nome = value

    def get_idade(self):
        return self.__idade

    def set_idade(self, value):
        self.__idade = value

    def get_altura(self):
        return self.__altura

    def set_altura(self, value):
        self.__altura = value

    def dados(self):
        print(f'{self.__nome} com {self.__idade} anos e {self.__altura}cm de altura')


pessoa1 = Pessoa('Hesnan', 23, 175)
pessoa1.dados()
