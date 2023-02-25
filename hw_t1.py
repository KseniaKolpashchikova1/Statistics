# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 

from math import factorial

def combinations (n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

# 1)благоприятствующие исходы (m)
m = combinations(13, 4)
print(f'm = {m}')

# 2)общее количество исходов (n)
n = combinations(52, 4)
print(f'n = {n}')

# 3)вероятность того, что все карты – крести
P = m/n
print(f'P = {round(P,4)}')

print('―' * 10)
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
# 1)благоприятствующие исходы (m1)
m1 = sum([combinations(4,1)*combinations(48,3), combinations(4,2)*combinations(48,2), combinations(4,3)*combinations(48,1), 1])
print(f'm1 = {m1}')

# 2)общее количество исходов (n1)
n1 = combinations(52, 4)
print(f'n1 = {n1}')

# 3)вероятность того, что среди 4-х карт окажется хотя бы один туз
P1 = m1/n1
print(f'P1 = {round(P1,4)}')