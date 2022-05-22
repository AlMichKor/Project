#Task 1
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_1.txt", "w") as file_task_1:
    value_to_f = input("Введите данные: ")
    while value_to_f != "":
        file_task_1.writelines(value_to_f + "\n")
        value_to_f = input("Введите еще данные: ")
print()

#Task 2
file_path = input("Введите адрес файла: ")
with open(file_path, "r") as file_task_2:
    vol_str = 0
    vol_wrd = 0
    for line in file_task_2:
        vol_str += 1
        vol_wrd = vol_wrd + len(line.split(" "))
print(f"Строк - {vol_str} штук")
print(f"Слов - {vol_wrd} штук")
print()

#Task 3
salary = {"Иванов": 10000, "Петров": 20000, "Сидоров": 15000, "Антонов": 35000, "Шмелев": 45000, "Румковский": 26000, "Шиховский": 37000, "Шоколад": 56000, "Ананьев": 56000, "Корбан": 66000}
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_3.txt", "w") as file_task_3:
    for key, value in salary.items():
        file_task_3.writelines(str(key) + " " + str(value) + "\n")

salary_task_answer = {}
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_3.txt", "r") as file_task_3:
    print("У следующих сотруднико з/п ниже 20 000:")
    for line in file_task_3:
        line = line.split(" ")
        salary_task_answer[line[0]] = int(line[1])
        if int(line[1]) < 20000:
            print(f"{line[0]}")
    print()
    print(f"Среднее значение з/п = {sum(salary_task_answer.values()) / len(salary_task_answer.values())}")
    print()

#Task 4
out_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4}
value_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_4.txt", "w") as file_task_4:
    for key, value in out_dict.items():
        file_task_4.writelines(str(key) + " - " + str(value) + "\n")
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_4.txt", "r") as file_task_4:
    for line in file_task_4:
        line = line.split(" - ")
        print(f"{value_dict[line[0]]} - {line[1]}")
        file_path_task4 = (r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_4_" + f"{int(line[1])}.txt")
        with open(file_path_task4, "w") as file_task_4_:
            file_task_4_.writelines(f"{value_dict[line[0]]} - {line[1]}")

#Task 5
user_line = input("Введите числа через пробел: ")
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_5.txt", "w") as file_task_5:
    file_task_5.writelines(user_line)
user_line = user_line.split(" ")
for i, item in enumerate(user_line):
    user_line[i] = int(item)
print(f"Сумма записанных чисел = {sum(user_line)}")

#Task 6
task_6_dict = {}
with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_6.txt", "r", encoding='utf-8') as file_task_6:
    for line in file_task_6:
        line = line.split(":")
        task_6_dict[line[0]] = line[1]
for i in task_6_dict.items():
    sum_hour = []
    sum_hour_value = ""
    for j in i[1]:
        if j.isdigit():
            sum_hour_value += j
        else:
            sum_hour.append(sum_hour_value)
            sum_hour_value = ""
    sum_hour = list(filter(None, sum_hour))
    for i_en, item in enumerate(sum_hour):
        sum_hour[i_en] = int(item)
    task_6_dict[i[0]] = sum(sum_hour)


#Task 7
import json

list_of_profit = []
task7_list = []
task7_dict_firm = {}
task7_dict_profit = {}

with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_7.txt", "r", encoding='utf-8') as file_task_7:
    for line in file_task_7:
        line = line.split()
        if int(line[2]) > int(line[3]):
            list_of_profit.append(int(line[2]) - int(line[3]))
        task7_dict_firm[line[0]] = int(line[2]) - int(line[3])
task7_dict_profit["average_profit"] = sum(list_of_profit) / len(list_of_profit)
task7_list.append(task7_dict_firm)
task7_list.append(task7_dict_profit)

with open(r"C:\Users\amkorotkov\PycharmProjects\pythonProject1\project file\task_7.json", "w") as write_f:
    json.dump(task7_list, write_f)







