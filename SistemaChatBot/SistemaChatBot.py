from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        self.__lista_bots=[]
        ##verificar se a lista de bots contém apenas bots
        for i in lista_bots:
            if i (isinstance(i,Bot)):
                self.__lista_bots.append(i)

        
        self.__bot = None
    
    def boas_vindas(self):
        print("Ola esse eh o sistema de ChatBots da empresa %s" % (self.__empresa))
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Os chat bots disponiveis no momento sao:")

        for i in (0,len(self.__lista_bots):
            print("%d - Bot: %s - Mensagem de apresentacao: %d" % (i, self.__lista_bots[i].nome), self.__lista_bots[i].apresentacao() )
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        a = input()
        self.__bot = self.__lista_bots[int(a)]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        b = input("Digite o comando desejado (ou -1 para sair)")
        self.__bot.executa_comando(b)
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            self.le_envia_comando() 
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
