from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        self.__lista_bots=[]
        for i in lista_bots:
            if i (isinstance(i,Bot)):
                self.__lista_bots.append(i)

        
        self.__bot = None
    
    def boas_vindas(self):
        print("Ola esse eh o sistema de ChatBots da empresa %s" % (self.__empresa))


    def mostra_menu(self):
        print("Os chat bots disponiveis no momento sao:")

        for i in (0,len(self.__lista_bots)):
            print("%d - Bot: %s - Mensagem de apresentacao: %d" % (i, self.__lista_bots[i].nome), self.__lista_bots[i].apresentacao())

    
    def escolhe_bot(self):
        a = input("Digite o numero do chat bot desejado")
        self.__bot = self.__lista_bots[int(a)]
 

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()


    def le_envia_comando(self):
        b = input("Digite o comando desejado (ou -1 para sair)")
        if b == "-1":
            return False
        self.__bot.executa_comando(b)
        return


    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            retorno = self.le_envia_comando()
            if retorno == False:
                break
 
