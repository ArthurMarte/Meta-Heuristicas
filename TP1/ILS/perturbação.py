import random

def perturba(solucao, perturbacao):
    x, y = solucao
    #perturba a solução adicionando um valor aleatório à x e y
    perturba_x = x + random.uniform(-perturbacao, perturbacao)
    perturba_y = y + random.uniform(-perturbacao, perturbacao)

    return perturba_x, perturba_y