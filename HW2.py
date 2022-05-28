# Задание № 1
lst = [123, 11.23, "some text", False]
print([type(i) for i in lst])

#Задание № 2
lst2 = list(input("Введите эелементы списка: "))
lgth = len(lst2)
if lgth % 2 != 0:
    lgth = lgth - 1
for i in range (1,lgth,2):
    lst2[i-1], lst2[i] = lst2[i], lst2[i-1]
print(lst2)

#Задание № 3
year = {"зима":[1,2,12], "весна":[3,4,5], "лето":[6,7,8], "осень":[9,10,11]}
time_of_year = input("Введите число месяца: ")
while int(time_of_year) not in [i for i in range(1, 13)]:
    time_of_year = input("Введите корректное значение месяца от 1 до 12: ")
for i in year.keys():
    if int(time_of_year) in year[i]:
        print(F"Указанный месяц относится к времени года - {i}")

#Задание 4
my_str = input("Введите строку с пробелами: ")
my_str = my_str.split()
for i, val in enumerate(my_str, start=1):
    print (f"Номер элемента {i} = > {val[:10]}")

#Задание 5
my_list = [7, 5, 3, 3, 2]
new_elmnt = 0
while True:
    new_elmnt = input("Введите новое значение рейтинга: ")
    while not (new_elmnt.isdigit() or new_elmnt == "break"):
        new_elmnt = input("Введите корректное значение рейтинга (целые числа): ")
    if new_elmnt == "break":
        break
    my_list.append(int(new_elmnt))
    my_list.sort(reverse=True)
    print(my_list)

#Задание № 6
product_list = []
product_tuple = ()
parametr_dict = {}
#получаем первичные данные от пользователя и формируем структуру данных
while True:
    number_product = input("Введите номер товара: ")
    while not (number_product.isdigit() or number_product == "break"):
        number_product = input("Введите корректный номер товара (целое число): ")
    if number_product == "break":
        break
    name = input("Введите наименование товара: ")
    price = input("Введите цену товара: ")
    quantity = input("Введите количество товара: ")
    unit_of_measure = input("Введите единицу измерения товара: ")
    parametr_dict["название"] = name
    parametr_dict["цена"] = price
    parametr_dict["количество"] = quantity
    parametr_dict["ед"] = unit_of_measure
    product_tuple = (int(number_product), parametr_dict.copy())
    product_list.append(product_tuple)
print()

#Очистим product_tuple для дальнейшего использования
temp = list(product_tuple)
temp.clear()
product_tuple = tuple(temp)

for i in product_list:
    print(i)
print()

#Собираем аналитику о товарах
name_lst = []
price_lst = []
quantity_lst = []
UOM_lst = []
for i in product_list:
    name_lst.append(i[1]["название"])
    price_lst.append(i[1]["цена"])
    quantity_lst.append(i[1]["количество"])
    UOM_lst.append(i[1]["ед"])

product_analytics = {}
product_analytics["название"] = name_lst
product_analytics["цена"] = price_lst
product_analytics["количество"] = quantity_lst
product_analytics["ед"] = UOM_lst

for i in product_analytics.items():
   print(i)







