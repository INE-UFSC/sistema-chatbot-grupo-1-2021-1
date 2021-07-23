from Bots.Bot import Bot

class BotStreamer(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = { "1": "Boas vindas", "2": "Horario live", "3": "Prime", "4": "Agradecer Sub" }
        super().__init__(self.__nome, self.__comandos)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def executa_comando(self, cmd):
        comandos = { "1": self.boas_vindas, "2": self.horario_live, "3": self.prime, "4": self.agradecimento_sub}
        print(comandos[cmd]())

    def apresentacao(self):
        return f'Salve, sou o {self.__nome}.'

    def horario_live(self):
        return f'Live amanha, hoje to cansado.'

    def prime(self):
        return f'Escorrega o prime marreco.'

    def agradecimento_sub(self):
        return f'GOD GOD, VALEU, TAMO JUNTO.'

    def boas_vindas(self):
        return f'---> {self.__nome} diz: Opaaa, fala delee.'

    def despedida(self):
        return f'---> {self.__nome} diz: Falou, vai ter live amanha em.'