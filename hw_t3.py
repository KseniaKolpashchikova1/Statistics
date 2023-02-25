# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial

def combinations (n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

# 1)благоприятствующие исходы (m)
m = combinations (9, 3)
print(f'm = {m}')

# 2)общее количество исходов (n)
n = combinations (15, 3)
print(f'n = {n}')

# 3)вероятность того, что все извлеченные детали окрашены
P = m/n
print(f'P = {round(P,4)}')