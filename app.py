#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotStreamer import BotStreamer
from Bots.BotOtaku import BotOtaku

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Patati"), BotStreamer("Redy"), BotOtaku("Sasuke XD")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
