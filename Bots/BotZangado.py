from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = { "1": "Boas vindas", "2": "Xingamento", "3": "Motivos de por que estou zangado" }
        super().__init__(self.__nome, self.__comandos)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def executa_comando(self, cmd):
        comandos = { "1": self.boas_vindas, "2": self.xingamento, "3": self.motivos }
        print(comandos[cmd]())

    def apresentacao(self):
        return f'Meu nome é {self.__nome}. Nossa como não queria estar aqui. Você me irrita.'

    def boas_vindas(self):
        return f'---> {self.__nome} diz: Boas vindas é o caramba, só quero sair.'

    def despedida(self):
        return f'---> {self.__nome} diz: Finalmente, espero não te ver novamente.'
    
    def xingamento(self):
        return f'---> {self.__nome} diz: Seu bobo.'
    
    def motivos(self):
        return f'---> {self.__nome} diz: Meus motivos? ... Pra começo de conversa, por que eu te falaria?!'