chamadas_original = 0
def knapsack_original(target, weights, index=0, current=None, result=None):
    global chamadas_original
    chamadas_original += 1
    if current is None:
        current = []

    if result is None:
        result = []

    if target == 0:
        result.append(current.copy())
        return result

    if target < 0 or index == len(weights):
        return result

    weight = weights[index]
    current.append(weight)
    knapsack_original(target - weight, weights, index + 1, current, result)
    current.pop()
    knapsack_original(target, weights, index + 1, current, result)
    return result


chamadas_memo = 0
def knapsack_memo(target, weights, index=0, memo=None):
    global chamadas_memo
    chamadas_memo += 1
    if memo is None:
        memo = {}

    if (target, index) in memo:
        return memo[(target, index)]

    if target == 0:
        return [[]]

    if target < 0 or index == len(weights):
        return []

    weight = weights[index]
    combinacoes = knapsack_memo(target - weight, weights, index + 1, memo)
    combinacoes = [[weight] + c for c in combinacoes]
    pulando = knapsack_memo(target, weights, index + 1, memo)
    memo[(target, index)] = combinacoes + pulando
    return memo[(target, index)]

weight_list = [2,3,5,7,1,2]
print(knapsack_original(10, weight_list))
print(f"Sem memoização: {chamadas_original}")

weight_list = [2,3,5,7,1,2]
print(knapsack_memo(10, weight_list))
print(f"Com memoização: {chamadas_memo}")
