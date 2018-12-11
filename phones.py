# -*- coding: utf-8 -*-
__author__ = 'Liter WU'
__date__ = '2018/7/12 17:34'

# 数据模型
class Phone(object):
    """
    手机类
    """
    def __init__(self, name, price, stock):

        self.name = name
        self.price = price
        self.stock = stock


# 用来操作整个程序执行逻辑
class PhoneShop(object):
    """
    商店类
    """
    def __init__(self):
        # phones 存储所有手机对象
        self.phones = []

    def add(self):
        """
        添加手机
        :return:
        """
        name = input('*    请输入手机型号：')
        price = int(input('*    请输入手机价格：'))
        stock = int(input('*    请输入手机库存：'))
        # 如果添加的产品库存小于1，重新输入
        while stock < 1:
            stock = int(input('*    库存不能小于1，请重输：'))

        # 创建一个Phone对象
        phone = Phone(name=name, price=price, stock=stock)

        # 将phone对象添加到phones列表中
        self.phones.append(phone)

    def modify(self):

        print('*    a.添加新产品')
        print('*    b.修改原有产品')

        select = input('*    选择您的操作：')

        while select != 'a' and select != 'b':
            select = input('*    选项有误，请重选：')

        if select == 'a':

            self.add()
        else:
            if len(self.phones) == 0:
                print('*    没有手机信息，请稍后重试~')
                return

            for idx, phone in enumerate(self.phones):
                # 输出对象的属性值
                print('*    序号：%s   型号：%s   价格：%s   库存：%s' % (idx + 1, phone.name, phone.price, phone.stock))

            idx = int(input('*    选择要修改的序号：'))

            while idx < 1 or idx > len(self.phones):

                idx = int(input('*    序号有误，请重选：'))
            # 取出要进行修改的对象
            phone = self.phones[idx - 1]
            phone.name = input('*     请输入修改后的型号（%s）：' % phone.name)
            phone.price = int(input('*     请输入修改后的价格（%s）：' % phone.price))
            stock = int(input('*     请输入修改后的库存（%s）：' % phone.stock))

            while stock < 1:
                stock = int(input('*     库存不能少于1，请重输（%s）：' % phone.stock))

            phone.stock = stock

            print('*    修改完成！')

    def query_all(self):
        """
        查看手机
        :return:
        """
        if len(self.phones) == 0:
            print('*    没有手机产品信息，请稍后重试~ ')
            return

        # 遍历大列表，取出每一个对象
        for idx, phone in enumerate(self.phones):
            # 输出对象的属性值
            print('*    序号：%s   型号：%s' % (idx + 1, phone.name))

        print('*    a.选择序号，查看商品详情')
        print('*    b.返回上级')

        select = input('*     请选择您的操作：')
        while select != 'a' and select != 'b':
            select = input('*     选项有误，请重选：')

        if select == 'a':

            idx = int(input('*     输入产品序号：'))
            while idx < 1 or idx > len(self.phones):
                idx = int(input('*     序号有误，请重选：'))

            phone = self.phones[idx - 1]
            print('*    序号：%s   型号：%s   价格：%s    库存：%s' % (idx, phone.name, phone.price, phone.stock))

            print('*    a.购买')
            print('*    b.取消')
            select = input('*      选择操作：')
            while select != 'a' and select != 'b':
                select = input('*     选项有误，请重选：')
            if select == 'a':

                phone.stock -= 1
                print('*    购买成功！')
                if phone.stock == 0:
                    # 库存为0，删除该产品
                    self.phones.remove(phone)

    def delete(self):

        if len(self.phones) == 0:

            print('*    没有手机产品信息，请稍后重试~')
            return
        print('*    a.选择序号删除')
        print('*    b.删除所有信息')
        print('*    c.返回上级')

        select = input('*   选择您的操作：')
        while select != 'a' and select != 'b' and select != 'c':
            select = input('*   选项有误，请重选：')

        if select == 'a':

            for idx, phone in enumerate(self.phones):
                # 输出对象的属性值
                print('*    序号：%s   型号：%s   价格：%s   库存：%s' % (idx + 1, phone.name, phone.price, phone.stock))

            idx = int(input('*    选择要修改的序号：'))

            while idx < 1 or idx > len(self.phones):
                idx = int(input('*    序号有误，请重选：'))

            phone = self.phones[idx - 1]

            is_del = input('*    确定要删除（%s）的信息？y/n：' % phone.name)

            if is_del == 'y':

                self.phones.remove(phone)
                print('*    删除成功！')

        elif select == 'b':
            is_del = input('*    确定要删除所有的信息？y/n：' )

            if is_del == 'y':
                # 删除所有数据
                self.phones.clear()
                print('*    删除成功！')

    def run(self):
        """
        启动程序
        :return: None
        """
        while True:
            print('*    欢迎使用手机销售系统  ')
            print('*    1.查看手机')
            print('*    2.修改手机信息')
            print('*    3.删除手机')
            print('*    0.退出程序')

            select = int(input('*   请选择您的操作：'))

            if select == 1:
                self.query_all()

            elif select == 2:
                self.modify()

            elif select == 3:
                self.delete()

            else:
                print('*    感谢您的使用，下次再会~')
                break


shop = PhoneShop()
shop.run()

