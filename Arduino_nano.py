from funcSensor import *
import funcSensor
from funMotor import *
# /**
#   Função para verificar se os sensores acharam borda.
# */


def achouBorda():
    #   Inicializa variável de retorno.
    result = True
#   Obtém a leitura dos sensores.
    valorBorda = verificaBorda()
#   Se o sensor de trás foi acionado.
    if valorBorda == -11:
     # Anda pra frente
        avancar(255)
     # Se o sensor da frente foi acionado.
    elif valorBorda == 11:
     # Anda pra trás.
        recuar(255)
    elif valorBorda == 1:
        girarPraEsquerda(255)
    elif valorBorda == -1:
        girarPraDireita(255)

#   Caso nenhum dos sensores tenha sido acionado.
    else:
     # Atualiza variável de retorno.
        result = False

    return result


#
# Função para verificar se os sensores de inmigo detectou algo.
#
def achouInimigo():
    valorPresenca = verificaPresencas()

    result = True

    if valorPresenca == 0:
        result = False

    return result


# /**
# * Funcao para rodar todo o funcionamento do sistema.
# */
def Main():

    if not achouBorda():

        if achouInimigo():

            if inimigoPraDireita:

                girarPraDireita(150)

            elif inimigoPraEsquerda:

                girarPraEsquerda(150)

            else: # se o inimigo não tiver pra nenhum lado
                avancar(255) # ir pra frente empurrar ele
        else: # se não tiver encontrado inimigo, procurar

            if funcSensor.last_seen == 'right': #se tiver visto o inimigo pela ultima vez na direita
                girarPraDireita(150)

            elif funcSensor.last_seen == 'left': #se tiver visto o inimigo pela ultima vez na esquerda
                girarPraEsquerda(150)

while(True):
    Main()
