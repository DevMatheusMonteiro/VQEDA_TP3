""" 
    Com array ordenado ou invertido o quicksort particionam mal os elementos, 
    nesses dois casos o pivô se mantém em uma extremidade do subarray em vez do meio.
    Já em um array de ordem aleatória o pivô na média dos casos se mantém no meio, 
    particionando melhor os elementos e levando menos passos para concluir a ordenação.
"""

def particionar(array, inicio, fim):
    index_pivo = fim
    pivo = array[index_pivo]
    esquerda = inicio
    direita = fim - 1
    while True:
        while array[esquerda] < pivo:
            esquerda += 1
        while array[direita] > pivo and direita > esquerda:
            direita -= 1
        if esquerda >= direita:
            break
        array[esquerda], array[direita] = array[direita], array[esquerda]
        esquerda += 1
    array[esquerda], array[index_pivo] = array[index_pivo], array[esquerda]
    return esquerda
def quicksort(array, inicio=0, fim=None):
    if fim is None:
        fim = len(array) - 1
    if fim - inicio > 0:
        index_pivo = particionar(array, inicio, fim)
        quicksort(array, inicio, index_pivo - 1)
        quicksort(array, index_pivo + 1, fim)

array = [1,2,3,4,5]
quicksort(array)
print(f"Ordenado: {array}")

array = [5,4,3,2,1]
quicksort(array)
print(f"Ordem invertida: {array}")

array = [3,2,5,1,4]
quicksort(array)
print(f"Ordem aleatória: {array}")
