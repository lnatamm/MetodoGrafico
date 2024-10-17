# Resumo
Esse repositório consiste na implementação do Método Gráfico, utilizado na resolução de problemas de programação linear

# Método Gráfico

Na resolução de problemas de otimização com 2 variáveis, é muito    comum o uso do chamado Método Gráfico.

## Definição do problema
>
>### [ Variáveis ]
>𝑥, 𝑦 ∈ ℝ+
>
>### [ Função Objetivo ]
>𝑓(𝑥, 𝑦) = 𝑐1𝑥 + 𝑐2𝑦 (min/max)
>
>### [ Condições ]
>𝑎11𝑥 + 𝑎12𝑦 ≤ 𝑏1\
>𝑎21𝑥 + 𝑎22𝑦 ≤ 𝑏2\
>⋮\
>𝑎𝑛1𝑥 + 𝑎𝑛2𝑦 ≤ 𝑏𝑛
>
>As condições podem ser reescritas pela equação 𝐴𝑥 ≤ 𝑏. Estas definem uma região 𝑅 no plano cartesiano
>convexa e limitada por retas, chamada uma Região Poligonal ou Região Factível, a menos que 𝑅 = ∅
>
>

## Teorema
Se um problema de otimização linear 𝑃 tem soluções ótimas, então alguma destas ocorre em um vértice
da região poligonal.

## Implementação
### [main.py](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py)
>### Classe [MetodoGrafico](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L2):
>### Variáveis:
>c = [c1, c2].\
\
>min: booleano que define a função como de minimização ou maximização.\
\
>𝐴𝑏: uma matriz de três colunas onde as duas primeiras apresentam os coeficientes da matriz 𝐴 e a terceira
>armazena a matriz coluna 𝑏.
>### Métodos:
>### Métodos do Método Gráfico
>### [Construtor(𝑐1, 𝑐2, 𝑚𝑖𝑛)](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L5):
>Armazena a função objetivo com os valores 𝑐1
>e 𝑐2
>, bem como indica com um booleano
>se a função requer uma minimização ou maximização. Esta função inicializa 𝐴𝑏 como:\
>𝐴𝑏 =
>
>| | | |
>|---|---|---|
>| -1 | 0 | 0 |
>| 1 | 0 | 𝐼𝑁𝐹|
>| 0 | -1 | 0 |
>| 0 | 1 | 𝐼𝑁𝐹 |
>
>OBS: 𝐼𝑁𝐹 = 100000
>
>Isso indica que 0 <= x, y <= 𝐼𝑁𝐹.
>
>### [AddEq(𝑎1, 𝑎2, 𝑏)](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L68): 
>Adiciona a equação 𝑎1𝑥 + 𝑎2
>𝑦 <= 𝑏 à matriz 𝐴𝑏.
>
>### [ListEq()](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L93): 
>Lista as equações, numeradas de 0 a 𝑛 − 1.
>
>### [RemoveEq(𝑘)](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L101): 
>remove a 𝑘-ésima equação da matriz 𝐴𝑏. Não é permitido remover as equações 0, 1, 2 e 3,
>dadas pela inicialização.
>
>### [GetMin()](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L121)
>Retorna a intercessão que resulta no menor valor da função objetivo e o seu resultado
>### [GetMax()](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L146)
>Retorna a intercessão que resulta no maior valor da função objetivo e o seu resultado
>### [CheckPoint(𝑥0, 𝑦0)](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L109): 
>Verifica se o ponto (𝑥0, 𝑦0) satisfaz todas as condições do problema.
>
>### [GetSolution()](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L171): 
>Retorna uma solução ótima do problema. Caso a solução tenha alguma de suas coordenadas valendo
>𝐼𝑁𝐹, retorna a string "Função Ilimitada".
>
>### Métodos de solução de sistemas
>
>### [GetElements(A):](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L27)
>Retorna os elementos a, b, c, d de uma matriz A 2x2
>| | |
>|---|---|
>| a | b |
>| c | d |
>### [GetDeterminant(A):](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L31)
>Retorna o determinante da matriz A 2x2
>### [InvertMatrix(A):](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L36)
>Retorna o inverso da matriz A 2x2
>### [MultiplyMatrix(A, b):](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L49)
>Multiplica a matriz A 2x2 pela matriz coluna b
>### [FormatValue(value):](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L54)
>Conserta o "-0.0" que pode ocorrer em algumas multiplicações
>### [GetSolutionAb(A, b):](https://github.com/lnatamm/MetodoGrafico/blob/main/main.py#L60)
>Retorna a solução do sistema de equação formado pela multiplicação da matriz A 2x2 pela matriz coluna b