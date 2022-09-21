""" Задача 1.
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11 """

""" X = input('Введите вещественное число ')
sum = 0
for i in X:
   if i != ',':
      sum += int(i)
print(sum) """

"""
Задача 2.
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

""" N = int(input('Введите число N '))
numbers = [i for i in range(1, N+1)]
print(numbers)
for i in range(1,N):
    numbers[i] = numbers[i] * numbers[i-1]
print(numbers) """

"""
Задача 3.
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
"""

""" n = int(input('Введите n '))
sum = 0
for i in range(1, n+1): 
    m = ((1 + ((1 / i)-int(1/i)))**i)
    print(m)
    sum = m + sum
print(f'Сумма чисел последовательности $(1+\frac 1 n)^n$ =', {sum})   """

"""
Задача 5. 
Реализуйте алгоритм перемешивания списка. """


import random
def shuffle(spisok):
    spisok_copy = spisok[:]
    copy_length = len(spisok_copy)
    for i in range(copy_length):
        n = random.randint(0, copy_length-1)
        temp = spisok_copy[i]
        spisok_copy[i] = spisok_copy[n]
        spisok_copy[n] = temp
    return spisok_copy
list = [0, 2, 8, 10, 12]
print(list)
print(shuffle(list)) 