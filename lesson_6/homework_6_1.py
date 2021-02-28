'''
Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
'''

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print('Синалы светофорав\n')
        i = 0
        while i <= 100:
            print(f'{TrafficLight.__color[i % 3]}')
            if i % 3 == 0:
                sleep(7)
            elif i % 3 == 1:
                sleep(5)
            elif i % 3 == 2:
                sleep(2)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()