# APS 4: Cubo giratório
# Aluna: Júlia Ferreira de Paiva

1. Como instalar e rodar o programa:

Tenha instalado em sua máquina um editor de código, como por exemplo, Visual Studio Code. Na página do projeto no Github, clique em "Code" e baixe como zip. Extraia em uma pasta e abra essa pasta no editor de código. Instale os pacotes necessários 
com o comando "pip install -r requirements.txt", pelo terminal. Depois que a instalação tiver sido bem-sucedida, entre no arquivo "main.py" e execute-o.

2. Modelo matemático:

Fazer com que um cubo possa girar em várias direções digitalmente envolve uma análise sobre a projeção de pontos. Podemos ter uma noção melhor de como a projeção funciona através do modelo de câmera pinhole, que usamos como base aqui. Utilizando elementos desse modelo, podemos chegar à uma matriz que será chamada "matriz de transformação", que apontará para onde os pontos estão sendo projetados.

![alt-text](https://github.com/juliapaiva1/cubo_giratorio/blob/main/pinhole_diagrama.png)

Podemos pensar em começar encontrando equações para determinar os valores de Xp e Yp, mantendo o eixo Z estático por enquanto. Como é perceptível na imagem, temos dois triângulos sendo formados, então podemos utilizar semelhança de triângulos. Pela maneira como os triângulos estão dispostos, podemos estabelecer uma relação pela tangente:

$$
Tan (\theta) = \frac{x0}{y0} = \frac{xp}{yp}
$$

E, para encontrar a equação correspondente à Xp, podemos isolá-lo:

$$
Xp = \frac{x0*yp}{y0}
$$

O ideal é que encontremos um número real, que multiplicado por X0, resulte em Xp. Podemos chamar esse número real de Wp, e representá-lo com a seguinte equação:

$$
X0 = Xp * Wp
$$

Para encontrar a equação referente à Wp, podemos aproveitar essa equação anterior, apenas isolando o Wp, e tomando yp como -d (pois Yp pode ser interpretado como a distância entre o eixo x e o anteparo):

$$
Wp = \frac{y0}{yp} = \frac{y0}{-d}
$$

Podemos representar em matriz, então, como:

$$
\begin{bmatrix}
 1 & 0 & 0 \\
 0 & 0 & -d \\
 0 & -1/d & 0
\end{bmatrix}
$$

Agora fazemos o mesmo processo, mas ao invés de usarmos os pares (X0, Y0) e (Xp, Yp), usamos (Z0, Y0) e (Zp, Yp). A seguir, os passos seguem a mesma lógica dos anteriores:

$$
Y0 = \frac{yp*z0}{zp}
$$

Y0 = Yp * Wp

$$
Wp = \frac{Z0}{Zp} 
$$

E obtemos a seguinte representação:

$$
\begin{bmatrix}
 1 & 0 & 0 \\
 0 & 0 & -d \\
 0 & -1/d & 0
\end{bmatrix}
$$

Combinando as duas matrizes, chegamos à nossa matriz de transformação:

$$
\begin{bmatrix}
 1 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 \\
 0 & 0 & 0 & -d\\
 0 & 0 & -1/d & 0\\
\end{bmatrix}
$$

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
1 & 1 & -1 \\
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



3. Gif do programa funcionando:

![alt-text](https://github.com/juliapaiva1/cubo_giratorio/blob/main/gif_cubo.gif)
