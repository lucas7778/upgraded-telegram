from numpy import array
from numpy.linalg import solve


class MMQ:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def mmq(self):
        sx2 = []
        tx = len(self.__x)
        sx = sum(self.__x)
        for i in range(0, len(self.__x)):
            x2 = self.__x[i] ** 2
            sx2.append(x2)
            s = sum(sx2)
        sy = sum(self.__y)
        spxy = []
        for i in range(0, len(self.__x)):
            p = self.__x[i] * self.__y[i]
            spxy.append(p)
            sxy = sum(spxy)

        x_ = array([[tx, sx], [sx, s]])
        y_ = array([sy, sxy])
        c = solve(x_, y_)
        return print(c[0])
