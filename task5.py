#Реализуйте алгоритм перемешивания списка.
from random import*
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

new_list = []
n = len(list)  #количество элементов список выведено в отдельную переменную для дальнейшего цикла
n1 = len(list) #то же самое, но для генерации рандомного числа из этого диапозона
while n:
    random_element = randint(1, n1)  #генерируем рандомное число в интервале от 1 до n1
    if random_element not in new_list:
        new_list.append(random_element)  #добавляем рандомное число в новый список
        n = n - 1  #уменьшение числа итераций
    else:
        continue
print(new_list)