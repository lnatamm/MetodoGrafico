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
    
    def AddEq(a1, b1, b): # Adiciona a equação 𝑎1𝑥 + 𝑎2𝑦 = 𝑏 à matriz 𝐴𝑏
        pass

    def ListEq(): # Lista as equações, numeradas de 0 a 𝑛 − 1
        pass

    def RemoveEq(k): # remove a 𝑘-ésima equação da matriz 𝐴𝑏. Não é possível remover as equações 0, 1, 2 e 3, dadas pela inicialização
        pass
    
    def CheckPoint(x0, y0): # Testa se o ponto (𝑥0, 𝑦0) satisfaz todas as condições do problema
        pass

    def GetSolution(): # Retorna uma solução ótima do problema. Caso a solução tenha alguma de suas coordenadas valendo 𝐼𝑁𝐹, retorna a string "Função Ilimitada".
        pass