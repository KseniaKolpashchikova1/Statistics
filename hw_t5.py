# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

# Формула: P(B/A) = (P(A/B)*P(B))/P(A)
# Полная вероятность брака
marriage_d1 = 0.1
marriage_d2 = 0.2
marriage_d3 = 0.25
all_marriage = marriage_d1 + marriage_d2 + marriage_d3
print(f'Вероятность брака всех деталей: {all_marriage:.2%}')
print('-'*20)
two_marriage_det = (marriage_d1 + marriage_d2)/all_marriage
two_marriage_det_2 = (marriage_d2 + marriage_d3)/all_marriage
two_marriage_det_3 = (marriage_d1 + marriage_d3)/all_marriage
print(f'Вероятность брака 1 и 2 деталей: {two_marriage_det:.2%}\n',
      f'Вероятность брака 2 и 3 деталей:{two_marriage_det_2:.2%}\n',
      f'Вероятность брака 1 и 3 деталей:{two_marriage_det_3:.2%}')
print('-'*20)
one_marriage_det = marriage_d1/all_marriage
one_marriage_det_2 = marriage_d2/all_marriage
one_marriage_det_3 = marriage_d3/all_marriage
print(f'Вероятность брака детали 1: {one_marriage_det:.2%}\n',
      f'Вероятность брака детали 2: {one_marriage_det_2:.2%}\n',
      f'Вероятность брака детали 3: {one_marriage_det_3:.2%}')
print('-'*20)
one_two_marriage_det = (one_marriage_det+one_marriage_det_2+one_marriage_det_3
+two_marriage_det+two_marriage_det_2+two_marriage_det_3)/all_marriage
print(f'Вероятность брака от 1 до 2 деталей: {one_two_marriage_det:.2%}')