from Bots.Bot import Bot

class BotOtaku(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = { "1": "Apresentação", "2": "Boas vindas", "3": "Despedida", "4": "Recomendações" }
        super().__init__(self.__nome, self.__comandos)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def executa_comando(self, cmd):
        comandos = { "1": self.apresentacao, "2": self.boas_vindas, "3": self.despedida, "4": self.recomendacoes }
        print(comandos[cmd]())

    def apresentacao(self):
        return f'Meu nome é {self.__nome}. Não fala mal dos meus animes!'

    def boas_vindas(self):
        return f'---> {self.__nome} diz: Só vou aceitar boas vindas se você gosta de algum anime.'
    
    def recomendacoes(self):
        return f'---> {self.__nome} diz: Recomendo School Days, Death Note, Demon Slayer e Attack on Titan.'

    def despedida(self):
        return f'---> {self.__nome} diz: Vai lá assistir animes.'