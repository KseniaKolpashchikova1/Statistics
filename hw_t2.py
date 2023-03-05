# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, 
# из второго - 4. 
# Какова вероятность того, что 3 мяча белые?
from math import factorial

def combinations (n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

# 1)благоприятствующие исходы (m)
m_1 = combinations(10, 3)
print(f'благоприятствующие исходы = {m_1}')

# 2)неблагоприятствующие исходы (m)
m_2 = combinations(10, 3)
print(f'неблагоприятствующие исходы = {m_2}')

# 2)общее количество исходов (n)
n = combinations(20, 6)
print(f'общее количество исходов = {n}')

# 3)вероятность того, что достанем 3 белых шарика из 2 ящиков
P = (m_1*m_2)/n
print(f'вероятность того, что достанем 3 белых шарика из 2 ящиков = {round(P,2)}')