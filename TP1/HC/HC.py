import obj_function
import random


def hillClimbing(max_iter, inferior, superior, tam_passo, func_escolhida):

    #inicialização
    #gera uma solução candidata aleatória
    #𝑣𝑖 = (𝑙𝑠𝑖 − 𝑙𝑖𝑖) ∗ 𝑟𝑖 + 𝑙𝑖𝑖
    x = (superior - inferior) * random.uniform(0,1) + inferior
    y = (superior - inferior) * random.uniform(0,1) + inferior
    solucao = (x,y)
    #calcula o valor da solução objetivo inicial
    melhor_solucaoObj = obj_function.funcaoObjetivo(solucao, func_escolhida) #na primeira iteração a melhor função objetivo 
                                                            #é a solução com os valores de x e y iniciais

    
    #modificação
    for i in range(max_iter):
        #dar um passo
        x_candidato = solucao[0] + random.uniform(0, 1) * tam_passo
        y_candidato = solucao[1] + random.uniform(0, 1) * tam_passo
        candidato = (x_candidato, y_candidato)

        #avaliar ponto candidato
        valor_candidato = obj_function.funcaoObjetivo(candidato, func_escolhida)

        #verifica se o candidato é melhor
        if valor_candidato <= melhor_solucaoObj:
            #armazena a nova solução
            solucao, melhor_solucaoObj = candidato, valor_candidato
        

    return solucao, melhor_solucaoObj
    
