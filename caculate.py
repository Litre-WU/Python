# -*- coding: utf-8 -*-
__author__ = 'Liter'
__date__ = '2018/7/13 17:05'

import math

class Geometry(object):

    def __init__(self, name=''):
        self.name = name
        self.list = []

    def show_list(self):

        self.list.append(Geometry(name='圆形'))

        self.list.append(Geometry(name='扇形'))

        self.list.append(Geometry(name='正方形'))

        self.list.append(Geometry(name='矩形'))

        self.list.append(Geometry(name='三角形'))
        for idx, x in enumerate(self.list):

            print('%s   %s' % (idx+1, x.name))

    def select(self):
        self.show_list()
        print('-------------------------------')
        print('\n')

        while True:
            idx = input('请输入图形编号(退出请按Q):')
            if idx =='q' or idx =='Q':
                return
            else:
                idx = int(idx)
                print('--------------------------------')
                while idx < 1 or idx > len(self.list):
                    idx = int(input('编号有误，请重选：'))

                x = self.list[idx - 1]
                print('%s' % x.name)
                print('--------------------------------')
                if idx == 1:
                    r = int(input('请输入半径:'))
                    l = 2*math.pi*r
                    s = math.pi*r*r/2
                    print('--------------------------------')
                    print('周长:%s' % l)
                    print('面积:%s' % s)
                    print('--------------------------------')
                elif idx == 2:
                    r = int(input('请输入半径:'))
                    n = int(input('请输入角度:'))
                    l = n*math.pi*r/180+2*r
                    s = n*math.pi*r*r/360
                    print('--------------------------------')
                    print('周长:%s' % l)
                    print('面积:%s' % s)
                    print('--------------------------------')
                elif idx == 3:
                    w = int(input('请输入边长:'))
                    l = 4*w
                    s = w*w
                    print('--------------------------------')
                    print('周长:%s' % l)
                    print('面积:%s' % s)
                    print('--------------------------------')
                elif idx == 4:
                    w = int(input('请输入长:'))
                    h = int(input('请输入宽:'))
                    l = 2*(h+w)
                    s = h*w
                    print('--------------------------------')
                    print('周长:%s' % l)
                    print('面积:%s' % s)
                    print('--------------------------------')
                elif idx == 5:
                    a = int(input('请输入三角形的一条边:'))
                    b = int(input('请输入三角形的另一条边:'))
                    c = int(input('请输入三角形的第三条边:'))
                    if a+b>c and math.fabs(a-b)<c:
                        l = a + b + c
                        p = l / 2
                        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
                        print('--------------------------------')
                        print('周长:%s' % l)
                        print('面积:%s' % s)
                        print('--------------------------------')
                    else:
                        c = int(input('请重新输入三角形的第三条边:'))
                        l = a + b + c
                        p = l / 2
                        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
                        print('--------------------------------')
                        print('周长:%s' % l)
                        print('面积:%s' % s)
                        print('--------------------------------')
                else:
                    if input() == 'q':
                        print('输入错误')
                        break

    def run(self):
        print('几何计算器')
        print('v0.1')
        print('\n')
        print('请选择几何图形：')
        print('===============================')

        self.select()


geometry = Geometry()
geometry.run()

