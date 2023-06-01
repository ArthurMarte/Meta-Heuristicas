import math

#aqui estão as duas funções objetivo utilizadas
def funcaoObjetivo(solucao, func_escolhida):
     x, y = solucao
     if(func_escolhida == 1):
          return x**2 + y**2 + 25 * (math.sin(x)**2 + math.sin(y)**2)
     elif(func_escolhida == 2):
          return -(y + 47) * math.sin(math.sqrt(abs(y + 0.5 * x + 47))) - x * math.sin(math.sqrt(abs(x - (y + 47))))