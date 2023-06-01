import math
import perturbação
import obj_function

#algoritmo de busca local baseado no hill-climbing
def buscaLocal(solucao, perturbacao, func_escolhida):
    x, y = solucao
    solucao_atual = x, y
    melhor_funcaoObj = obj_function.funcaoObjetivo(solucao_atual, func_escolhida)

    while True:
        #perturba a solução atual (melhor_solução)
        solucao_perturbada = perturbação.perturba(solucao_atual, perturbacao)
        funcaoObj_perturbada = obj_function.funcaoObjetivo(solucao_perturbada, func_escolhida)
        
        #verifica se a solução perturbada é melhor que a solução atual
        if funcaoObj_perturbada < melhor_funcaoObj:
            solucao_atual = solucao_perturbada
            melhor_funcaoObj = funcaoObj_perturbada
        else:
            break

    return solucao_atual, melhor_funcaoObj