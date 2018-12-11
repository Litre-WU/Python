# -*- coding: utf-8 -*-

__author__ = 'Liter WU'

import random


print('猜数字数字游戏')
print('v0.1')
print('\n')
n = random. randint(1, 100)
a = 0
print('我已经想好 了一个数字, 它们在1到100之间,看你几次能猜对!')
print()
print('.................................')
print()
while True:
    s = input('请输入: ')
    a = a+1
    i = int(s)

    if i == n:
        print('恭喜你，猜对了,你一共猜了%s次，太厉害了!' % a)
        break
    else:
        if i > n:
            print()
            print('你猜错了,太大了,你再猜')
            print()
            print()
            print()
        else:
            print()
            print('你猜错了,太小了,你再猜')
            print()
            print('............................')
            print()
print()
print('.....................................')
print()
print('很高兴和你玩这个游戏，再见! ')

