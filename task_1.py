import time


class TrafficLight:
    __color = ''

    def __init__(self):
        self.color_and_duration = [('red', 7), ('yellow', 2), ('green', 5)]

    def running(self):
        for color, duration in self.color_and_duration:
            self.__color = color
            print(f'Цвет светофора: {self.__color}')
            time.sleep(duration)


trafficlight = TrafficLight()
trafficlight.running()
