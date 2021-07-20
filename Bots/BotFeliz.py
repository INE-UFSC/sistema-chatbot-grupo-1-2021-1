from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = { "1": "Apresentação", "2": "Boas vindas", "3": "Despedida" }
        super.__init__(self.__nome, self.__comandos)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
 
    def mostra_comandos(self):
      super().mostra_comandos()
    
    def executa_comando(self, cmd):
        comandos = { "1": self.boas_vindas(), "2": self.apresentacao(), "3": self.despedida() }
        comandos[cmd]

    def apresentacao(self):
        return f'{self.__nome} diz: Meu nome é {self.__nome}. Nossa como estou feliz.'

    def boas_vindas(self):
        return f'{self.__nome} diz: Boas vindas querido amigo.'

    def despedida(self):
        return f'{self.__nome} diz: Espero te ver novamente.'