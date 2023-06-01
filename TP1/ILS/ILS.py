import init_solution 
import perturbação
import busca_local
import obj_function

#Critério de parada: número máximo de iterações
def ils(max_iter, perturbacao, inferior, superior, func_escolhida):
    melhor_solucao = init_solution.solucaoInicial(inferior, superior) #na primeira iteração a melhor solução é a inicial
    melhor_solucaoObj = obj_function.funcaoObjetivo(melhor_solucao, func_escolhida) #na primeira iteração a melhor função objetivo 
                                                                    #é a solução com os valores de x e y iniciais

    for i in range(max_iter):
        #faz uma busca local na solução atual
        solucao_atual, solucaoObjAtual = busca_local.buscaLocal(melhor_solucao, perturbacao, func_escolhida)

        # Se a função objetivo perturbada for melhor que a melhor solução objetivo encontrada até o momento ela atualiza
        if solucaoObjAtual < melhor_solucaoObj:
            melhor_solucao = solucao_atual
            melhor_solucaoObj = solucaoObjAtual


    return melhor_solucao, melhor_solucaoObj



