def knapsack(target, weights, index=0, current=None, result=None):
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
    knapsack(target - weight, weights, index + 1, current, result)
    current.pop()
    knapsack(target, weights, index + 1, current, result)
    return result

weight_list = [2,3,5,7,1]
print(knapsack(10, weight_list))
weight_list = [5,3,5,7,1,1]
print(knapsack(10, weight_list))
weight_list = [5,3,5,7,2]
print(knapsack(10, weight_list))
