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
def quickselect(array, k, inicio=0, fim=None):
    if fim is None:
        fim = len(array) - 1
    index_pivo = particionar(array, inicio, fim)
    if index_pivo == k:
        return array[index_pivo]
    if k < index_pivo:
        return quickselect(array, k, inicio, index_pivo - 1)
    return quickselect(array, k, index_pivo + 1, fim)

array = [7,2,1,8,6,3,5,4]
print(f"Mediana: {quickselect(array, len(array) // 2)}")
