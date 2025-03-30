import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import wireCube
from escala import getDirection_escala
from translacao import getDirection_translacao

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)


screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

# Posição e velocidade do cubo
position = [0, 0]
direction = [1,1]
aspect_ratio = screen_width / screen_height
fov = 60

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -5)
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


def display_escala(): #Display 1 -> Demonstração de escalas
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    z = getDirection_escala(position, direction)  # Define a taxa de alteração de escala do cubo
    glTranslate(0, 0, z)
    glPushMatrix()
    wireCube()
    glPopMatrix()

def display_translacao(): #Display 2 -> Demonstração da Translação

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    x, y = getDirection_translacao(position, direction) #Define a direção de translação do cubo
    glTranslate(x, y, 0)
    glPushMatrix()
    wireCube()
    glPopMatrix()

done = False
tipo = 0 #Verificador para garantir que todas as cenas foram mostradas
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tipo += 1 #Altera de uma cena para outra
            position = [0, 0] #Reseta a variável das posições
            direction = [1, 1] #Reseta a variável das direções
            initialise() #Reseta a configuração do cubo
            if tipo == 2: #Verifica se todas as cenas já foram vistas (tipo 0 = escala, tipo 1 = translação, tipo 2 = espelhamento)
                done = True
    if tipo == 0:
        display_escala() #Define a configuração atual como a de escala
    elif tipo == 1:
        display_translacao() #Define a configuração atual como a de translação
    #else:
        #display_espelhamento()
    pygame.display.flip()
    pygame.time.wait(250); #Define o tempo de atualização dos displays
pygame.quit()
