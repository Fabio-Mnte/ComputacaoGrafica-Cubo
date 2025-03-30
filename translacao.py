
def getDirection_translacao(position, direction):
    # Verifica colisões com os limites da tela
    if position[0] >= 2 or position[0] <= -2:
        direction[0] *= -1  # Inverte a direção X

    if position[1] >= 2 or position[1] <= -2:
        direction[1] *= -1  # Inverte a direção Y

    position[0] += direction[0]
    position[1] += direction[1]

    return direction



