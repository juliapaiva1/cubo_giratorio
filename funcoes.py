import numpy as np

#cria uma matriz possibilitando rotação no eixo x
def matriz_rotacao_x(angulo):
    radianos = np.radians(angulo)
    matriz = np.array([[1, 0, 0, 0],
        [0, np.cos(radianos), -np.sin(radianos), 0],
        [0, np.sin(radianos), np.cos(radianos), 0], 
        [0, 0, 0, 1]])

    return matriz

#cria uma matriz possibilitando rotação no eixo y
def matriz_rotacao_y(angulo):
    radianos = np.radians(angulo)
    matriz = np.array([[np.cos(radianos), 0, np.sin(radianos), 0],
        [0, 1, 0, 0],
        [-np.sin(radianos), 0, np.cos(radianos), 0], 
        [0, 0, 0, 1]])
    
    return matriz

#cria uma matriz possibilitando rotação no eixo z
def matriz_rotacao_z(angulo):
    radianos = np.radians(angulo)
    matriz =  np.array([[np.cos(radianos), -np.sin(radianos), 0, 0],
        [np.sin(radianos), np.cos(radianos), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    
    return matriz

#cria uma matriz de translação através dos valores fornecidos de x, y, e z
def matriz_translacao(x, y, z):

    matriz = np.array([[1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]])

    return matriz


#devolve os vértices projetados em um plano, aplicando uma matriz de transformação através da distância fornecida
def projecao(pontos, d):
    matriz_transformacao = np.array([[0, 0, 0, -d],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1/d, 0]])
    
    pontos_transformados = matriz_transformacao @ pontos
    escalar = pontos_transformados[3, :]
    pontos_projetados = np.stack((pontos_transformados[1, :] / escalar, pontos_transformados[2, :] / escalar, pontos[2, :]), axis=1)

    return pontos_projetados
