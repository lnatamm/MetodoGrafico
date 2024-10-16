INF = 100000
class MetodoGrafico:
    def __init__(self, c1, c2, min):
        self.c = [c1, c2]
        self.min = min
        self.Ab = [
            [-1, 0, 0],
            [1, 0, INF],
            [0, -1, 0],
            [0, 1, INF]
        ]

    # Retorna os elementos de uma matriz A 2x2
    def GetElements(A):
        return A[0][0], A[0][1], A[1][0], A[1][1]

    # Retorna o determinante de uma matriz A 2x2
    def GetDeterminant(A):
        a, b, c, d = GetElements(A)
        return (a*d) - (b*c)

    # Retorna o inverso da matriz A
    def InvertMatrix(A):
        a, b, c, d = GetElements(A)
        determinant = GetDeterminant(A)
        if(determinant == 0):
            print("Matriz não possui inversa, portando o sistema é impossível ou indeterminado")
            return None
        invertedMatrix = [
            [d/determinant, -b/determinant],
            [-c/determinant, a/determinant]
        ]
        return invertedMatrix

    #Multiplica a matriz A 2x2 pela matriz coluna b
    def MultiplyMatrix(A, b):
        result = [(A[0][0] * b[0]) + (A[0][1] * b[1]), (A[1][0] * b[0]) + (A[1][1] * b[1])]
        return result

    #Retorna a solução do sistema de equação formado pelas condições c1 e c2
    def GetSolution(c1, c2):
        A = [
            [c1[0], c1[1]],
            [c2[0], c2[1]]
        ]
        b = [c1[2], c2[2]]
        invertedA = InvertMatrix(A)
        solution = MultiplyMatrix(invertedA, b)
        return solution


    # Adiciona a inequação 𝑎1𝑥 + 𝑎2𝑦 <= 𝑏 à matriz 𝐴𝑏
    def AddEq(self, a1, b1, b):
        self.Ab.append([a1, b1, b])

    # Lista as inequações, numeradas de 0 a 𝑛 − 1
    def ListEq(self):
        n = len(self.Ab)
        for i in range(n):
            eq = self.Ab[i]
            print(f"Equação {i}: {eq[0]}*x {eq[1]}*y <= {eq[2]}")
    # Remove a 𝑘-ésima inequação da matriz 𝐴𝑏. Não é possível remover as inequações 0, 1, 2 e 3, dadas pela inicialização
    def RemoveEq(self, k): 
        if(k <= 3 and k >= 0):
            return
        self.Ab.pop(k)
        
    # Testa se o ponto (𝑥0, 𝑦0) satisfaz todas as condições do problema
    def CheckPoint(self, x0, y0): 
        n = len(self.Ab)
        for i in range(n):
            eq = self.Ab[i]
            if(((eq[0] * x0) + (eq[1] * y0)) > eq[2]):
                return False
        return True
    # Retorna uma solução ótima do problema. Caso a solução tenha alguma de suas coordenadas valendo 𝐼𝑁𝐹, retorna a string "Função Ilimitada".
    def GetSolution(self): 
        pass