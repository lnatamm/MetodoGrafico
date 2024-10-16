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
        if(self.min):
            self.intercessions = [
                [0, 0]
            ]
        else:
            self.intercessions = [
                [INF, INF]
            ]

    # Retorna os elementos de uma matriz A 2x2
    def GetElements(self, A):
        return A[0][0], A[0][1], A[1][0], A[1][1]

    # Retorna o determinante de uma matriz A 2x2
    def GetDeterminant(self, A):
        a, b, c, d = self.GetElements(A)
        return (a*d) - (b*c)

    # Retorna o inverso da matriz A
    def InvertMatrix(self, A):
        a, b, c, d = self.GetElements(A)
        determinant = self.GetDeterminant(A)
        if(determinant == 0):
            print("Matriz não possui inversa, portando o sistema é impossível ou indeterminado")
            return None
        invertedMatrix = [
            [d/determinant, -b/determinant],
            [-c/determinant, a/determinant]
        ]
        return invertedMatrix

    #Multiplica a matriz A 2x2 pela matriz coluna b
    def MultiplyMatrix(self, A, b):
        result = [(A[0][0] * b[0]) + (A[0][1] * b[1]), (A[1][0] * b[0]) + (A[1][1] * b[1])]
        return result

    #Conserta o "-0.0" que pode ocorrer em algumas multiplicações
    def FormatValue(self, value):
        if(abs(value) < 1e-10):
            return 0.0
        return value

    #Retorna a solução do sistema de equação formado pela multiplicação da matriz A 2x2 pela matriz coluna b
    def GetSolutionAb(self, A, b):
        invertedA = self.InvertMatrix(A)
        solution = self.MultiplyMatrix(invertedA, b)
        solution = [self.FormatValue(value) for value in solution]
        return solution

    # Adiciona a inequação 𝑎1𝑥 + 𝑎2𝑦 <= 𝑏 à matriz 𝐴𝑏
    def AddEq(self, a1, b1, b):
        self.Ab.append([a1, b1, b])
        for i in range(len(self.Ab)):
            A = [
                [a1, b1],
                [self.Ab[i][0], self.Ab[i][1]]
            ]
            bValues = [b, self.Ab[i][2]]
            if(self.GetDeterminant(A) != 0):
                solution = self.GetSolutionAb(A, bValues)
                if(self.CheckPoint(solution[0], solution[1]) and solution not in self.intercessions):
                    self.intercessions.append(solution)


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

    # Retorna a intercessão que resulta no menor valor da função objetivo
    def GetMin(self):
        n = len(self.intercessions)
        minValue = INF
        solution = [None, None]
        for i in range(n):
            point = self.intercessions[i]
            if(self.CheckPoint(point[0], point[1])):
                result = (point[0] * self.c[0]) + (point[1] * self.c[1])
                if(result < minValue):
                    minValue = result
                    solution = point
        return solution

    # Retorna a intercessão que resulta no maior valor da função objetivo
    def GetMax(self):
        n = len(self.intercessions)
        maxValue = -INF
        solution = [None, None]
        for i in range(n):
            point = self.intercessions[i]
            if(self.CheckPoint(point[0], point[1])):
                result = (point[0] * self.c[0]) + (point[1] * self.c[1])
                if(result > maxValue):
                    maxValue = result
                    solution = point
        return solution

    # Retorna uma solução ótima do problema. Caso a solução tenha alguma de suas coordenadas valendo 𝐼𝑁𝐹, retorna a string "Função Ilimitada".
    def GetSolution(self): 
        if(self.min):
            return self.GetMin()
        return self.GetMax()