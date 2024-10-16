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