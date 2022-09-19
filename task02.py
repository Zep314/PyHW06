# Задача 43: Дана последовательность чисел. Получить список
# уникальных элементов заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

def get_uniq(local_list: list) -> list:
    dict1={}
    for i in local_list:
        if dict1.get(i,False):
            dict1[i] += 1
        else:
           dict1[i] = 1
    return [k for (k,v) in dict1.items() if v == 1]

#my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_list = [randint(0,10) for _ in range(10)]

print(f"Исходный список: {my_list}")
print(f"Обработанный список: {get_uniq(my_list)}")


##########################################################
################## Вывод результата ######################
##########################################################
# Исходный список: [3, 4, 10, 10, 10, 4, 7, 0, 4, 10]
# Обработанный список: [3, 7, 0]