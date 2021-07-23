from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = { "1": "Boas vindas", "2": "Mensagem motivacional", "3": "Coisas que me deixam feliz" }
        super().__init__(self.__nome, self.__comandos)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def executa_comando(self, cmd):
        comandos = { "1": self.boas_vindas, "2": self.mensagem_motivacional, "3": self.felicidades }
        print(comandos[cmd]())
    
    def mensagem_motivacional(self):
        return f'---> {self.__nome} diz: Acredite, você pode tudo. Eu acredito em você'
    
    def felicidades(self):
        return f'---> {self.__nome} diz: Coisas que me deixam feliz: Falar com você, comer melância.'

    def apresentacao(self):
        return f'Meu nome é {self.__nome}. Nossa como estou feliz.'

    def boas_vindas(self):
        return f'---> {self.__nome} diz: Boas vindas querido amigo. Estou muito feliz que você está aqui.'

    def despedida(self):
        return f'---> {self.__nome} diz: Espero te ver novamente.'