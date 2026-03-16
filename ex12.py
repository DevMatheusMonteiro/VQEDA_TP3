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
def quickselect(array, k, inicio=0, fim=None):
    if fim is None:
        fim = len(array) - 1
    index_pivo = particionar(array, inicio, fim)
    if index_pivo == k:
        return array[index_pivo]
    if k < index_pivo:
        return quickselect(array, k, inicio, index_pivo - 1)
    return quickselect(array, k, index_pivo + 1, fim)
def testar_quicksort(array):
    global comparacoes, copias
    comparacoes = 0
    copias = 0
    quicksort(array)

def testar_quickselect(array, k):
    global comparacoes, copias
    comparacoes = 0
    copias = 0
    quickselect(array, k)

array = [1,2,3,4,5]
testar_quicksort(array)
print(f"Ordem aleatória: {array}")
print(f"Comparações: {comparacoes} - Cópias: {copias}")
array = [1,2,3,4,5]
testar_quickselect(array, len(array) // 2)
print(f"Ordem aleatória: {array}")
print(f"Comparações: {comparacoes} - Cópias: {copias}")
