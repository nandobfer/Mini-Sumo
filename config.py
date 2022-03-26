# Arquivo para configuração das portas, variáveis auxiliares e globais.

PORTAMOTOR1 = 1  # //ESQUERDA
PORTAMOTOR2 = 2  # //DIREITA
PORTASENSORPRESENCA1 = 3  # //Sensor de presenca mais a esquerda.
PORTASENSORPRESENCA2 = 4  # //Sensor de presenca entre a esquerda e o meio.
PORTASENSORPRESENCA3 = 5  # /Sensor de prenca central.
PORTASENSORPRESENCA4 = 6  # //Sensor de presenca entre o direito e o meio.
PORTASENSORPRESENCA5 = 7  # //Sensor de presenca mais a direita,
PORTASENSORBORDAFRENTEDIREITA = 8  # //Sensor de borda da frente.
PORTASENSORBORDATRASDIREITA = 9  # //Sensor de borda de trás
PORTASENSORBORDAFRENTEESQUERDA = 10  # //Sensor de borda da frente.
PORTASENSORBORDATRASESQUERDA = 11  # //Sensor de borda de trás

sensoresPresensa = {
    PORTASENSORPRESENCA1: -1,
    PORTASENSORPRESENCA2: -10,
    PORTASENSORPRESENCA3: 100,
    PORTASENSORPRESENCA4: 10,
    PORTASENSORPRESENCA5: 1
}

# Alterei os sensores de borda pra acompanhar o projeto eletrônico
sensoresBorda = {
    PORTASENSORBORDAFRENTEDIREITA: 1,
    PORTASENSORBORDAFRENTEESQUERDA: 10,
    PORTASENSORBORDATRASDIREITA: -10,
    PORTASENSORBORDATRASESQUERDA: -1
}
