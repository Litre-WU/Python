# Calculator 类(主类)

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 17:40'

from shape import Shape
from circle import Circle
from sector import Sector
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class Calculator(object):

    def __init__(self):

        self.version = '1.0'
        self.shape = [Circle(), Square(), Sector(), Rectangle(), Triangle()]

    def list(self):

        for x in range(0, len(self.shape)):
            s =self.shape[x]
            print('{:<10}{}'.format(x+1, s.name))

        Shape.print_line()

    def calc(self):

        while True:
            self.list()
            idx = input('请输入图形编号，按Q退出：')
            if idx == 'q':
                break
            Shape.print_line()

            idx = int(idx)
            s = self.shape[idx-1]
            s.run()

    def run(self):

        print('几何计算器')
        print('V{}'.format(self.version))
        self.calc()


if __name__ == '__main__':
    p = Calculator()
    p.run()

# Shape类

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 16:37'


class Shape:

    def __init__(self):

        self.name = '形状'
        self.side = 0.0
        self.area = 0.0

    def show_name(self):
        print(self.name)

    def collect_args(self):
        '''
        收集计算所需的参数
        :return:
        '''
        pass

    def calc(self):
        '''
        执行计算
        :return:
        '''
        pass

    def show_result(self):
        '''
        展示结果
        :return:
        '''
        print('周长：{:.3f}'.format(self.side))
        print('面积：{:.3f}'.format(self.area))

    def run(self):
        '''
        程序执行过程，运行生命周期
        :return:
        '''
        self.show_name()
        Shape.print_line()

        self.collect_args()
        Shape.print_line()

        self.calc()
        self.show_result()
        Shape.print_line()

    # staticmethod 装饰器
    # 使用该装饰器装饰的函数，称为静态函数，可以由类直接调用
    # 不用再创建对象
    @staticmethod
    def print_line():
        print('-'*50)

    @staticmethod
    def print_double_line():
        print('=' * 50)

# 本文件测试
if __name__ == '__main__':

    s = Shape()
    s.run()

#  Circle 类

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 17:16'

import math
from shape import Shape


class Circle(Shape):

    def __init__(self):
        # 先初始化父类的初始化函数
        super(Circle, self).__init__()
        self.name = '圆形'
        self.r = 0

    def collect_args(self):

        self.r = float(input('请输入半径：'))

    def calc(self):

        self.side = self.r*math.pi*2
        self.area = math.pi*self.r*self.r

# 本文件测试
if __name__ == '__main__':
    circle = Circle()
    circle.run()

# Sector类

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 17:29'

from circle import Circle


class Sector(Circle):
    def __init__(self):
        super(Sector, self).__init__()
        self.name = '扇形'
        self.angle = 0

    def collect_args(self):
        super(Sector,self).collect_args()
        self.angle = float(input('请输入角度：'))

    def calc(self):
        super(Sector, self).calc()
        ratio = int(input('请输入角度：'))
        ratio = self.angle / 360
        # 扇形周长
        self.side = self.side * ratio + self.r * 2
        # 扇形面积
        self.area *= ratio

# 本文件测试
if __name__ == '__main__':

    s = Sector()
    s.run()

# Square类

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 17:25'

from shape import Shape


class Square(Shape):

    def __init__(self):
        super(Square, self).__init__()
        self.name = '正方形'

    def collect_args(self):

        self.l = float(input('请输入边长：'))

    def calc(self):
            self.side = self.l * 4
            self.area = self.l * self.l

# 本文件测试
if __name__ == '__main__':
    s = Square()
    s.run()

# Rectangle类

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 19:07'
from square import Square


class Rectangle(Square):
    def __init__(self):
        super(Rectangle, self).__init__()
        self.name = '矩形'

    def collect_args(self):
        self.w = float(input('请输入矩形的宽：'))
        self.h = float(input('请输入矩形的高：'))

    def calc(self):
        self.side = 2*(self.w+self.h)
        self.area = self.w*self.h

# 本文件测试
if __name__ == '__main__':
    r = Rectangle()
    r.run()

# Triangle类

# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/18 19:20'

import math
from shape import Shape


class Triangle(Shape):

    def __init__(self):
        super(Triangle, self).__init__()
        self.name = '三角形'

    def collect_args(self):

        self.one = float(input('请输入三角形的第一条边:'))
        self.two = float(input('请输入三角形的第二条边:'))
        self.three = float(input('请输入三角形的第三条边:'))
        if self.one + self.two <= self.three:
            self.three = float(input('请重新输入三角形的第三条边:'))

    def calc(self):
        self.side = self.one+self.two+self.three
        self.area = math.sqrt(self.side/2 * (self.side/2 - self.one) * (self.side/2 - self.two) * (self.side/2 - self.three))
# 本文件测试

if __name__ == '__main__':

    t = Triangle()
    t.run()