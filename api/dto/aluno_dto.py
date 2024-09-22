from enum import property
from dataclasses import dataclass
from datetime import date

@dataclass
class AlunoDTO():

    nome: str
    data_nasc: date

    #O @dataclass BASICAMENTE ESCREVE SOZINHO O CODIGO ABAIXO
    
    # def __init__(self, nome, data_nasc):
    #     self.__nome = nome
    #     self.__data_nasc = data_nasc
    
    # @property
    # def nome(self):
    #     return self.__nome
    
    # @nome.setter
    # def nome(self, nome):
    #     self.__nome = nome

    # @property
    # def data_nasc(self):
    #     return self.__data_nasc
    
    # @data_nasc.setter
    # def data_nasc(self, data_nasc):
    #     self.__data_nasc = data_nasc