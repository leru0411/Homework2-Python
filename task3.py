#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
n = int(input('Введите число: '))
for i in range(1, n + 1):
    print(f'{i}: {(1 + 1/i)**i}')