import random


#solução inicial gerada aleatóriamente com valores de x e y dentro dos
#limites definidos na documentação do trabalho
def solucaoInicial(inferior, superior):
    #random.uniform gera valores aleatórios de x e y dentro do intervalo desejado
    x = random.uniform(inferior, superior)
    y = random.uniform(inferior, superior)
    
    print('Valor de x e y:', x, y)
    return x, y