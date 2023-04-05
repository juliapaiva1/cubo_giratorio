import pygame
import numpy as np
from funcoes import *

#define altura e largura da tela, distância focal e tamanho do cubo
LARGURA, ALTURA = 800, 600
d = 250
tamanho_cubo = 50

#define as coordenadas dos vertices e aplica tamanho do cubo
vertices = np.array([[-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1]])
vertices = vertices.T * tamanho_cubo
vertices = np.vstack((vertices, np.ones((1, vertices.shape[1]))))

#define os indices dos vertices
indice_vertices = np.array([[0, 1],
    [0, 2],
    [0, 4],
    [1, 3],
    [1, 5],
    [2, 3],
    [2, 6],
    [3, 7],
    [4, 5],
    [4, 6],
    [5, 7],
    [6, 7]])

#inicializa o pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cubo Girando")
clock = pygame.time.Clock()
running = True
COR_FUNDO = (0, 0, 0)
COR_BLOCO = (255, 255, 0)

#cria ângulos e direções iniciais do cubo
angulo_rotacao = 180
direcao_cubo = np.array([1, 0, 1])

#loop para receber e tratar eventos
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #incrementa ângulo de rotação e "limpa" a tela para evitar interferências no cubo
    angulo_rotacao += 1
    tela.fill(COR_FUNDO)

    #aplica as matrizes de rotação, translação e projeção para projetar os pontos
    vertices_rotacionados = matriz_translacao(direcao_cubo[0], direcao_cubo[1], direcao_cubo[2] + 200) @ matriz_rotacao_x(angulo_rotacao) @ matriz_rotacao_y(angulo_rotacao) @ matriz_rotacao_z(angulo_rotacao) @ vertices
    pontos_projetados = projecao(vertices_rotacionados, d)

    #constrói as arestas do cubo através da projeção dos pontos
    for vertice in indice_vertices :
        ponto_inicial = (pontos_projetados[vertice[0]][0] + (LARGURA/2), pontos_projetados[vertice[0]][1] + ALTURA/2)
        ponto_final = (pontos_projetados[vertice[1]][0] + (LARGURA/2), pontos_projetados[vertice[1]][1] + ALTURA/2)
        pygame.draw.line(tela, COR_BLOCO, ponto_inicial, ponto_final, 4)

    #atualiza o display do programa      
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
