
"""
    Complexidade temporal: O(log N)
    O expoente é dividido pela metade a cada chamada recursiva.
    Assim, o número de passos cresce de forma logarítmica e, 
    quando N dobra, o número de passos aumenta apenas em 1.
"""
def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y < 0:
        return 1 / power(x, -y)
    if y % 2 == 0:
        half = power(x, y // 2)
        return half * half
    return x * power(x, y-1)

print(power(4, 0))
print(power(4, 1))
print(power(7, -10))
print(power(-7, 10))
print(power(2, 16))
print(power(2, 32))
