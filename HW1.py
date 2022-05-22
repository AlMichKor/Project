# Задание 1
string1 = input("Введите любое число: ")
print(int(string1))

string2 = input("Введите любое текст: ")
print(str(string2))

# Задание 3
number1 = input("Введите целое положительное число : ")
itog = 0
for i in range (1, int(number1)+1):
    sumnumber = i * number1
    itog = int(itog) + int(sumnumber)
print(itog)

# Задание 4
number2 = input("Введите целое положительное число: ")
maxitog = 0
count = 0
while (count < len(number2)):
    if int(maxitog) < int(number2[count:count+1]):
        maxitog = number2[count:count+1]
    count += 1
print(maxitog)

#Задание 5 и 6
Income = float(input("Введите выручку: "))
while Income <= 0:
    Income = float(input("Введите корректную выручку (больше 0): "))
Costs = float(input("Введите издержки: "))
while Costs <= 0:
    Costs = float(input("Введите корректные издержки (больше 0): "))
Profit = Income - Costs
if Profit < 0:
    print("Ваш убыток = ", Profit * -1)
else:
    print("Ваша прибыль = ", Profit)
    print("Рентабельность = ", Profit / Income)
    Personal = int(input("Введите численность компании: "))
    while Personal <= 0:
        Personal = int(input("Введите корректное значение численности: "))
    print("Прибыль на одного сотрудника = ", Profit / Personal)

# Задание 7
a = float(input("Количество км в 1-ый день: "))
b = float(input("Цель в км: "))
с = 1
while a < b:
    a = a * 1.1
    с += 1
print("На " + str(с) + " день спортсмен достиг цели")