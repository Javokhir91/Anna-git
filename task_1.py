from math import pi
# Задача №47. 
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>

# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# 
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# transformation = lambda x: x

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')
# pi * a * b for a, b in list_of_orbits
# S = 3.14 * a * b
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     s = [pi * a * b for a, b in list_of_orbits if a != b]
#     return list_of_orbits[s.index(max(s))]

# print(find_farthest_orbit(orbits))


# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) < 2
# values = [0, 222, 10, 6] 

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7, 16]
# start_ = 5
# end_ = 15

# lst2 = [i for i in range(len(lst)) if lst[i] > start_ and lst[i] < end_]

# print(lst2)

# print(3+2+1-5+4%2-1/4+6)

lst = [1, 2, 3]
for i in lst:
    if i % 2 == 0:
        lst.append(i)
print(lst)