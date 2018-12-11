# -*- coding: utf-8 -*-
__author__ = 'Liter WU'

import requests


def music():

    while True:
        musiclist = result['musiclist']
        for x in range(0, 99):
            list_music = musiclist[x]
            music_name = list_music['name']
            print('*    歌曲名称:%s' % music_name)
            music_artist = list_music['artist']
            print('*    歌手:%s' % music_artist)
            music_album = list_music['album']
            print('*    专辑:%s' % music_album)
            music_score100 = list_music['score100']
            print('*    评分:%s' % music_score100)
            print('\n')
        return


while True:
    print('*    欢迎来到酷我新歌榜    *')
    print('*    1.查看新歌榜单')
    print('*    0.退出程序')
    select = input('*    请选择您的操作:')
    select = int(select)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    url = 'http://kbangserver.kuwo.cn/ksong.s?from=pc&fmt=json&type=bang&data=content&id=17&pn=0&rn=200&isbang=1&show_copyright_off=0&pcmp4=1&bangid=0&t=1528788054321&vipver=MUSIC_8.7.7.0_PQ'
    # 1.通过请求拿出数据
    response = requests.get(url)

    # 2.将数据转化为字典
    result = response.json()
    # print(result)

    if select == 1:
        music()
    else:
        break