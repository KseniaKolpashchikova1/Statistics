# В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. 
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?
from math import factorial

def combinations (n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

m = combinations(1, 1)
print(f'Благоприятствующие исходы для каждого факультета = {m}')

n = combinations(3, 1)
print(f'Общее количество исходов для каждого факультета = {n}')

P = m/n
print(f'P = {round(P,2)}')

sport_1 = (P*0.8)*((1-P)**2)
print(f'Вероятность того, что сессию сдал студент факультета А: {round(sport_1,2)}')
sport_2 = (P*0.7)*((1-P)**2)
print(f'Вероятность того, что сессию сдал студент факультета В: {round(sport_2,2)}')
sport_3 = (P*0.9)*((1-P)**2)
print(f'Вероятность того, что сессию сдал студент факультета С: {round(sport_3,2)}')
print('Итог: вероятность того, что сессию сдал студент факультета С выше')