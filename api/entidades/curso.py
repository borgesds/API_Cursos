class Curso():
    def __init__(self, nome, descricao, data_publicacao):
        self.__nome = nome
        self.__descricao = descricao
        self.__data_publicacao = data_publicacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @nome.setter
    def nome(self, descricao):
        self.__descricao = descricao

    @property
    def data_publicacao(self):
        return self.__data_publicacao

    @nome.setter
    def nome(self, data_publicacao):
        self.__data_publicacao = data_publicacao

