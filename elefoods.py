# -*- coding: utf-8 -*-
__author__ = 'Liter'
__date__ = '2018/7/13 14:18'


class Shop(object):

    def __init__(self, name='', price='', stock=0):
        self.name = name
        self.price = price
        self.stock = stock

        self.list = []

    def show_shop(self):

        print('========================================')
        s1 = Shop(name='Apple Watch', price='￥3299.00', stock=100)
        self.list.append(s1)
        s2 = Shop(name='AirPods', price='￥1288.00', stock=100)
        self.list.append(s2)
        s3 = Shop(name='Home Pod', price='￥1299.00', stock=100)
        self.list.append(s3)
        # print(self.list)
        for idx, x in enumerate(self.list):

            print('%s       %s      %s' % (idx + 1, x.name, x.price))
            print('-------------------------------------')

    def select_shop(self):
        self.show_shop()
        while True:
            idx = int(input('请输入商品ID（回车去结账，0清空购物车）:'))
            print('\n')
            while idx < 1 or idx > len(self.list):
                idx = int(input('ID有误，请重新输入：'))

            x = self.list[idx - 1]
            print('ID：%s   名称：%s   价格：%s    库存：%s' % (idx, x.name, x.price, x.stock))
            print('\n')
            buy_num = int(input('请输入购买数量:'))
            print('\n')
            x.price = x.price.strip('￥')
            cash = float(x.price) * buy_num
            print('-------------------------')
            print('%s(%s)*%s    =￥%.2f' % (x.name, x.price, buy_num, cash))
            print('-------------------------')
            print('\n')
            print('总金额:%.2f' % cash)
            print('\n')

    def run(self):

        print('电子产品商店')
        print('v0.1')
        print('\n')
        print('请选择商品：')

        self.select_shop()


shop = Shop()
shop.run()