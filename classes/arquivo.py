from io import TextIOWrapper


class Arquivo:
    __slots__ = ['__name_file', '__operation', '__encoding']

    def __init__(
            self,
            name_file,
            operation,
            encoding='utf-8'
    ):
        self.__name_file = name_file
        self.__operation = operation
        self.__encoding = encoding

    # operações dos arquivos
    def abrir_arquivo(self):
        return open(self.__name_file, self.__operation, encoding=self.__encoding)

    def fechar_arquivo(self, arquivo: TextIOWrapper):
        arquivo.close()
