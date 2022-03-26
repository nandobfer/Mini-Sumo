# /**
# * Retorna o valor correspondente ao sensor, caso o sensor detecte algo.
# */
import config
from NANO import *

# armazena direção em que o inimigo foi visto por ultimo
last_seen = ''

def verificaPresenca(sensor: int) -> int:

    if (analogRead(sensor) < 10):

        result = False

    return result

# Recebe um valor numérico e retorna a chave do dicionário equivalente a posição do número

def getKey(n, dict):
    for i, key in enumerate(dict.keys()):
                if i == n-1:
                    return key
    return None


# /**
# * Verifica os sensores de presença(inimigo).
# * Possíveis valores de retorno:
#     * = 100: Inimigo à frente.
#     * > 100: Inimigo à direita.
#     * < 100: Inimigo à esquerda.
#     * = 0: Inimigo não encontrado.
#     */


def verificaPresencas() -> int:
    global last_seen
    result = 0
    for i in range(0, len(config.sensoresPresensa)):
        key = getKey(i, config.sensoresPresenca)
        result += verificaPresenca(config.sensoresPresenca[key])
        if result > 0 and result < 100:
            last_seen = 'right'
        elif result < 0:
            last_seen = 'left'
        else:
            last_seen = 'front'

    return result


# / **
# * Retorna o valor correspondente ao sensor de borda, caso o sensor detecte algo.
# * /
def verificaBorda(sensor: int) -> int:
    result = 0
    if digitalRead(sensor):
        result = config.sensoresBorda[sensor]

    return result


# / **
# * Verifica os sensores de borda(segurança).
# * Possíveis valores de retorno:
#     * > 0: Borda da frente detectada.
#     * < 0: Borda de trás detectada.
#     * = 0: Nenhuma borda detectada.
#     * /


def verificaBordas() -> int:
    result = 0
    for i in range(0, len(config.sensoreBorda)):
        key = getKey(i, config.sensoresBorda)
        result += verificaBorda(config.sensoresBorda[key])

    return result

# Verifica se o inimigo está para a direita
# Retorna True se for sim, False caso contrário
def inimigoPraDireita():
    valorPresenca = verificaPresencas()

    if valorPresenca > 0 and valorPresenca < 100:
        return True
    else:
        return False

# Verifica se o inimigo está para a esquerda
# Retorna True se for sim, False caso contrário
def inimigoPraEsquerda():
    valorPresenca = verificaPresencas()

    if valorPresenca < 0:
        return True
    else:
        return False
