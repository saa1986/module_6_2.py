class Vehicle: # Определяем класс Vehicle (Транспортное средство)

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    # Список допустимых цветов (с приватным доступом)

    def __init__(self, owner, model, color, engine_power): # Конструктор для инициализации объекта класса
        self.owner = owner # Установка владельца транспортного средства
        self.__model = model # Установка модели (приватно)
        self.__color = color # Установка цвета (приватно)
        self.__engine_power = engine_power # Установка мощности двигателя (приватно)

    def get_model(self): # Метод для получения модели транспортного средства
        return f"Модель: {self.__model}"  # Возвращает строку с моделью

    def get_horsepower(self): # Метод для получения мощности двигателя
        return f"Мощность двигателя: {self.__engine_power}" # Возвращает строку с мощностью

    def get_color(self): # Метод для получения цвета транспортного средства
        return f"Цвет: {self.__color}"  # Возвращает строку с цветом

    def print_info(self): # Метод для вывода всей информации о транспортном средстве
        info = [self.get_model(), self.get_horsepower(), self.get_color(), f"Владелец: {self.owner}"]
        # Собираем информацию в список
        print('\n'.join(info))  # Выводим информацию, разделяя строки


    def set_color(self, new_color): # Метод для изменения цвета транспортного средства
        if new_color.lower() in self.__COLOR_VARIANTS:  # Проверяем, если новый цвет допустим
            self.__color = new_color # Устанавливаем новый цвет
        else: # Если цвет недопустим
            print(f"Нельзя сменить цвет на {new_color}") #Выводим сообщение об ошибке


class Sedan(Vehicle):  # Определяем класс Sedan (Седан), который наследуется от Vehicle
    __PASSENGERS_LIMIT = 5 # Максимальное количество пассажиров

# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
#Создание экземпляра класса Sedan

vehicle1.print_info() # Вызов метода для печати информации о транспортном средстве

vehicle1.set_color('Pink') # Попытка установить цвет на розовый (недопустимо)
vehicle1.set_color('BLACK')  # Попытка установить цвет на черный (допустимо)
vehicle1.owner = 'Vasyok'  # Изменение владельца транспортного средства

vehicle1.print_info() # Повторный вызов метода для печати обновленной информации