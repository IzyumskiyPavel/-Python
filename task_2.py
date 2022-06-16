class Road:
    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        res = (self._length * self._width * Road.weight * Road.thickness) / 1000
        print(f'{res} тонн.')


r_obj = Road(20, 5000)
r_obj.calc()
