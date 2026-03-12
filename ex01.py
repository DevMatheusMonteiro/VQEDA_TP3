def mult(x, y, count=1):
    if y == 0 or x == 0:
        print("Caso base caso os valores x ou y sejam 0 (se um dos dois for 0, retorna 0)")
        return 0
    if count >= y:
        print(
            "Caso base para contador maior ou igual a y "
            "(se for igual ou maior, retorna o valor de x)"
        )
        return x
    result = x + mult(x, y, count + 1)
    print(
        f"Resultado: {result} - Contador: {count}. "
        "A soma ocorre após resolver mult(x,y)"
    )
    return result

print(mult(7, 2))
print(mult(9, 0))