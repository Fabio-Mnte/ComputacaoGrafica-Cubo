def getDirection_escala(position, direction):
    # Verifica o tamanho maximo e minimo do cubo
    if position[0] >= 3 or position[0] <= -3:
        direction[0] *= -1  # Inverte a taxa de crescimento

    position[0] += direction[0]

    return direction[0]



