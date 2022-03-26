# /**
#  * Função para avançar ou recuar, passando a potência e o sentido do motor.
#  * Analizar como vai funcionar a ponte H para determinar como fazer pra ele recuar se for preciso.
#  */
import config
from ESP import *


def andar(pot: int, frente: bool):
    if not frente:
        pot *= -1

    digitalWrite(config.PORTAMOTOR1, pot)
    digitalWrite(config.PORTAMOTOR2, pot)


#  * Funçao para girar, passando as potências para o motor.

def girar(pot1: int, pot2: int):

    digitalWrite(config.PORTAMOTOR1, pot1)
    digitalWrite(config.PORTAMOTOR2, pot2)


# * Funcao para girar pra direita.


def girarPraDireita(pot: int):
    girar(10, pot)


#  * Funcao para girar pra esquerda.


def girarPraEsquerda(pot: int):
    girar(pot, 10)


#  * Função para avançar, passando apenas a potÊncia do motor.


def avancar(pot: int):
    andar(pot, True)


#  * Função para recuar, passando apenas a potência do motor.


def recuar(pot: int):
    andar(pot, False)


#  * Função para parar.


def parar():
    avancar(0)
