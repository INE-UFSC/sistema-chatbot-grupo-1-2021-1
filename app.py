#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Me")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
