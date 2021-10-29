class Car:

    def __init__(self, speed,  color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость выше, чем положено! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} в рамках разрешоного'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше, чем положено! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} в рамках разрешоного'


class PoliceCar(Car):
    pass


town = TownCar(70, 'Серая', 'Тойота', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar(170, 'Красная', 'Ламборджини', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar(30, 'Синяя', 'Жигули', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar(100, 'Белая', 'КИА', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())