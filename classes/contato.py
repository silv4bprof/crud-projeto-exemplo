class Contato:
    # __slots__ = ['__id_contato', '__nome', '__telefone', '__email']

    def __init__(
            self,
            id_contato: int,
            nome: str,
            telefone: str,
            email: str
    ):
        self.__id_contato = id_contato
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    # Properties (getter) vêm antes de Setters (setter)

    def get_id_contato(self):
        return self.__id_contato

    def set_id_contato(self, id_contato):
        self.__id_contato = id_contato

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome.lower()

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, nome):
        self.__telefone = nome.lower()

    def get_email(self):
        return self.__email

    def set_email(self, nome):
        self.__email = nome.lower()

    def descreve_contato(self):
        pass
