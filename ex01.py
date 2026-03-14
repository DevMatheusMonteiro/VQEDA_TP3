def mult(x, y, count=1):
    print(f"Chamada: {count}")
    num = -x if (y < 0) else x
    if y == 0 or x == 0:
        print("Caso base caso os valores x ou y seja 0 (se um dos dois for 0, retorna 0)")
        return 0
    if count >= abs(y):
        print(
            "Caso base para contador maior ou igual a y "
            "(se for igual ou maior, retorna o valor de x)"
        )
        return num
    result = num + mult(x, y, count + 1)
    print(
        f"Resultado: {result} - Contador: {count}. "
        "A soma ocorre após resolver mult(x,y)"
    )
    return result

print(mult(-7, -10))
print(mult(7, -10))
print(mult(10, -10))
print(mult(-7, 10))
print(mult(9, 0))