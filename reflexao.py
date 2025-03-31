import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
from Cube import wireCube
# Configuração dos vértices do cubo
vertices = [(0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, -0.5, -0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (0.5, 0.5, 0.5),
            (0.5, -0.5, 0.5)]

triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
             13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]

def wireCube_colorido():
    for t in range(len(triangles) - 3):
        glBegin(GL_LINES)
        if t == 0 or t == 1 or t == 2:
            glColor3f(1, 0, 0)  # Vermelho para o primeiro triângulo
        elif t== 6 or t == 7 or t == 8:
            glColor3f(0, 0, 1)  # azul para o primeiro triângulo
        elif t == 12 or t == 13 or t == 14:
            glColor3f(0, 1, 0)  # azul para o primeiro triângulo
        else:
            glColor3f(1, 1, 1)  # Branco para os outros
        glVertex3fv(vertices[triangles[t]])
        glVertex3fv(vertices[triangles[t + 1]])
        glVertex3fv(vertices[triangles[t + 2]])
        glEnd()
        t += 3
