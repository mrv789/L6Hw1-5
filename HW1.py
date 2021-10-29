import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print('Светофор:')

        print(f'Переключился на: {TrafficLight.__color[0]}')
        time.sleep(7)

        print(f'Переключился на: {TrafficLight.__color[1]}')
        time.sleep(2)

        print(f'Переключился на: {TrafficLight.__color[2]}')
        time.sleep(10)

t_light = TrafficLight()
print(t_light.running())