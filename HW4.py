#Задание 1
from sys import argv
def salary(production, pay_per_hour, bonus):
    if  (production.isdigit() and pay_per_hour.isdigit() and bonus.isdigit()):
        itog = float(production) * float(pay_per_hour) + float(bonus)
        return (f"Заработная плата = {itog}")
    else:
        return ("Параметры некорректные")
print(salary(argv[1], argv[2], argv[3]))

#Задание 2
nums = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
nums_mod = [n for n in nums if (nums.index(n) > 0 and nums[nums.index(n)] > nums[nums.index(n)-1])]
print(nums_mod)

#Задание 3
nums_range = [n for n in range(20, 241) if (n % 20 == 0 or n % 21 == 0)]
print(nums_range)

#Задание 4
nums_4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
nums_4_mod = [n for n in nums_4 if nums_4.count(n) == 1]
print(nums_4_mod)

#Задание 5
from functools import reduce
new_list = [n for n in range(100, 1001) if n % 2 == 0]
composition = reduce(lambda x, y: x * y, new_list)
print(composition)

#Задание 6.1
from itertools import count
user_iterator = []
first_number = int(input("Введите первое число последовательности: "))
for n in count(first_number):
    if n > first_number+first_number:
        break
    user_iterator.append(n)
print(user_iterator)

#Задание 6.2
from itertools import cycle
user_iterator_6_2 = []
user_str = input("Введите свою последовательность символов: ")
user_vol_iter = int(input("Введите кол-во итераций последоствательности: "))
vol = 0
for n in cycle(user_str):
    if vol >= user_vol_iter * len(user_str):
        break
    user_iterator_6_2.append(n)
    vol += 1
print(user_iterator_6_2)

#Задание 7
def user_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *=i
        yield result
for i in user_factorial(int(input("Введите число: "))):
    print(i)