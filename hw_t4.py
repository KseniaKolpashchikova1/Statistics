# В лотерее 100 билетов. Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial

def combinations (n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

# 1)благоприятствующие исходы (m)
m = combinations (2, 2)
print(f'm = {m}')

# 2)общее количество исходов (n)
n = combinations (100, 2)
print(f'n = {n}')

# 3)вероятность того, что 2 приобретенных билета окажутся выигрышными
P = m/n
print(f'P = {round(P,4)}')