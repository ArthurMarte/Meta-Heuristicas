import ILS
import matplotlib.pyplot as plt
import numpy as np


perturbacao = 0.5  #perturbação
max_iter = 500  #número máximo de iterações

#escolhe qual função será minimizada
print('Qual função você deseja minimizar?')
print('1: x**2 + y**2 + 25 * (math.sin(x)**2 + math.sin(y)**2)')
print('2: -(y + 47) * math.sin(math.sqrt(abs(y + 0.5 * x + 47))) - x * math.sin(math.sqrt(abs(x - (y + 47))))\n')
valor = input('Escolha entre 1 e 2:')
valor = int(valor)


#recebe os limites superior e inferior para gerar o valor aleatório da solução inicial
print('\nEntre com os limites desejados:')
inferior = input('Limite inferior:')
inferior = float(inferior)
superior = input('Limite superior:')
superior = float(superior)


#lista para armazenar os valores da função objetivo retornados em cada execução
valores_objetivo = []
#armazena os valores das variáveis de decisão
melhores_solucoes = []

#executa o algoritmo ILS 30 vezes
for i in range(30):
    melhor_solucao, melhor_funcaoObj = ILS.ils(max_iter, perturbacao, inferior, superior, valor)
    valores_objetivo.append(melhor_funcaoObj)
    melhores_solucoes.append(melhor_solucao)
    print(f'\nValores da função objetivo na execução {i+1}:', melhor_funcaoObj)



# Calcular as estatísticas
media = np.mean(valores_objetivo)
valor_minimo = np.min(valores_objetivo)
valor_maximo = np.max(valores_objetivo)
desvio_padrao = np.std(valores_objetivo)
print("\n\nEstatísticas:")
print("Média:", media)
print("Valor Mínimo:", valor_minimo)
print("Valor Máximo:", valor_maximo)
print("Desvio Padrão:", desvio_padrao)


# Encontrar o índice da melhor solução
best_index = valores_objetivo.index(min(valores_objetivo))
#valores das variáveis de decisão para a melhor solução
print("\nMelhor solução encontrada:")
print("x =", melhores_solucoes[best_index][0])
print("y =", melhores_solucoes[best_index][1])


#boxplot dos resultados
plt.boxplot(valores_objetivo)
plt.title("Resultado ILS - d)")
plt.show()
