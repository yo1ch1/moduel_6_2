class Vehicle:
    __COLOR_VARIANTS = ["red", "blue", "green", "black", "white"]

    def __init__(self, owner, __model, __color,__engine):
        if isinstance(owner,str):
            self.owner = owner
        if isinstance(__model,str):
            self.__model = __model
        if isinstance(__color,str):
            self.__color = __color
        if isinstance(__engine,int):
            self.__engine = __engine

    def get_model(self):
        if isinstance(self.__model,str):
            return print(f'"Модель: {self.__model}"')

    def get_hourepower(self):
        if isinstance(self.__engine,int):
            return print(f'"Мощность двигателя: {self.__engine}"')

    def get_color(self):
        if isinstance(self.__color,str):
            return print(f'"Цвет: {self.__color}"')

    def print_info(self):
        self.get_model()
        self.get_hourepower()
        self.get_color()
        print(f'"Владелец: {self.owner}"')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'"Нельзя сменить цвет на {new_color}"')



class Sedan(Vehicle):
    __PASSENGER_LIMIT= 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()