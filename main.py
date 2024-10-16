INF = 100000
class MetodoGrafico:

    # Método Construtor da classe
    def __init__(self, c1, c2, min):
        self.c = [c1, c2]
        self.min = min
        #Essa inicialização diz que 0 <= x, y <= 𝐼𝑁𝐹
        self.Ab = [
            [-1, 0, 0],
            [1, 0, INF],
            [0, -1, 0],
            [0, 1, INF]
        ]
        #Caso a função seja de minimização, o primeiro ponto é (0, 0), já que x, y >= 0
        if(self.min):
            self.intercessions = [
                [0, 0]
            ]
        #Caso a função seja de maximização, o primeiro ponto é (𝐼𝑁𝐹, 𝐼𝑁𝐹), já que a única restrição é x, y <= 𝐼𝑁𝐹
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

    # Multiplica a matriz A 2x2 pela matriz coluna b
    def MultiplyMatrix(self, A, b):
        result = [(A[0][0] * b[0]) + (A[0][1] * b[1]), (A[1][0] * b[0]) + (A[1][1] * b[1])]
        return result

    # Conserta o "-0.0" que pode ocorrer em algumas multiplicações
    def FormatValue(self, value):
        if(abs(value) < 1e-10):
            return 0.0
        return value

    # Retorna a solução do sistema de equação formado pela multiplicação da matriz A 2x2 pela matriz coluna b
    def GetSolutionAb(self, A, b):
        invertedA = self.InvertMatrix(A)
        #A solução de um sistema de equação de 2° grau é encontrada ao multiplicar o inverso da matriz A pela matriz coluna b
        solution = self.MultiplyMatrix(invertedA, b)
        solution = [self.FormatValue(value) for value in solution]
        return solution

    # Adiciona a inequação 𝑎1𝑥 + 𝑎2𝑦 <= 𝑏 à matriz 𝐴𝑏
    def AddEq(self, a1, b1, b):
        #Adicionamos a inequação à matriz Ab
        self.Ab.append([a1, b1, b])
        #Iteramos por cada inequação da matriz Ab
        for i in range(len(self.Ab)):
            #Separamos a matriz Ab em A e b
            A = [
                #A inequação que acabamos de adicionar
                [a1, b1],
                #A inequação atual do loop
                [self.Ab[i][0], self.Ab[i][1]]
            ]
            #O valor associado da inequação adicionada e da inequação atual
            bValues = [b, self.Ab[i][2]]
            #Caso o sistema Ab possua solução única, existe uma intercessão entre a inequação adicionada e a inequação atual
            if(self.GetDeterminant(A) != 0):
                #A solução do sistema é a intercessão
                solution = self.GetSolutionAb(A, bValues)
                #Se a intercessão satisfaz todas as inequações de Ab
                if(self.CheckPoint(solution[0], solution[1]) and solution not in self.intercessions):
                    #Adicionamos essa intercessão
                    self.intercessions.append(solution)


    # Lista as inequações, numeradas de 0 a 𝑛 − 1
    def ListEq(self):
        n = len(self.Ab)
        #Loop para cada inequação de Ab
        for i in range(n):
            ineq = self.Ab[i]
            print(f"Equação {i}: {ineq[0]}*x {ineq[1]}*y <= {ineq[2]}")

    # Remove a 𝑘-ésima inequação da matriz 𝐴𝑏. Não é possível remover as inequações 0, 1, 2 e 3, dadas pela inicialização
    def RemoveEq(self, k): 
        #Se k é 0, 1, 2 ou 3 nada acontece
        if(k <= 3 and k >= 0):
            return
        #Se k é válido removemos a 𝑘-ésima inequação
        self.Ab.pop(k)
        
    # Testa se o ponto (𝑥0, 𝑦0) satisfaz todas as condições do problema
    def CheckPoint(self, x0, y0): 
        n = len(self.Ab)
        #Loop para cada inequação
        for i in range(n):
            ineq = self.Ab[i]
            #Se a inequação atual não é satisfeita pelo ponto (𝑥0, 𝑦0) retornamos False
            if(((ineq[0] * x0) + (ineq[1] * y0)) > ineq[2]):
                return False
        #Caso todas tenha sido satisfeitas retornamos True
        return True

    # Retorna a intercessão que resulta no menor valor da função objetivo e o seu resultado
    def GetMin(self):
        n = len(self.intercessions)
        #Inicializamos o menor valor como 𝐼𝑁𝐹 para que qualquer primeira intercessão seja menor
        minValue = INF
        #Caso não haja solução esse é a solução padrão
        solution = [None, None]
        #Loop para cada intercessão, esse é um algoritmo simples de retornar minimo da lista
        for i in range(n):
            #Armazenamos a coordenada da intercessão atual
            point = self.intercessions[i]
            #Caso a intercessão satisfaça todas as inequações, essa verificação é necessária pois 
            #a intercessão pode não ser mais válida
            if(self.CheckPoint(point[0], point[1])):
                #Substituímos o x e y da coordenada na função objetivo para saber o seu valor
                result = (point[0] * self.c[0]) + (point[1] * self.c[1])
                #Verificamos se esse resultado é menor que os outros
                if(result < minValue):
                    #Atualizamos o mínimo
                    minValue = result
                    #Salvamos essa possível solução
                    solution = point
        #Retornamos o melhor ponto
        return solution, minValue

    # Retorna a intercessão que resulta no maior valor da função objetivo e o seu resultado
    def GetMax(self):
        n = len(self.intercessions)
        #Inicializamos o maior valor como -𝐼𝑁𝐹 para que qualquer primeira intercessão seja maior
        maxValue = -INF
        #Caso não haja solução esse é a solução padrão
        solution = [None, None]
        #Loop para cada intercessão, esse é um algoritmo simples de retornar minimo da lista
        for i in range(n):
            #Armazenamos a coordenada da intercessão atual
            point = self.intercessions[i]
            #Caso a intercessão satisfaça todas as inequações, essa verificação é necessária pois 
            #a intercessão pode não ser mais válida
            if(self.CheckPoint(point[0], point[1])):
                #Substituímos o x e y da coordenada na função objetivo para saber o seu valor
                result = (point[0] * self.c[0]) + (point[1] * self.c[1])
                #Verificamos se esse resultado é maior que os outros
                if(result > maxValue):
                    #Atualizamos o máximo
                    maxValue = result
                    #Salvamos essa possível solução
                    solution = point
        #Retornamos o melhor ponto e o seu resultado
        return solution, maxValue

    # Retorna uma solução ótima do problema. Caso a solução tenha alguma de suas coordenadas valendo 𝐼𝑁𝐹, retorna a string "Função Ilimitada".
    def GetSolution(self): 
        #Caso o problema seja de minimização retornamos a solução mínima
        if(self.min):
            solution, minimum = self.GetMin()
            #Caso a solução tenha alguma de suas coordenadas valendo 𝐼𝑁𝐹
            if(solution[0] == INF or solution[1] == INF):
                print("Função Ilimitada")
            return solution, minimum
        #Caso o problema seja de maximização retornamos a solução máxima
        solution, maximum = self.GetMax()
        #Caso a solução tenha alguma de suas coordenadas valendo 𝐼𝑁𝐹
        if(solution[0] == INF or solution[1] == INF):
            print("Função Ilimitada")
        return solution, maximum