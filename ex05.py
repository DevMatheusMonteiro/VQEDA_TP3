def teams(candidates, k, start=0, current="", result=None):
    if result is None:
        result = []
    if len(current) == k:
        result.append(current)
        return
    for i in range(start, len(candidates)):
        teams(candidates, k, i + 1, current + candidates[i], result)
    return result

combinacoes = teams(["A", "B", "C", "D", "E"], 2)
print(combinacoes)
combinacoes = teams(["A", "B", "C", "D", "E"], 3)
print(combinacoes)
combinacoes = teams(["A", "B", "C", "D", "E"], 4)
print(combinacoes)
combinacoes = teams(["A", "B", "C", "D", "E"], 5)
print(combinacoes)
