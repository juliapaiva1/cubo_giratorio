# APS 4: Cubo giratório
# Aluna: Júlia Ferreira de Paiva

1. Como instalar e rodar o programa:

Tenha instalado em sua máquina um editor de código, como por exemplo, Visual Studio Code. Na página do projeto no Github, clique em "Code" e baixe como zip. Extraia em uma pasta e abra essa pasta no editor de código. Instale os pacotes necessários 
com o comando "pip install -r requirements.txt", pelo terminal. Depois que a instalação tiver sido bem-sucedida, entre no arquivo "main.py" e execute-o.

2. Modelo matemático:

(descrição matemática do modelo que você implementou, incluindo quais transformações foram aplicadas e como as matrizes de transformação funcionam)

Para que o cubo gire perfeitamente e permaneça no centro da tela, são incorporadas quatro matrizes diferentes na matriz do cubo: rotação (nos eixos x, y e z) e translação. As matrizes de rotação utilizadas são as seguintes:

$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

E a de translação:

$$
T = \begin{bmatrix}
1 & 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

E elas são aplicadas através de uma multiplicação matricial na matriz que representa as coordenadas dos vértices:

$$
V = \begin{bmatrix}
-1 & -1 & -1 \\
-1 & -1 & 1 \\
-1 & 1 & -1 \\
-1 & 1 & 1 \\
1 & -1 & -1 \\
1 & -1 & 1 \\
1 & 1 & -1 & z \\
1 & 1 & 1 
\end{bmatrix}
$$

Com essa multiplicação feita, obtemos uma matriz de vértices rotacionados, e podemos finalmente aplicar a matriz de transformação, obtida antes:

$$
V = \begin{bmatrix}
0 & 0 & 0 & -d \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & -1/d & 0 
\end{bmatrix}
$$

Com isso, obtemos uma matriz que representa os pontos projetados, e podemos utilizar seus pontos para criar as arestas, como apontado no código.

organizacao: 

1 - explicar o modelo matematico em si (a explicacao da lousa)
2 - relacionar com o codigo
3 - explicar como foram feitas as transformacoes de matrizes

3. Gif do programa funcionando:

![alt-text](https://github.com/juliapaiva1/cubo_giratorio/blob/main/gif_cubo.gif)
