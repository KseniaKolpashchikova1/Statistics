# 4) Есть ли статистически значимые различия в росте дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

import numpy as np
import scipy.stats as stats

x = np.array([172,177,158,170,178,175,164,160,169])
y = np.array([173,175,162,174,175,168,155,170,160])
α = 0.025
print(stats.ttest_ind(x,y))
d1 = np.var(x,ddof=1)
print(f'Дисперсия x = {round(d1,3)}')
d2 = np.var(y,ddof=1)
print(f'Дисперсия y = {round(d2,3)}')
m1 = np.mean(x)
print(f'Среднее арифметическое x = {round(m1,3)}')
m2 = np.mean(y)
print(f'Среднее арифметическое y = {round(m2,3)}')
t_n=(m1-m2)/(np.sqrt((d1/len(x))+(d2/len(y))))
print(f'Наблюдаемый t критерий: {round(t_n,3)}')
t_t= stats.t.ppf(0.975,16)
print(f'Табличный t критерий: {round(t_t,3)}')
if t_t>t_n: 
    print('Результат: мы принимаем нулевую гипотезу о том, что различий нет')
else: 
    print('Результат: мы принимаем альтернативную гипотезу о том, что различия есть')