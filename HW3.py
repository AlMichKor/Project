# Задание 1
def division(a1, a2):
    if int(a2) == 0:
        print ("Деление на 0")
    else:
        return (float(a1) / float(a2))

chislitel = input("Введите числитель: ")
while not chislitel.isdigit():
    chislitel = input("Введите корректный числитель: ")
znamenatel = input("Введите знаменатель: ")
while not (znamenatel.isdigit() and znamenatel != "0"):
    znamenatel = input("Введите корректный знаменатель: ")

print(division(chislitel, znamenatel))

# Задание 2
def person_data(name, second_name, year_born, city, mail, number):
    print(f"имя - {name}, фамилия - {second_name}, год рождения - {year_born}, город проживания - {city}, e-mail - {mail}, телефон - {number}")

person_data(second_name="Иванов", name="Иван", year_born=1990, city="NigtCity", mail="фыв@fff", number = 123456)

# Задание 3
def my_func_2max(a, b, c):
    lst = [a, b, c]
    lst.sort()
    return(lst[1:])
print(my_func_2max(11, 6, 9))

#Задание 4.1
def my_func_1(x, y):
    return (x**y)

#Задание 4.2
def my_func_2(x, y):
    count = 1
    itog = x
    while count < abs(y):
        count +=1
        itog = itog * x
    if y < 0:
        return (1/itog)
    else:
        return (itog)

#Задание 5
user_string = input("Введите строку чисел: ")
user_string = list(user_string.split())
user_itog = 0
for i in user_string:
    user_itog += float(i)
print(f"Сумма чисел первой партии получилась вот такая: {user_itog}")
exit = False
while True:
    user_string = input("Добавьте числа или введите exit: ")
    user_string = list(user_string.split())
    for i in user_string:
        if i == "exit":
            exit = True
            break
        else:
            user_itog += float(i)
    print(f"Сумма чисел общая получилась вот такая: {user_itog}")
    if exit:
        break

#Задание 6 и 7
def int_func(a):
    return a.title()
print(int_func("knknk knkn MKNJH"))