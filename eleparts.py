# 商品类
class Goods(object):
    """商品"""
    def __init__(self, name, price, stock):
        self.id = 0
        self.name = name
        self.price = price
        self.stock = stock

    # 当打印对象时，输出的内容
    def __str__(self):

        return 'id：%s\n' \
               '名称：%s\n' \
               '价格：%s\n' \
               '库存：%s\n' % (self.id, self.name, self.price, self.stock)


# 本文件测试
if __name__ == '__main__':

    goods = Goods('Apple pods', 2999, 100)
    print(goods)


# 购物车类

from goods import *


class CartItem(object):
    """购物车商品"""
    def __init__(self, goods, count):

        self.goods = goods
        self.count = count

    def __str__(self):
        # %.2f 保留小数点后2位
        return '%s(￥%.2f)*%s' % (self.goods.name, self.goods.price, self.count)

    def amount(self):
        """
        计算商品小计
        :return: 小计总额
        """
        return self.goods.price * self.count


# 本文件测试
if __name__ == '__main__':
    goods = Goods('Apple Pods', 1999, 99)
    # 想创建购物车商品对象，需要传入一个商品对象
    item = CartItem(goods, 2)
    # 商品小计
    money = item.amount()
    print(money)


# 主类

from goods import Goods
from cart import CartItem


class Shop(object):
    """商店"""
    def __init__(self):
        # 存储所有商品
        self.shops = []
        # 存储购物车商品
        self.cart = []
        # 加载商品
        self.load()

    def load(self):
        """加载商品"""
        self.add(Goods('Apple Watch', 3299, 100))
        self.add(Goods('AirPods', 1288, 100))
        self.add(Goods('Home Pod', 1299, 100))
        self.add(Goods('iPhone X', 6288, 100))

    def add(self, good):
        """
        设置新商品的id，添加到列表中
        :param good: 新商品
        :return: None
        """
        good.id = len(self.shops) + 1
        self.shops.append(good)

    def print_line(self):

        print('-'*50)

    def print_double_line(self):
        print('='*50)

    def list(self):
        """列出所有商品"""
        print('请选择商品：')
        self.print_double_line()
        # 遍历商品列表
        for g in self.shops:

            print('%s       %s        %s' % (g.id, g.name, g.price))
            self.print_line()

    def list_cart(self):
        """展示购物车商品，计算总价"""
        self.print_line()
        total = 0.0
        for item in self.cart:
            print('%s     =￥%s' % (item, item.amount()))
            total += item.amount()
        self.print_line()
        print('总金额：￥%.2f' % total)

    def add_to_cart(self):
        """添加商品到购物车"""
        print('\n')
        g_id = input('请输入商品Id（回车去结账，0清空购物车）：')

        if len(g_id) == 0:
            # 结账
            total = 0.0
            for item in self.cart:

                total += item.amount()
            self.print_line()
            print('请支付：￥%.2f' % total)

            # 清空购物车
            self.cart.clear()
            print('支付成功！')

        elif g_id == '0':
            self.cart.clear()
            print('购物车已清空！')
        else:
            # 计算商品索引
            idx = int(g_id) - 1
            # 取出商品
            goods = self.shops[idx]
            self.print_line()
            print(goods)

            count = int(input('请输入购买数量：'))
            # 判断数量是否大于库存量
            while count > goods.stock:
                count = int(input('没有这么多商品，请重新输入：'))

            # 如果商品已经在购物车中，修改商品数量
            # 变量表示在购物车中是否有这个商品
            is_exsts = False
            for item in self.cart:
                if item.goods == goods:
                    # 说明在购物车中有该商品
                    is_exsts = True
                    item.count += count
                    # 减少库存
                    goods.stock -= count

            # 如果执行到这，is_exsts的值还是False，说明购物车中没有该商品
            if is_exsts == False:
                # 把商品添加到购物车
                goods.stock -= count
                self.cart.append(CartItem(goods, count))

            # 展示购物车商品，计算总价
            self.list_cart()

    def run(self):
        """运行应用程序"""
        print('电子产品商店')
        print('v1.0')
        print('\n')

        self.list()

        while True:
            self.add_to_cart()


shop = Shop()
shop.run()