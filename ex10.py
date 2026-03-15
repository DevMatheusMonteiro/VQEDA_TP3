""" 
Resultado:
    Ordenado: [1, 2, 3, 4, 5]
    Comparações: 18 - Cópias: 12    
    Ordem invertida: [1, 2, 3, 4, 5]
    Comparações: 16 - Cópias: 12    
    Ordem aleatória: [1, 2, 3, 4, 5]
    Comparações: 12 - Cópias: 12
Arrays ordenados ou invertidos degradam o desempenho do quicksort, como o pivô é o último elemento,
ele produz partições muito desbalanceadas. Arrays aleatórios tendem a gerar partições mais equilibradas, reduzindo o número de comparações.
"""

comparacoes = 0
copias = 0
def trocar(array, i, j):
    global copias
    array[i], array[j] = array[j], array[i]
    copias += 3
def particionar(array, inicio, fim):
    global comparacoes
    index_pivo = fim
    pivo = array[index_pivo]
    esquerda = inicio
    direita = fim - 1
    while True:
        while True:
            comparacoes += 1
            if not array[esquerda] < pivo:
                break
            esquerda += 1
        while True:
            comparacoes += 1
            if not (array[direita] > pivo and direita > esquerda):
                break
            direita -= 1
        if esquerda >= direita:
            break
        trocar(array, esquerda, direita)
        esquerda += 1
    trocar(array, esquerda, index_pivo)
    return esquerda
def quicksort(array, inicio=0, fim=None):
    if fim is None:
        fim = len(array) - 1
    if fim - inicio > 0:
        index_pivo = particionar(array, inicio, fim)
        quicksort(array, inicio, index_pivo - 1)
        quicksort(array, index_pivo + 1, fim)
def testar(array):
    global comparacoes, copias
    comparacoes = 0
    copias = 0
    quicksort(array)

array = [1,2,3,4,5]
testar(array)
print(f"Ordenado: {array}")
print(f"Comparações: {comparacoes} - Cópias: {copias}")

array = [5,4,3,2,1]
testar(array)
print(f"Ordem invertida: {array}")
print(f"Comparações: {comparacoes} - Cópias: {copias}")

array = [3,2,5,1,4]
testar(array)
print(f"Ordem aleatória: {array}")
print(f"Comparações: {comparacoes} - Cópias: {copias}")
