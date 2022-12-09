#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число '))
numbers = [0,1]
for i in range(2, n + 1):
    numbers.append(numbers[i - 1] + numbers [i - 2])
not_numbers = list(map(lambda p: p[1] * (-1)**p[0], enumerate(numbers[1:])))
not_numbers.reverse()
print (not_numbers + numbers)