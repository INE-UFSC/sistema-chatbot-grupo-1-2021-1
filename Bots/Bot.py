##implemente as seguintes classes

from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self, nome, comandos = {}):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def mostra_comandos(self):
        for k,v in self.__comandos.items():
            print(k,":",v)

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass