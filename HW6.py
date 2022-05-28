# Задание 1
class TrafficLight:

    def __init__(self, color={"красный": 7, "желтый": 2, "зеленый": 1}):
        self.__color = color

    def running(self):
        from time import sleep
        import time
        for items in self.__color.items():
            print(items[0])
            time.sleep(items[1])


a1 = TrafficLight()
a1.running()


# Задание 2
class Road:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calculation(self, mass_for_one: int, thickness: int):
        massa = self._width * self._length * mass_for_one * thickness / 1000
        print(f"Масса составит {massa} тонн")


a2 = Road(20, 5000)
a2.calculation(25, 5)


# Задание 3

class Worker:

    def __init__(self, name, surname, position, wage=100, bonus=10):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        sum = 0
        for values in self._income.values():
            sum += values
        return sum


a3_1 = Position("Иван", "Иванов", "Big Boss", 200, 30)
a3_2 = Position("Петр", "Петров", "Little Boss", 100, 5)
print(a3_1.get_full_name())
print(a3_1.get_total_income())
print(vars(a3_1))

print(a3_2.get_full_name())
print(a3_2.get_total_income())
print(vars(a3_2))


# Задание 4
class Car:

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return self.speed

    def go(self):
        return "Погнали вперед!"

    def stop(self):
        return "Остановка"

    def turn(self, direction: str):
        return "Поворачиваем " + direction


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return "Вы превысили скорость для городской машины!"
        else:
            return self.speed


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость для рабочей машины!"
        else:
            return self.speed


class SportCar(Car):

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


a4_1 = TownCar(100, "Синий", "Автобус")
a4_2 = TownCar(50, "Синий", "Автобус")
a4_3 = PoliceCar(150, "Красный-синий", "Седан")
a4_4 = WorkCar(150, "Коричневый", "Седан")
a4_5 = WorkCar(50, "Коричневый", "Седан")
a4_6 = SportCar(150, "Красный", "Седан")

print(vars(a4_1))
print(vars(a4_2))
print(vars(a4_3))
print(vars(a4_4))
print(vars(a4_5))
print(vars(a4_6))

print(a4_1.show_speed())
print(a4_2.show_speed())
print(a4_1.go())
print(a4_1.stop())
print(a4_1.turn("направо"))


# Задание 5
class Stationery:

    def __init__(self, title="Базовое перо"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером")


a5_1 = Stationery("Базовое перо")
a5_2 = Pen()
a5_3 = Pencil("Карандаш")
a5_4 = Handle("Маркер")

a5_1.draw()
a5_2.draw()
a5_3.draw()
a5_4.draw()
