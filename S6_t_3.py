# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import numpy as np
import scipy.stats as stats
x = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
y = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
m1 = np.mean(x)
m2 = np.mean(y)
delta = m2-m1
alfa = 0.5
d1 = np.var(x,ddof=1)
d2 = np.var(y,ddof=1)
d_all = (d1+d2)/2
SE = np.sqrt(d_all/len(x)+d_all/len(y))
t = stats.t.ppf(1 - (alfa/2),18)
L = delta-t*SE
U = delta+t*SE
print(f'Доверительный интервал для разности среднего роста: {round(L,3)}; {round(U,3)}')
